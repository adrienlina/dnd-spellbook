from django.db.models.signals import post_save
from django.dispatch import receiver

from spellbook.models import DEFAULT_SLOTS, Spellbook


@receiver(post_save, sender=Spellbook)
def create_default_spell_slots(sender, instance, created, **kwargs):
    if created:
        for spell_slot_infos in DEFAULT_SLOTS:
            instance.slots.create(**spell_slot_infos)
