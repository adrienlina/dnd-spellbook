from django.conf.urls import url
from django.urls import path

from spellbook.views.spell import SpellListView
from spellbook.views.spellbook import (SpellbookListView, create_spellbook, spellbook_detail_view,
                                       spellbook_modify_spells_view)
from spellbook.views.spellbook_and_slots import (edit_spellbook_slots, reset_spellbook_slots,
                                                 use_spellbook_slot)
from spellbook.views.spellbook_and_spells import (add_spell_to_spellbook,
                                                  prepare_spell_for_notebook,
                                                  remove_spell_from_spellbook,
                                                  unprepare_spell_for_notebook)

app_name = "spellbook"

urlpatterns = [
    url(r'^home$', SpellListView.as_view(), name='spellbook-home'),
    url(r'^spells$', SpellListView.as_view(), name='spell-list'),

    # Spellbooks related
    url(r'^spellbooks/$',
        SpellbookListView.as_view(),
        name='spellbook-list'),
    path('spellbooks/new',
         create_spellbook,
         name='spellbook-new'),
    path('spellbooks/<int:pk>/',
         spellbook_detail_view,
         name='spellbook-detail'),

    # Spells usage related
    path('spellbooks/<int:pk>/edit-spells',
         spellbook_modify_spells_view,
         name='spellbook-edit-spells'),
    path('spellbooks/<int:pk>/add',
         add_spell_to_spellbook,
         name='spellbook-add-spell'),
    path('spellbooks/<int:pk>/remove',
         remove_spell_from_spellbook,
         name='spellbook-remove-spell'),
    path('spellbooks/<int:pk>/prepare',
         prepare_spell_for_notebook,
         name='spellbook-prepare-spell'),
    path('spellbooks/<int:pk>/unprepare',
         unprepare_spell_for_notebook,
         name='spellbook-unprepare-spell'),

    # Spell slots related
    path('spellbooks/<int:pk>/spell-slots',
         edit_spellbook_slots,
         name="spellbook-edit-slots"),
    path('spellbooks/<int:pk>/use-slot/<int:slot_level>/',
         use_spellbook_slot,
         name="spellbook-use-slot"),
    path('spellbooks/<int:pk>/reset-slots/',
         reset_spellbook_slots,
         name="spellbook-reset-slots"),
    path('spellbooks/<int:pk>/reset-slots/<int:slot_level>',
         reset_spellbook_slots,
         name="spellbook-reset-slots"),
]
