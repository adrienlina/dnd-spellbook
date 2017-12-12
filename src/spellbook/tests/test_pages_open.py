from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from profiles.models import Profile

User = get_user_model()


class SpellbookPagesOpenCase(TestCase):

    # Pages that should always open
    public_url_names = [
        'spellbook:spell-list',
        'spellbook:spellbook-home',
        'spellbook:spellbook-new',
        'spellbook:spellbook-list',
    ]

    # Pages that have a different behavior with a logged in user
    logged_in_url_names = [
        'spellbook:spellbook-list',
    ]

    def test_pages_open(self):
        """All app pages should open"""
        for url_name in self.public_url_names:
            r = self.client.get(reverse(url_name))
            self.assertEqual(r.status_code, 200)

    def test_user_pages_open(self):
        """App pages with a user-specific dynamic should open"""
        user = User(email="email@email.com", password="password")
        user.save()

        profile = Profile(user=user)
        profile.save()

        self.client.login(email="email@email.com", password="password")
        for url_name in self.logged_in_url_names:
            r = self.client.get(reverse(url_name))
            self.assertEqual(r.status_code, 200)
