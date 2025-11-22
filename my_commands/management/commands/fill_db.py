# my_commands/management/commands/fill_db.py

from django.core.management.base import BaseCommand
from random import choice

from sandbox.factories import ComposerFactory, MusicFactory


class Command(BaseCommand):
    help = "Populate database with demo composers and music pieces"

    def handle(self, *args, **kwargs):

        self.stdout.write('Creating 25 composers...')
        composers = ComposerFactory.create_batch(25)

        self.stdout.write('Creating 50 pieces of music...')
        for _ in range(50):
            MusicFactory.create(composer=choice(composers))

        self.stdout.write(self.style.SUCCESS("Database successfully populated."))