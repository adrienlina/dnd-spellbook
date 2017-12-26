from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from spellbook.models import Spell, Spellbook


class SpellListView(ListView):
    model = Spell


def spell_list_json(request, spellbook_pk=None):
    """Return the spell list as a JSON, excluding the spellbook's spells if any"""
    fields = ['name', 'level', 'spell_range', 'cast_type', 'description']

    if spellbook_pk:
        spellbook = get_object_or_404(Spellbook, pk=spellbook_pk)
        query_set = Spell.objects \
            .exclude(pk__in=spellbook.spells.all().values_list('pk', flat=True))
    else:
        query_set = Spell.objects.all()

    spells = serializers.serialize('json', query_set, fields=fields)

    return HttpResponse(spells, content_type="application/json")
