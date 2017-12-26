from django.core import serializers
from django.http import HttpResponse
from django.views.generic.list import ListView

from spellbook.models import Spell


class SpellListView(ListView):
    model = Spell


def spell_list_json(request):
    """Return the spell list as a JSON"""
    fields = ['name', 'level', 'spell_range', 'cast_type', 'description']
    spells = serializers.serialize('json',
                                   Spell.objects.all(),
                                   fields=fields)

    return HttpResponse(spells, content_type="application/json")
