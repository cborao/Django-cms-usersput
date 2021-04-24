from django.test import TestCase
from django.test import Client

# Create your tests here.


class GetTests (TestCase):

    def test_root(self):
        client = Client()
        response = client.get('/cms/')
        self.assertEqual(response.status_code, 200)

        content = response.content.decode('utf-8')
        self.assertIn('You are in the root page.', content)


