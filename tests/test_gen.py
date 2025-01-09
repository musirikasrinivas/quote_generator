import unittest
from unittest.mock import patch, MagicMock
from quote_gen import QuoteGenerator

class TestQuoteGenerator(unittest.TestCase):
    def setUp(self):
        self.api_key = "test-api-key"
        self.generator = QuoteGenerator(api_key=self.api_key)

    def test_initialization(self):
        self.assertIsNotNone(self.generator)
        self.assertEqual(self.generator.api_key, self.api_key)
        self.assertIsNotNone(self.generator.themes)

    def test_add_theme(self):
        initial_count = len(self.generator.themes)
        self.generator.add_theme("wisdom")
        self.assertEqual(len(self.generator.themes), initial_count + 1)
        self.assertIn("wisdom", self.generator.themes)

    def test_remove_theme(self):
        self.generator.add_theme("test_theme")
        initial_count = len(self.generator.themes)
        self.generator.remove_theme("test_theme")
        self.assertEqual(len(self.generator.themes), initial_count - 1)
        self.assertNotIn("test_theme", self.generator.themes)

    def test_list_themes(self):
        themes = self.generator.list_themes()
        self.assertIsInstance(themes, list)
        self.assertTrue(len(themes) > 0)

    @patch('anthropic.Anthropic')
    def test_generate_quote(self, mock_anthropic):
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Test quote")]
        mock_anthropic.return_value.messages.create.return_value = mock_response

        quote = self.generator.generate_quote(theme="test")
        self.assertEqual(quote, "Test quote")

if __name__ == '__main__':
    unittest.main()