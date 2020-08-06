from django.shortcuts import render

# Create your views here.

from .models import Deck, WhiteCard, BlackCard

def creator(request):
    return render(request, 'decks/creator.html')

def decks(request):

    decks = Deck.objects.all()

    context = {
        'decks': decks
    }

    return render(request, 'decks/decks.html', context)