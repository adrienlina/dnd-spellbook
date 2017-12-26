from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from spellbook.models import Spellbook

User = get_user_model()


class SpellbookSlotViewsCase(TestCase):
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

        # Create a level 2 slot
        cls.spellbook.slots.create(level=2, max_capacity=1, current_capacity=1)

    def setUp(self):  # NOQA: N802
        """Log in as the user"""
        self.client.login(username='test@user.com', password='password')

    def test_0_edit_spell_slots(self):
        """It should be possible to edit the spell slots from the edit page"""
        url = reverse('spellbook:spellbook-edit-slots', kwargs={'pk': self.spellbook.pk})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

        data = {
            'spellbook_pk': self.spellbook.pk,
            'spell_slots_level_1': 3,
            'spell_slots_level_2': 2,
        }
        for level in range(3, 10):
            data['spell_slots_level_%s' % level] = 0

        r = self.client.post(url, data, follow=True)
        self.assertEqual(r.status_code, 200)

        # Spell slots should be updated
        self.assertEqual(self.spellbook.slot_level(1).max_capacity, 3)
        self.assertEqual(self.spellbook.slot_level(1).current_capacity, 3)
        self.assertEqual(self.spellbook.slot_level(2).max_capacity, 2)
        self.assertEqual(self.spellbook.slot_level(3).max_capacity, 0)
        self.assertEqual(self.spellbook.slots.count(), 9)

    def test_1_use_spell_slots(self):
        """It should be possible to use a spell slot"""
        # Use twice the same spell slot level
        url = reverse('spellbook:spellbook-use-slot', args=[self.spellbook.pk, 1])
        url = reverse('spellbook:spellbook-use-slot', args=[self.spellbook.pk, 1])
        r = self.client.get(url, follow=True)  # Once
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.slot_level(1).current_capacity, 1)

        r = self.client.get(url, follow=True)  # Twice
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.slot_level(1).current_capacity, 0)

        # And another slot level
        self.assertEqual(self.spellbook.slot_level(2).current_capacity, 1)
        url = reverse('spellbook:spellbook-use-slot', args=[self.spellbook.pk, 2])
        r = self.client.get(url, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.spellbook.slot_level(2).current_capacity, 0)

    def test_2_reset_spell_slots(self):
        """It should be possible to reset to the maximum a slot's capacity"""

        # Use two level 1 slots, one level 2 slot
        self.spellbook.slot_level(1).use_slot()
        self.spellbook.slot_level(1).use_slot()
        self.spellbook.slot_level(2).use_slot()
        self.assertEqual(self.spellbook.slot_level(1).current_capacity, 0)
        self.assertEqual(self.spellbook.slot_level(2).current_capacity, 0)
        # Reset level 1
        url = reverse('spellbook:spellbook-reset-slots', args=[self.spellbook.pk, 1])
        r = self.client.get(url, follow=True)
        self.assertEqual(r.status_code, 200)
        # Only level 1 should be reset
        self.assertEqual(self.spellbook.slot_level(1).current_capacity, 2)
        self.assertEqual(self.spellbook.slot_level(2).current_capacity, 0)

        # Use level 1 slot again
        self.spellbook.slot_level(1).use_slot()
        # Reset all slots
        url = reverse('spellbook:spellbook-reset-slots', args=[self.spellbook.pk])
        r = self.client.get(url, follow=True)
        self.assertEqual(r.status_code, 200)
        # All slots should be reset
        self.assertEqual(self.spellbook.slot_level(1).current_capacity, 2)
        self.assertEqual(self.spellbook.slot_level(2).current_capacity, 1)
