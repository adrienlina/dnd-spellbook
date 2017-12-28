from django.contrib.auth import get_user_model
from django.test import TestCase

from profiles.models import Profile
from spellbook.models import Spell, Spellbook, SpellUsage

from .test_spell_model import TEST_SPELL_EXAMPLE_FIELDS

User = get_user_model()


class SpellbookModelCase(TestCase):

    @classmethod
    def setUpTestData(cls):  # noqa: N802
        # We need a profile for a spellbook, thus we need a django user
        user = User(email="email@email.com", password="password")
        user.save()

        cls.profile = Profile(user=user)
        cls.profile.save()

    def test_0_create_spellbook(self):
        """It should be possible to create a spellbook"""

        n_spellbooks = Spellbook.objects.count()

        spellbook = Spellbook(
            name="spellbook_name",
            profile=self.profile,
        )
        spellbook.save()

        self.assertEqual(
            Spellbook.objects.count(),
            n_spellbooks + 1,
        )
        self.assertTrue(bool(spellbook.token))  # Token should not be empty

        # A spellbook should have a spell slot level 1 by default
        self.assertEqual(
            spellbook.slots.count(),
            1,
        )
        self.assertEqual(
            spellbook.slot_level(1).max_capacity,
            2,
        )

    def test_1_add_spell(self):
        """It should be possible to add and remove a spell to a spellbook"""

        spell = Spell(
            name="spell_name",
            **TEST_SPELL_EXAMPLE_FIELDS,
        )
        spell.save()

        spellbook = Spellbook(
            name="spellbook_name",
            profile=self.profile,
        )
        spellbook.save()

        spell_usage = SpellUsage(
            spell=spell,
            spellbook=spellbook,
        )
        spell_usage.save()

        self.assertEqual(
            spellbook.spells.count(),
            1,
        )

        SpellUsage.objects.filter(spell=spell, spellbook=spellbook).delete()

        self.assertEqual(
            spellbook.spells.count(),
            0,
        )
