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

    """def test_add_with_post(self):
        value = "testing post"
        client = Client()
        response = client.post('/cms/key', {'value': value})
        if response.content not 
        self.assertEqual(response.status_code, 404)
        response = client.get('/cms/key')
        self.assertEqual(response.status_code, 404)
        content = response.content.decode('utf-8')
        self.assertIn(value, content)
        self.assertIn('asfag', content)"""


