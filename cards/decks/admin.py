from django.contrib import admin

from .models import Deck, WhiteCard, BlackCard

# Register your models here.

class DeckAdmin(admin.ModelAdmin):
    readonly_fields = (id,)

admin.site.register(Deck, DeckAdmin)

admin.site.register(WhiteCard)

admin.site.register(BlackCard)