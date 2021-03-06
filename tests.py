import unittest
from app import meu_web_app


class TestHome(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/dcymaia')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<title>Danilo Cyrino Maia</title>', str(response_str))
        self.assertIn('<h1>Danilo Cyrino Maia</h1>', str(response_str))
        self.assertIn('<p>Mineiro, ', str(response_str))

    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)

    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="https://github.com/dcymaia"', response_str)
        self.assertIn('>my github</a>', response_str)

if __name__ == '__main__':
    unittest.main()