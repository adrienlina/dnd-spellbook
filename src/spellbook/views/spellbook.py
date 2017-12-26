from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView

from profiles.models import get_request_profile
from spellbook.forms import SpellbookForm
from spellbook.models import Spell, Spellbook
from spellbook.permissions import needs_login, needs_login_or_token


class SpellbookListView(ListView):
    template_name = "spellbook/spellbook_list.html"

    def get_queryset(self, *args, **kwargs):
        try:
            profile = get_request_profile(self.request)
        except TypeError:
            return []

        return Spellbook.objects.filter(profile=profile)


@needs_login_or_token
def spellbook_detail_view(request, pk):
    """Show the details of a given spellbook"""
    spellbook = get_object_or_404(Spellbook, pk=pk)

    spells_by_level = {}
    for spell in spellbook.spells_with_preparations:
        if spell.level not in spells_by_level:
            spells_by_level[spell.level] = {
                'level': spell.level,
                'level_as_dnd_format': spell.level_as_dnd_format,
                'slot': spellbook.slot_level(spell.level),
                'spells': [],
            }

        spells_by_level[spell.level]['spells'].append(spell)

    context = {
        'spellbook': spellbook,
        'spells_by_level': spells_by_level,
    }

    return render(request, "spellbook/spellbook_detail.html", context)


@needs_login_or_token
def spellbook_modify_spells_view(request, pk):
    """Show the list of spells of a spellbook and the available spells"""
    spellbook = get_object_or_404(Spellbook, pk=pk)
    spellbook_spells = spellbook.spells.all()
    spells = [spell
              for spell in Spell.objects.all()
              if spell not in spellbook_spells]

    context = {
        'spellbook': spellbook,
        'spells': spells,
        'spellbook_spell_actions': [
            'spellbook/widgets/spellbook_prepare_spell.html',
            'spellbook/widgets/spellbook_remove_spell.html',
        ],
        'other_spell_actions': [
            'spellbook/widgets/spellbook_add_spell.html',
        ],
    }

    return render(request, "spellbook/spellbook_modify_spells.html", context)


@needs_login
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
