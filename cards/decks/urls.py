from django.urls import path

from . import views

urlpatterns = [
    path('creator', views.creator, name='creator'),
    path('decks', views.decks, name='decks')
]