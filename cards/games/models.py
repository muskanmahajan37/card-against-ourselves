from django.db import models
from decks.models import Deck
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# Create your models here.

class Game(models.Model):
    author = models.CharField(max_length=80, default='Dodo')
    password = models.CharField(max_length=80)
    max_users = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(10)])
    # users = models.ForeignKey()
    decks = models.ManyToManyField(Deck)
    created = models.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return self.author + '\'s ' + 'Game'