from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Roster

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', email='test@gmail.com', password='pass')
        testuser1.save()

        test_roster = Roster.objects.create(
            name = 'Test Player',
            position = 'QB',
            depth = '1',
            coach = testuser1,
        )
        test_roster.save()

    def test_roster_content(self):
        roster = Roster.objects.get(id=1)
        actual_name = str(roster.name)
        actual_position = str(roster.position)
        actual_depth = str(roster.depth)

        self.assertEqual(actual_name, 'Test Player')
        self.assertEqual(actual_position, 'QB')
        self.assertEqual(actual_depth, '1')
