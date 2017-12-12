from django.forms import ModelForm

from .models import Spellbook


class SpellbookForm(ModelForm):
    class Meta:
        model = Spellbook
        fields = ['name']
