from django.conf.urls import url

from spellbook.views.spell import SpellListView
from spellbook.views.spellbook import SpellbookListView, create_spellbook, get_spellbook_details

urlpatterns = [
    url(r'^home$', SpellListView.as_view(), name='spellbook-home'),
    url(r'^spells$', SpellListView.as_view(), name='spell-list'),

    url(r'^spellbooks$', SpellbookListView.as_view(), name='spellbook-list'),
    url(r'^spellbooks/(?P<pk>\d+)$', get_spellbook_details, name='spellbook-detail'),
    url(r'^spellbooks/new$', create_spellbook, name='spellbook-new'),
]
