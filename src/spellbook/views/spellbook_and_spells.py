from django.shortcuts import get_object_or_404, redirect

from spellbook.forms import SpellPkForm
from spellbook.models import Spellbook, SpellUsage


def add_spell_to_spellbook(request, pk):
    """Add a spell to a spellbook"""
    def add_spell_usage(spellbook, spell):
        SpellUsage.objects \
            .get_or_create(spell=spell, spellbook=spellbook)

    return _handle_spell_usage_form(request, pk, add_spell_usage)


def remove_spell_from_spellbook(request, pk):
    """Remove a spell from a spellbook"""
    def delete_spell_usage(spellbook, spell):
        SpellUsage.objects \
            .filter(spell=spell, spellbook=spellbook) \
            .delete()

    return _handle_spell_usage_form(request, pk, delete_spell_usage)


def prepare_spell_for_notebook(request, pk):
    """Prepare a spell of a notebook"""
    def prepare_spell(spellbook, spell):
        SpellUsage.objects \
            .filter(spell=spell, spellbook=spellbook) \
            .update(prepared=True)

    return _handle_spell_usage_form(request, pk, prepare_spell)


def unprepare_spell_for_notebook(request, pk):
    """Unprepare a spell of a notebook"""
    def unprepare_spell(spellbook, spell):
        SpellUsage.objects \
            .filter(spell=spell, spellbook=spellbook) \
            .update(prepared=False)

    return _handle_spell_usage_form(request, pk, unprepare_spell)


def _handle_spell_usage_form(request, pk, handler):
    """Handle a spell usage form and return to the spellbook detail view"""
    if request.method == 'POST':
        form = SpellPkForm(request.POST)
        if form.is_valid():
            spellbook = get_object_or_404(Spellbook, pk=pk)
            spell = form.cleaned_data['spell']

            handler(spellbook=spellbook, spell=spell)

    return redirect('spellbook:spellbook-detail', pk)
