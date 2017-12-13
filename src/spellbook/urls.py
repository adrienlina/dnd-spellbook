from django.conf.urls import url

from spellbook.views.spell import SpellListView
from spellbook.views.spellbook import SpellbookListView, create_spellbook, get_spellbook_details
from spellbook.views.spellbook_and_spells import (add_spell_to_spellbook,
                                                  prepare_spell_for_notebook,
                                                  remove_spell_from_spellbook,
                                                  unprepare_spell_for_notebook)

urlpatterns = [
    url(r'^home$', SpellListView.as_view(), name='spellbook-home'),
    url(r'^spells$', SpellListView.as_view(), name='spell-list'),

    url(r'^spellbooks$',
        SpellbookListView.as_view(),
        name='spellbook-list'),
    url(r'^spellbooks/(?P<pk>\d+)$',
        get_spellbook_details,
        name='spellbook-detail'),
    url(r'^spellbooks/(?P<pk>\d+)/add$',
        add_spell_to_spellbook,
        name='spellbook-add-spell'),
    url(r'^spellbooks/(?P<pk>\d+)/remove$',
        remove_spell_from_spellbook,
        name='spellbook-remove-spell'),
    url(r'^spellbooks/(?P<pk>\d+)/prepare$',
        prepare_spell_for_notebook,
        name='spellbook-prepare-spell'),
    url(r'^spellbooks/(?P<pk>\d+)/unprepare$',
        unprepare_spell_for_notebook,
        name='spellbook-unprepare-spell'),
    url(r'^spellbooks/new$',
        create_spellbook,
        name='spellbook-new'),
]
