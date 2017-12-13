from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView

from profiles.models import get_request_profile
from spellbook.forms import SpellbookForm, SpellPkForm
from spellbook.models import Spell, Spellbook, SpellUsage


class SpellbookListView(ListView):
    template_name = "spellbook/spellbook_list.html"

    def get_queryset(self, *args, **kwargs):
        try:
            profile = get_request_profile(self.request)
        except TypeError:
            return []

        return Spellbook.objects.filter(profile=profile)


def get_spellbook_details(request, pk):
    """Show the details of a given spellbook"""
    spellbook = get_object_or_404(Spellbook, pk=pk)
    spells = Spell.objects.all()

    context = {
        'spellbook': spellbook,
        'spells': spells,
    }

    return render(request, "spellbook/spellbook_detail.html", context)


def add_spell_to_spellbook(request, pk):
    """Add a spell to a spellbook"""
    def add_spell_usage(spellbook, spell):
        SpellUsage.objects.get_or_create(spell=spell, spellbook=spellbook)

    return _handle_spell_usage_form(request, pk, add_spell_usage)


def remove_spell_from_spellbook(request, pk):
    """Remove a spell from a spellbook"""
    def delete_spell_usage(spellbook, spell):
        SpellUsage.objects.filter(spell=spell, spellbook=spellbook).delete()

    return _handle_spell_usage_form(request, pk, delete_spell_usage)


def create_spellbook(request):
    """Show a form to create a new spellbook"""
    if request.method == 'POST':
        form = SpellbookForm(request.POST)
        if form.is_valid():
            spellbook = form.save(commit=False)
            # Find the profile of the user
            spellbook.profile = get_request_profile(request)
            spellbook.save()

            return redirect('spellbook:spellbook-detail', spellbook.pk)
    else:
        form = SpellbookForm()

        return render(request, 'spellbook/new_spellbook.html', {'form': form})


def _handle_spell_usage_form(request, pk, handler):
    """Handle a spell usage form and return to the spellbook detail view"""
    if request.method == 'POST':
        form = SpellPkForm(request.POST)
        if form.is_valid():
            spellbook = get_object_or_404(Spellbook, pk=pk)
            spell = form.cleaned_data['spell']

            handler(spellbook=spellbook, spell=spell)

    return redirect('spellbook:spellbook-detail', pk)
