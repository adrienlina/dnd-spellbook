from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from spellbook.models import Spell, Spellbook

User = get_user_model()


class SpellbookDetailsCase(TestCase):
    """
    A spellbook should be editable through the spellbook details page
    """

    @classmethod
    def setUpTestData(cls):  # noqa: N802
        """Set up a user with a spellbook and some spells"""
        # We need a profile for a spellbook, thus we need a django user
        cls.user = User.objects.create_user(
            email='test@user.com',
            password='password',
        )

        cls.spellbook = Spellbook(
            name="spellbook_name",
            profile=cls.user.profile,
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
        self.client.login(username='test@user.com', password='password')

    def test_0_view_spellbook_and_spelss(self):
        """It should be possible to view the spellbook and spells page"""

        url = reverse('spellbook:spellbook-edit-spells', kwargs={'pk': self.spellbook.pk})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_1_add_remove_spell_to_spellbook(self):
        """It should be possible to add/remove a spell to a spellbook with a POST request"""
        add_url = reverse('spellbook:spellbook-add-spell', kwargs={'pk': self.spellbook.pk})

        # Add one spell
        r = self.client.post(add_url, {'spell_pk': self.spells[0].pk}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.spells.count(), 1)

        # Add another spell
        r = self.client.post(add_url, {'spell_pk': self.spells[1].pk}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.spells.count(), 2)

        # Try to add the first one again, it should fail because a spellbook
        # can have a spell only once
        r = self.client.post(add_url, {'spell_pk': self.spells[0].pk}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.spells.count(), 2)

        # Remove one of the spells
        remove_url = reverse('spellbook:spellbook-remove-spell', kwargs={'pk': self.spellbook.pk})
        r = self.client.post(remove_url, {'spell_pk': self.spells[0].pk}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.spells.count(), 1)
