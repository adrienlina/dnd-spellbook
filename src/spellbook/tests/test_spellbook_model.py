from django.contrib.auth import get_user_model
from django.test import TestCase

from profiles.models import Profile
from spellbook.models import Spellbook

User = get_user_model()


class SpellbookModelCase(TestCase):
    def test_0_create_spellbook(self):
        """It should be possible to create a spell"""

        # We need a profile for a spellbook, thus we need a django user
        user = User(email="email@email.com", password="password")
        user.save()

        profile = Profile(user=user)
        profile.save()

        n_spellbooks = Spellbook.objects.count()

        new_spell_book = Spellbook(
            name="spellbook_name",
            profile=profile,
        )

        new_spell_book.save()

        self.assertEqual(
            Spellbook.objects.count(),
            n_spellbooks + 1,
        )
