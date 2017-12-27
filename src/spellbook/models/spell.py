from django.db import models


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

    """The school the spell belongs to"""
    school = models.TextField(
        verbose_name="School",
        max_length=20,
    )

    """The duration of the spell"""
    duration = models.TextField(
        verbose_name="Spell Duration",
        max_length=50,
    )

    """Source page where the spell is listed"""
    page = models.CharField(
        verbose_name="Page (Source)",
        max_length=50,
    )

    """Whether the spell requires concentration"""
    concentration = models.BooleanField()

    """Whether the spell requires a ritual"""
    ritual = models.BooleanField()

    """
    Components required to cast the spell
    V = verbal, S = somatic (movement), M = material
    """
    components = models.CharField(
        verbose_name="Components",
        max_length=10,
    )

    """Material components needed, if any"""
    material_component = models.TextField(
        blank=True,
        default=""
    )

    @property
    def level_as_dnd_format(self):
        if self.level == 0:
            return "Cantrip"

        return "Level %s" % self.level

    def __repr__(self):
        return "<Spell %s>" % self.name

    def __str__(self):
        return "Spell %s" % self.name
