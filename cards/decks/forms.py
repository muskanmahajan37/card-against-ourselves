from django import forms

class DeckForm(forms.Form):
    name = forms.CharField(label='Deck name', max_length=120, widget=forms.TextInput)
    name.widget.attrs.update({'class': 'validate', 'data-length': '120'})
