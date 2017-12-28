from django.db.utils import IntegrityError
from django.test import TestCase

from spellbook.models import Spell

TEST_SPELL_EXAMPLE_FIELDS = dict(
    level=0,
    cast_type="cast_type",
    spell_range="spell_range",
    description="description",
    school="school",
    duration="duration",
    page="page",
    concentration=False,
    ritual=False,
    components="components",
)


class SpellModelCase(TestCase):
    def test_0_create_spell(self):
        """It should be possible to create a spell"""
        spell = Spell(
            name="spell_name",
            **TEST_SPELL_EXAMPLE_FIELDS,
        )
        spell.save()

        self.assertEqual(Spell.objects.count(), 1)

    def test_1_unique_spell_names(self):
        """It should not be possible to create two spells with the same name"""
        spell_one = Spell(
            name="spell_name",
            **TEST_SPELL_EXAMPLE_FIELDS,
        )
        spell_one.save()

        with self.assertRaises(IntegrityError):
            spell_two = Spell(
                name="spell_name",
                **TEST_SPELL_EXAMPLE_FIELDS,
            )
            spell_two.save()
