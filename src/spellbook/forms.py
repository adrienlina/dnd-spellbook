from django import forms

from .models import Spell, Spellbook


class SpellbookForm(forms.ModelForm):
    class Meta:
        model = Spellbook
        fields = ['name']


class SpellPkForm(forms.Form):
    spell_pk = forms.IntegerField(label="spell_pk")

    def clean_spell_pk(self):
        pk = self.cleaned_data['spell_pk']
        try:
            self.cleaned_data['spell'] = Spell.objects.get(pk=pk)
        except Spell.DoesNotExist:
            raise forms.ValidationError("The spell does not exist")

        return pk
