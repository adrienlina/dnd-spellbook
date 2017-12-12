from django.core.urlresolvers import reverse
from django.test import TestCase


class SpellbookPagesOpenCase(TestCase):
    def test_spell_list(self):
        url = reverse('spellbook:spell-list')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_spellbook_home(self):
        url = reverse('spellbook:spellbook-home')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
