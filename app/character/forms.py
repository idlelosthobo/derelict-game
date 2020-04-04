from django import forms
from app.character import models


class CharacterCreateForm(forms.ModelForm):

    class Meta:
        model = models.Character
        exclude = [
            'user',
        ]
        labels = {
            'name': 'Character Name',
        }
        widgets = {
        }