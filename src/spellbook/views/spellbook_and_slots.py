from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from spellbook.forms import SpellbookSlotsForm
from spellbook.models import AVAILABLE_SLOTS_LEVELS, Spellbook, SpellSlotsLevel
from spellbook.permissions import needs_login_or_token
from tools.build_url import build_url


@needs_login_or_token
def edit_spellbook_slots(request, pk):
    """Edit the spell slots attached to a spellbook"""
    spellbook = get_object_or_404(Spellbook, pk=pk)
    form = SpellbookSlotsForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            for slot in form.cleaned_data['slots']:
                SpellSlotsLevel.objects.update_or_create(
                    spellbook=spellbook,
                    level=slot['level'],
                    defaults={
                        'max_capacity': slot['value'],
                        'current_capacity': slot['value'],
                    },
                )

            return HttpResponseRedirect(
                build_url('spellbook:spellbook-detail-view',
                          args=[pk],
                          get=request.GET,  # pass token if necessary
                          ),
            )

    slots = [{
        'level': slot_level,
        'default_value': _get_default_slot_value(spellbook, slot_level)
    } for slot_level in AVAILABLE_SLOTS_LEVELS]

    context = {
        'spellbook': spellbook,
        'form': form,
        'slots': slots
    }

    return render(request, 'spellbook/spellbook_edit_slots.html', context)


def _get_default_slot_value(spellbook, level):
    try:
        return spellbook.slot_level(level).max_capacity
    except AttributeError:
        return 0
