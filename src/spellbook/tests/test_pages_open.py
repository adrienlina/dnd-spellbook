from django.core.urlresolvers import reverse
from django.test import TestCase


class SpellbookPagesOpenCase(TestCase):

    url_names = [
        'spellbook:spell-list',
        'spellbook:spellbook-home',
        'spellbook:spellbook-new',
    ]

    def test_pages_open(self):
        for url_name in self.url_names:
            r = self.client.get(reverse(url_name))
            self.assertEqual(r.status_code, 200)
