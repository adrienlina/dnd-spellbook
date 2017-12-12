from django.conf.urls import url

from spellbook.views import SpellbookListView, SpellListView, create_spellbook

urlpatterns = [
    url(r'^home$', SpellListView.as_view(), name='spellbook-home'),
    url(r'^spells$', SpellListView.as_view(), name='spell-list'),
    url(r'^spellbooks$', SpellbookListView.as_view(), name='spellbook-list'),
    url(r'^spellbooks/new$', create_spellbook, name='spellbook-new'),
]
