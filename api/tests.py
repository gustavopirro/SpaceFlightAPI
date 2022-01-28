from django.test import TestCase


# Create your tests here.
class APITestCase(TestCase):
    def test_hello_world(self):
        self.assertEquals(2 + 2, 4)
