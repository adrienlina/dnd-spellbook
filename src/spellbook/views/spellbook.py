from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from profiles.models import get_request_profile
from spellbook.forms import SpellbookForm
from spellbook.models import Spell, Spellbook


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


def create_spellbook(request):
    """Show a form to create a new spellbook"""
    if request.method == 'POST':
        form = SpellbookForm(request.POST)
        if form.is_valid():
            spellbook = form.save(commit=False)
            # Find the profile of the user
            spellbook.profile = get_request_profile(request)
            spellbook.save()

            return HttpResponseRedirect(reverse('spellbook:spellbook-home'))
    else:
        form = SpellbookForm()

        return render(request, 'spellbook/new_spellbook.html', {'form': form})