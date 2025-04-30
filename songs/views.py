from collections import defaultdict
from django.shortcuts import render
from .models import Song

def index(request):
    songs = Song.objects.all()
    
    grouped_songs = defaultdict(list)
    for song in songs:
        grouped_songs[song.mood].append(song)

    mood_colors = {
        "romantic": "#e91e63",
        "heartbreak": "#9c27b0",
        "chill": "#03a9f4",
        "soulful": "#4caf50",
        "classical": "#ff9800",
        "old-but-gold": "#795548"
    }

    return render(request, "index.html", {
        "grouped_songs": dict(grouped_songs),
        "mood_colors": mood_colors
    })
