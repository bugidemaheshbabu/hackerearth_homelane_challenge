from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import StateWiseTesting
from datetime import datetime
# Create your tests here.
print("Running tests")



class TestStateWiseTesting(TestCase):
    def setUp(self):
        StateWiseTesting.objects.create(
            date=datetime.today(),
            state_name="Andra Pradesh",
            total_samples=0,
            negatives=0,
            positives=0
        )
        StateWiseTesting.objects.create(
            date=datetime.today(),
            state_name="Kerala",
            total_samples=0,
            negatives=0,
            positives=0
        )

    def test_state_names(self):
        state_1 = StateWiseTesting.objects.get(name="Andra Pradesh")
        state_2 = StateWiseTesting.objects.get(name="Kerala")

        self.assertEqual(state_1.name, 'Andra Pradesh')
        self.assertEqual(state_2.name, 'Kerala')