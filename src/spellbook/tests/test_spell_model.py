from django.test import TestCase

from spellbook.models import Spell


class SpellModelCase(TestCase):
    def test_0_create_spell(self):
        """It should be possible to create a spell"""
        n_spells = Spell.objects.count()

        new_spell = Spell(
            name="spell_name",
            level=0,
            cast_type="cast_type",
            spell_range="spell_range",
            description="description",
        )

        new_spell.save()

        self.assertEqual(
            Spell.objects.count(),
            n_spells + 1,
        )
