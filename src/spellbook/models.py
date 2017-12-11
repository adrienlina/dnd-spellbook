from django.db import models


# Create your models here.
class Spell(models.Model):
    """A unique spell as explained in the D&D Player's Handbook"""

    """Spell Name"""
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        unique=True,
    )

    """The level of the spell (0 = cantrip)"""
    level = models.IntegerField(
        verbose_name="Level",
    )

    """Cast type"""
    cast_type = models.CharField(
        verbose_name="Cast type",
        max_length=50,
    )

    """Spell range"""
    spell_range = models.CharField(
        verbose_name="Spell Range",
        max_length=50,
    )

    """Description"""
    description = models.TextField(
        verbose_name="Description",
    )
