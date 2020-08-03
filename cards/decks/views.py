from django.shortcuts import render

# Create your views here.

def creator(request):
    return render(request, 'decks/creator.html')