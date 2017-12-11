from django.views.generic.list import ListView

from spellbook.models import Spell


class SpellListView(ListView):

    model = Spell
