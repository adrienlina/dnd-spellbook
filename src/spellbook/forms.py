from django import forms

from .models import AVAILABLE_SLOTS_LEVELS, Spell, Spellbook


class SpellbookForm(forms.ModelForm):
    class Meta:
        model = Spellbook
        fields = ['name']


class SpellbookSlotsForm(forms.Form):
    spellbook_pk = forms.IntegerField(label="spellbook")
    slot_level_field_names = [
        'spell_slots_level_%s' % spell_slot
        for spell_slot in AVAILABLE_SLOTS_LEVELS
    ]

    def __init__(self, *args, **kwargs):
        super(SpellbookSlotsForm, self).__init__(*args, **kwargs)

        for spell_slot_name in self.slot_level_field_names:
            self.fields[spell_slot_name] = forms.IntegerField(
                label=spell_slot_name,
                min_value=0,
            )

    def clean_spellbook_pk(self):
        pk = self.cleaned_data['spellbook_pk']
        try:
            self.cleaned_data['spellbook'] = Spell.objects.get(pk=pk)
        except Spell.DoesNotExist:
            raise forms.ValidationError("The spellbook does not exist")

        return pk

    def clean(self):
        self.cleaned_data['slots'] = [{
            'level': spell_slot,
            'value': self.cleaned_data[spell_slot_name],
        } for spell_slot_name, spell_slot in zip(self.slot_level_field_names,
                                                 AVAILABLE_SLOTS_LEVELS)]


class SpellPkForm(forms.Form):
    spell_pk = forms.IntegerField(label="spell_pk")

    def clean_spell_pk(self):
        pk = self.cleaned_data['spell_pk']
        try:
            self.cleaned_data['spell'] = Spell.objects.get(pk=pk)
        except Spell.DoesNotExist:
            raise forms.ValidationError("The spell does not exist")

        return pk
