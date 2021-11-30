from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Music
from .serializers import MusicSerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

# Getting music by id:
@api_view(['GET', 'POST'])
def api_music(request,music_title,music_artist, music_thumbnail):
    if request.method == 'POST':
        m = 'https://images.genius.com/'+music_thumbnail
        try:
            Music.objects.get(song=music_title, artist=music_artist)
        except:
            Music.objects.create(song=music_title, artist=music_artist, thumbnail = m)
    music = Music.objects
    music.song = music_title
    music.artist = music_artist
    music.thumbnail = music_thumbnail
    serialized_music = MusicSerializer(Music.objects)
    return Response(serialized_music.data)


# Getting full playlist:
@api_view(['GET', 'POST'])
def api_playlist(request):
    if request.method == 'GET':
        playlist = Music.objects
        serialized_playlist = MusicSerializer(playlist, many=True)
        return Response(serialized_playlist.data)

# Deleting song from playlist:       
@api_view(['GET', 'POST','DELETE'])
def api_delete(request,music_title,music_artist):
    if request.method == 'DELETE':
        music = Music.objects.get(song=music_title, artist=music_artist)
        id = music.id
        playlist = Music.objects
        playlist.filter(id=id).delete()
        serialized_playlist = MusicSerializer(Music.objects, many=True)
        return Response(serialized_playlist.data)