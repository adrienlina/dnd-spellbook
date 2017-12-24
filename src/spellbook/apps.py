from django.apps import AppConfig


class SpellbookConfig(AppConfig):
    name = 'spellbook'
    verbose_name = 'Spellbook'

    def ready(self):
        import spellbook.signals  # NOQA
