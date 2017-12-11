from django.conf.urls import url

from spellbook.views import SpellListView

urlpatterns = [
    url(r'^home$', SpellListView.as_view(), name='spellbook-home'),
    url(r'^spells$', SpellListView.as_view(), name='spell-list'),
]
