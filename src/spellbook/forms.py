from django import forms

from .models import Spell, Spellbook, SpellUsage


class SpellbookForm(forms.ModelForm):
    class Meta:
        model = Spellbook
        fields = ['name']


class AddSpellToSpellbookForm(forms.Form):
    spell_pk = forms.IntegerField(label="spell_pk")

    def clean_spell_pk(self):
        pk = self.cleaned_data['spell_pk']
        self.cleaned_data['spell'] = Spell.objects.get(pk=pk)
        return pk
