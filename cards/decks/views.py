from django.shortcuts import render, redirect

# Create your views here.

from .models import Deck, WhiteCard, BlackCard

from .forms import DeckForm

def creator(request):

    if request.method == 'POST':

        form = DeckForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            tags = request.POST['tags']
            d = Deck(name=name, description=description, tags=tags)
            d.save()
            return redirect('deck/'+str(d.id))

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
    
    deck = Deck.objects.get(id=id)
    white = WhiteCard.objects.filter(deck__id=id)
    black = BlackCard.objects.filter(deck__id=id)
    tags = deck.tags.split(',')


    return render(request, 'decks/deck.html', {'deck': deck,
                'white': white,
                'black': black,
                'tags': tags})