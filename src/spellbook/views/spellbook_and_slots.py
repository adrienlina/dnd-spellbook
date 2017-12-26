from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render

from spellbook.forms import SpellbookSlotsForm
from spellbook.models import AVAILABLE_SLOTS_LEVELS, Spellbook, SpellSlotsLevel
from spellbook.permissions import needs_login_or_token, redirect_with_token


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

            return redirect_with_token(request,
                                       'spellbook:spellbook-detail-view',
                                       pk)

    slots = [{
        'level': slot_level,
        'default_value': _get_default_slot_value(spellbook, slot_level),
    } for slot_level in AVAILABLE_SLOTS_LEVELS]

    context = {
        'spellbook': spellbook,
        'form': form,
        'slots': slots,
    }

    return render(request, 'spellbook/spellbook_edit_slots.html', context)


@needs_login_or_token
def use_spellbook_slot(request, pk, slot_level):
    """Use one spell slot of a spellbook"""
    spellbook = get_object_or_404(Spellbook, pk=pk)

    spell_slot = spellbook.slots.get(level=slot_level)
    try:
        spell_slot.use_slot()
    except ValidationError:
        pass

    return redirect_with_token(request, 'spellbook:spellbook-detail-view', pk)


@needs_login_or_token
def reset_spellbook_slots(request, pk, slot_level=None):
    """Reset the slots of a spellbook"""
    spellbook = get_object_or_404(Spellbook, pk=pk)

    if slot_level:
        spellbook.slots.get(level=slot_level).reset_slots()
    else:
        spellbook.reset_slots()

    return redirect_with_token(request, 'spellbook:spellbook-detail-view', pk)


def _get_default_slot_value(spellbook, level):
    """
    Get the default value of a slot maximum capacity:
    - the existing maximum capacity if the slot already exists
    - 0 in other cases
    """
    try:
        return spellbook.slot_level(level).max_capacity
    except AttributeError:
        return 0
