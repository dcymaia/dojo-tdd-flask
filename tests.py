import unittest
from app import meu_web_app


class TestHome(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        self.assertIn('Danilo Cyrino Maia', self.response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()