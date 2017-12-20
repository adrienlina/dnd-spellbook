from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from spellbook.models import Spellbook

User = get_user_model()


class SpellbookDetailsAccessCase(TestCase):
    """
    A spellbook should only be accessible to its owner or through the use of its
    token
    """

    spellbook_detail_routes = [
        'spellbook:spellbook-detail',
        'spellbook:spellbook-add-spell',
        'spellbook:spellbook-remove-spell',
        'spellbook:spellbook-prepare-spell',
        'spellbook:spellbook-unprepare-spell',
    ]

    @classmethod
    def setUpTestData(cls):  # noqa: N802
        """Set up a user with a spellbook and another user"""
        # We need a profile for a spellbook, thus we need a django user
        cls.user1 = User.objects.create_user(
            email='test1@user.com',
            password='password',
        )

        cls.user2 = User.objects.create_user(
            email='test2@user.com',
            password='password',
        )

        cls.spellbook = Spellbook(
            name="spellbook_name",
            profile=cls.user1.profile,
        )
        cls.spellbook.save()

    def test_0_spellbook_no_access_anonymous(self):
        """
        It should not be possible to view the spellbook page if the user is
        anonymous
        """
        for route in self.spellbook_detail_routes:
            url = reverse(route, kwargs={'pk': self.spellbook.pk})
            r = self.client.get(url)
            self.assertEqual(r.status_code, 404)

    def test_1_spellbook_no_access_wrong_user(self):
        """
        It should not be possible to view the spellbook page if the user does
        not own the spellbook
        """
        self.client.login(username='test2@user.com', password='password')

        for route in self.spellbook_detail_routes:
            url = reverse(route, kwargs={'pk': self.spellbook.pk})
            r = self.client.get(url)
            self.assertEqual(r.status_code, 404)

    def test_2_spellbook_access_with_token(self):
        """
        It should be possible to view the spellbook page if the user has the
        appropriate token for that spellbook
        """
        for route in self.spellbook_detail_routes:
            url = reverse(route, kwargs={'pk': self.spellbook.pk})
            url += '?token=%s' % self.spellbook.token
            r = self.client.get(url, follow=True)
            self.assertEqual(r.status_code, 200)
