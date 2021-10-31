from django import forms
from django.core.exceptions import ValidationError


class NewGameForm(forms.Form):
    player_name = forms.CharField(label='Your Name', max_length=24)
    game_name = forms.CharField(label='Game Name', max_length=32)

    """
     Do additional validation here.
    """
    def clean(self):
        cd = super().clean()

class JoinExistingGameForm(forms.Form):
    player_name = forms.CharField(label='Your Name', max_length=24)
    game_id = forms.IntegerField(label='Game ID')