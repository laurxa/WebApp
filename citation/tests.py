from django.test import TestCase
from django.contrib.auth.models import User

from .models import Citation


class CitationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user')
        self.c1 = Citation.objects.create(title='cit 1', user=self.user)

    def test_citation_slug_generated(self):
        """On create the slug should be created based on the title."""
        self.assertEqual(self.c1.slug, 'cit-1')

    def test_slugs_per_user_are_unique(self):
        """Slugs per user must be unique."""
        c3 = Citation.objects.create(title='cit 1', user=self.user)
        self.assertNotEqual(self.c1.slug, c3.slug)
