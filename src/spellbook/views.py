from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView

from profiles.models import Profile
from spellbook.forms import SpellbookForm
from spellbook.models import Spell


class SpellListView(ListView):

    model = Spell


def create_spellbook(request):
    if request.method == 'POST':
        form = SpellbookForm(request.POST)
        if form.is_valid():
            spellbook = form.save(commit=False)
            # Find the profile of the user
            spellbook.profile = Profile.objects.get(user=request.user)
            spellbook.save()

            return HttpResponseRedirect(reverse('spellbook:spellbook-home'))
    else:
        form = SpellbookForm()

        return render(request, 'spellbook/new_spellbook.html', {'form': form})
