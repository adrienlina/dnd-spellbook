from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import RequestFactory, TestCase

from profiles.models import Profile
from spellbook.models import Spell, Spellbook, SpellUsage

User = get_user_model()


class SpellbookModelCase(TestCase):

    @classmethod
    def setUpTestData(cls):  # noqa: N802
        """Set up a user with a spellbook and some spells"""
        # We need a profile for a spellbook, thus we need a django user
        cls.user = User(email="email@email.com", password="password")
        cls.user.save()

        cls.profile = Profile(user=cls.user)
        cls.profile.save()

        cls.spellbook = Spellbook(
            name="spellbook_name",
            profile=cls.profile,
        )
        cls.spellbook.save()

        cls.spells = [
            Spell(
                name="spell_0_name",
                level=0,
                cast_type="cast_type",
                spell_range="spell_range",
                description="description",
            ),
            Spell(
                name="spell_1_name",
                level=0,
                cast_type="cast_type",
                spell_range="spell_range",
                description="description",
            ),
        ]
        for spell in cls.spells:
            spell.save()

    def setUp(self):  # noqa: N802
        """Log in as the user"""
        self.client.login(email=self.user.email, password=self.user.password)

    def test_0_view_spellbook(self):
        """It should be possible to view the spellbook page"""

        url = reverse('spellbook:spellbook-detail', kwargs={'pk': self.spellbook.pk})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_1_add_remove_spell_to_spellbook(self):
        """It should be possible to add/remove a spell to a spellbook with a POST request"""
        add_url = reverse('spellbook:spellbook-add-spell', kwargs={'pk': self.spellbook.pk})

        # Add one spell
        r = self.client.post(add_url, {'spell_pk': self.spells[0].pk})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.spells.count(), 1)

        # Add another spell
        r = self.client.post(add_url, {'spell_pk': self.spells[1].pk})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.spells.count(), 2)

        # Try to add the first one again, it should fail because a spellbook
        # can have a spell only once
        r = self.client.post(add_url, {'spell_pk': self.spells[0].pk})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.spells.count(), 2)

        remove_url = reverse('spellbook:spellbook-remove-spell', kwargs={'pk': self.spellbook.pk})
        r = self.client.post(remove_url, {'spell_pk': self.spells[0].pk})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.spells.count(), 1)
