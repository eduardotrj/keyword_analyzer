import unittest
from unittest.mock import MagicMock, patch, mock_open
from app.model import Model


class TestModel(unittest.TestCase):

    def setUp(self):
        """Initialize a Model instance before each test."""
        self.model = Model()
        self.model.scan_model.extract_keywords = MagicMock()

    @patch("app.model.os.listdir")
    @patch("builtins.open", new_callable=mock_open, read_data="Sample text content.")
    def test_extract_text(self, mock_open_func, mock_listdir):
        """Test extract_text reads files correctly."""
        mock_listdir.return_value = ["file1.txt", "file2.txt"]

        result = self.model.extract_text("/fake/path")

        expected_result = {
            "file1.txt": "Sample text content.",
            "file2.txt": "Sample text content."
        }
        
        self.assertEqual(result, expected_result)
        mock_open_func.assert_called_with("/fake/path/file2.txt", 'r', encoding='utf-8')

    def test_extract_keywords(self):
        """Test extract_keywords returns keywords correctly."""
        self.model.scan_model.extract_keywords.return_value = [("python", 0.8), ("testing", 0.6)]

        result = self.model.extract_keywords("Python testing is useful.")

        expected_result = [("python",), ("testing",)]
        self.assertEqual(result, expected_result)
        self.model.scan_model.extract_keywords.assert_called_once()

    def test_count_words(self):
        """Test count_words correctly counts word occurrences."""
        words = [("python",), ("test",)]
        text = "Python are importants. Sentence with many important Keywords. Test is important."

        result = self.model.count_words(words, text)

        expected_result = {"python": 2, "test": 2}
        self.assertEqual(result, expected_result)

    def test_get_phrases(self):
        """Test get_phrases extracts sentences containing keywords."""
        words = {"python": 2, "test": 3}
        text = "Python are importants. Sentence with many important Keywords. Test is important."

        result = self.model.get_phrases(words, text)

        expected_result = {
            "keywords": ["Sentence with many important Keywords.", "Keywords are important to manage information."],
            "test": ["Python is used in test cases.", "Test is important."]
        }
        self.assertEqual(result, expected_result)

    def test_get_document(self):
        """Test get_document finds which files contain keywords."""
        words = {"python": 2, "test": 3}
        files = {
            "file1.txt": "Sentence with many important Keywords.",
            "file2.txt": "Test is necessary."
        }

        result = self.model.get_document(words, files)

        expected_result = {
            "python": ["file1, "],
            "test": ["file1, ", "file2, "]
        }
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()