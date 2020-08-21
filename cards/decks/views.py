from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.

from .models import Deck, WhiteCard, BlackCard

from .forms import DeckForm, CardForm

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
    
    form = CardForm()

    try:
        deck = Deck.objects.get(id=id)
        white = WhiteCard.objects.filter(deck__id=id)
        black = BlackCard.objects.filter(deck__id=id)
        tags = deck.tags.split(',')
    except Deck.DoesNotExist:
        raise Http404('Deck not found.')

    return render(request, 'decks/deck.html', {'deck': deck,
                'white': white,
                'black': black,
                'tags': tags,
                'form': form})

def add_card(request):
    if request.method == 'POST':

        form = CardForm(request.POST)

        if form.is_valid():
            cards = []
            id = request.POST['id']
            deck = Deck.objects.get(id=id)
            entries = form.cleaned_data['text'].split(';')
            
            if request.POST['type'] == 'white':
                for card in entries:
                    cards.append(WhiteCard(text=card, deck=deck))
                WhiteCard.objects.bulk_create(cards)
                
            elif request.POST['type'] == 'black':
                for card in entries:
                    if card.count('_') > 0 and card.count('_') < 5:
                        cards.append(BlackCard(text=card, deck=deck))
                BlackCard.objects.bulk_create(cards)

    return redirect('deck/'+str(id))

def remove_card(request):
    if request.method == 'POST':
        id = request.POST['id']
        
        if request.POST['type'] == 'white':
            for key in request.POST.keys():
                if 'card-' in key:
                    c = WhiteCard.objects.get(id=request.POST[key])
                    if int(c.deck.id) == int(id):
                        c.delete()
                    
        elif request.POST['type'] == 'black':
            for key in request.POST.keys():
                if 'card-' in key:
                    c = BlackCard.objects.get(id=request.POST[key])
                    if int(c.deck.id) == int(id):
                        c.delete()
        
        return redirect('deck/'+str(id))
    else:
        return redirect('decks')