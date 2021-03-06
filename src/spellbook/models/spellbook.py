from django.db import models

from profiles.models import Profile
from tools.random_token import generate_random_token

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

    """Token that gives access to the spellbook, independently to the profile"""
    token = models.CharField(max_length=32, default=generate_random_token)

    @property
    def n_spells(self):
        """Returns the number of spells contained in the spellbook"""
        return self.spells.count()

    def has_spell_prepared(self, spell):
        """Checks if a spell is prepared for that spellbook"""
        spell_usage = self.spell_usages.get(spell=spell, spellbook=self)

        return spell_usage.prepared

    @property
    def spells_with_preparations(self):
        """Constructs a list of spells and adds is_prepared to each one"""
        spells_with_preparations = []

        for spell in self.spells.all():
            spell.is_prepared = self.has_spell_prepared(spell)
            spells_with_preparations.append(spell)

        return sorted(spells_with_preparations, key=lambda spell: ~spell.is_prepared)

    def slot_level(self, level):
        """Return the spell slot of a given level"""
        try:
            return self.slots.get(level=level)
        except models.ObjectDoesNotExist:
            return None

    def reset_slots(self):
        """Reset all available slots capacity to their maximum"""
        self.slots.all().update(current_capacity=models.F('max_capacity'))


class SpellUsage(models.Model):
    """Link between a spell and a spellbook that defines if it is prepared"""

    """The spell of the connection"""
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE, related_name='spell_usages')

    """The spellbook of the connection"""
    spellbook = models.ForeignKey(Spellbook, on_delete=models.CASCADE, related_name='spell_usages')

    """Whether the spell is prepared or not"""
    prepared = models.BooleanField(default=False)

    class Meta:
        unique_together = [
            ('spell', 'spellbook'),  # A spellbook can only have a spell once
        ]
