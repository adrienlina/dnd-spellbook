from django.db import models

from profiles.models import Profile

from .spell import Spell


class Spellbook(models.Model):
    """A spellbook of a character"""

    """Spellbook name"""
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
    )

    """Profile of the user that owns the spellbook"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)

    """Spells present in the spellbook"""
    spells = models.ManyToManyField(Spell, through='SpellUsage')


class SpellUsage(models.Model):
    """Link between a spell and a spellbook that defines if it is prepared"""

    """The spell of the connection"""
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)

    """The spellbook of the connection"""
    spellbook = models.ForeignKey(Spellbook, on_delete=models.CASCADE)

    """Whether the spell is prepared or not"""
    prepared = models.BooleanField(default=False)
