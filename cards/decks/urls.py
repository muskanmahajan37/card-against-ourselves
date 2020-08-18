from django.urls import path

from . import views

urlpatterns = [
    path('creator', views.creator, name='creator'),
    path('decks', views.decks, name='decks'),
    path('deck/<int:id>', views.deck, name='deck'),
    path('add_card', views.add_card, name='add')
]