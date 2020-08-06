from django.contrib import admin

from .models import Deck, WhiteCard, BlackCard

# Register your models here.

admin.site.register(Deck)

admin.site.register(WhiteCard)

admin.site.register(BlackCard)