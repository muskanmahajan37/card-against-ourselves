from django.db import models

# Create your models here.
class Deck(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='')
    tags = models.CharField(max_length=160, default='')
    author = models.CharField(max_length=120, default='dodo')

    def __str__(self):
        return self.name

class WhiteCard(models.Model):
    text = models.CharField(max_length=120)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='white_cards')

    def __str__(self):
        return self.deck.name + ' - ' + self.text

class BlackCard(models.Model):
    text = models.CharField(max_length=120)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='black_cards')

    def blank_count(self):
        return str(self.text).count('_')

    def __str__(self):
        return self.deck.name + ' - ' + self.text
