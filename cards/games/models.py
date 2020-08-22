from django.db import models
from decks.models import Deck
# Create your models here.

class Game(models.Model):
    author = models.CharField(max_length=80, default='Dodo')
    password = models.CharField(max_length=80)