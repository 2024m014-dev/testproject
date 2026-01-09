from django.test import TestCase
from django.contrib.auth.models import User
from .models import Action, GachaResult


class ActionModelTest(TestCase):
    def test_str_representation(self):
        user = User.objects.create_user(username="testuser", password="password")

        action = Action.objects.create(user=user, content="今日も大学行った")

        self.assertEqual(str(action), "今日も大学行った")


class GachaResultModelTest(TestCase):
    def test_str_representation(self):
        user = User.objects.create_user(username="testuser", password="password")

        result = GachaResult.objects.create(user=user, result_text="めちゃくちゃえらい")

        self.assertEqual(str(result), "めちゃくちゃえらい")
