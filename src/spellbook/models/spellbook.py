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

        return spells_with_preparations


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
