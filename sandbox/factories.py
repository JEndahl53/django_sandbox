# sandbox/factories.py

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from core.models import Composer, Music

fake = Faker()

class ComposerFactory(DjangoModelFactory):
    class Meta:
        model = Composer

    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())

class MusicFactory(DjangoModelFactory):
    class Meta:
        model = Music

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=3))
    composer = factory.SubFactory(ComposerFactory)

