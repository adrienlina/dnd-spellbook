from django.db import models

from .spellbook import Spellbook

AVAILABLE_SLOTS_LEVELS = range(1, 10)


class SpellSlotsLevel(models.Model):
    """
    Information about the spell slots attached to the usage of a spellbook and
    of a given spell level
    """

    """Spellbook attached to the slots"""
    spellbook = models.ForeignKey(Spellbook, on_delete=models.CASCADE, related_name="slots")

    """Level of the spell slots"""
    level = models.SmallIntegerField(verbose_name='Level')

    """Current number of spells still available to be used"""
    current_capacity = models.PositiveIntegerField(
        verbose_name="Current capacity",
        null=True,
        default=0
    )

    """Maximum number of spells available to be used when character has had a long rest"""
    max_capacity = models.PositiveIntegerField(
        verbose_name="Maximum capacity",
        null=True,
        default=0
    )

    class Meta:
        unique_together = [
            # A spellbook can only have one spell slots level of each level
            ('spellbook', 'level'),
        ]
