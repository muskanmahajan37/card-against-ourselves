from django.shortcuts import render, redirect

# Create your views here.

from .models import Deck, WhiteCard, BlackCard

from .forms import DeckForm

def creator(request):

    if request.method == 'POST':

        form = DeckForm(request.POST)

        if form.is_valid():
            
            return redirect('decks')

    else:
        form = DeckForm()

    return render(request, 'decks/creator.html', {'form': form})

def decks(request):

    decks = Deck.objects.all()

    context = {
        'decks': decks
    }

    return render(request, 'decks/decks.html', context)

def deck(request, id):
    
    return render(request, 'decks/deck.html')