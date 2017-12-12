from django.db import models

from profiles.models import Profile


class Spellbook(models.Model):
    """A spellbook of a character"""

    """Spellbook name"""
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
