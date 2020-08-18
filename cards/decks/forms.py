from django import forms

class DeckForm(forms.Form):
    name = forms.CharField(label='Deck name', max_length=120, widget=forms.TextInput)
    name.widget.attrs.update({'class': 'validate', 'data-length': '120'})
    description = forms.CharField(label='Description', max_length=160, widget=forms.TextInput)
    description.widget.attrs.update({'class': 'validate', 'data-length': '160'})

class CardForm(forms.Form):
    text = forms.CharField(label='Card text', widget=forms.Textarea)
    text.widget.attrs.update({'class': 'materialize-textarea', 'placeholder': 'XD;'})