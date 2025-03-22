import unittest
from unittest.mock import MagicMock, patch
import datetime
from app.controller import Controller


class TestController(unittest.TestCase):

    def setUp(self):
        """Initialize a Controller instance before each test."""
        self.controller = Controller()
        self.controller.view = MagicMock()  # Mock the View
        self.controller.model = MagicMock()  # Mock the Model

    @patch("app.controller.filedialog.askdirectory")
    def test_load_documents_with_folder_selected(self, mock_askdirectory):
        """Test if load_documents correctly loads documents when a folder is selected."""
        mock_askdirectory.return_value = "/fake/path"
        self.controller.model.extract_text.return_value = {"file1.txt": "text content"}

        result = self.controller.load_documents()
        
        self.controller.model.extract_text.assert_called_once_with("/fake/path")
        self.assertEqual(result, {"file1.txt": "text content"})

    @patch("app.controller.filedialog.askdirectory")
    def test_load_documents_without_folder_selected(self, mock_askdirectory):
        """Test if load_documents handles no folder selection properly."""
        mock_askdirectory.return_value = ""

        result = self.controller.load_documents()
        
        self.controller.view.alert.assert_called_once_with("Alert", "No folder was selected.")
        self.assertIsNone(result)

    def test_merge_files(self):
        """Test merging multiple text files into a single string."""
        input_files = {"doc1.txt": "Hello", "doc2.txt": "World"}
        expected_output = "Hello. World. "

        result = self.controller.merge_files(input_files)
        
        self.assertEqual(result, expected_output)

    @patch("app.controller.datetime.datetime")
    def test_create_name(self, mock_datetime):
        """Test if create_name generates a correctly formatted filename."""
        mock_datetime.now.return_value = datetime.datetime(2025, 3, 22, 14, 30)
        expected_filename = "Keywords_analysis_2025-03-22_14-30.pdf"

        result = self.controller.create_name()
        
        self.assertEqual(result, expected_filename)

    @patch("app.controller.FPDF")
    def test_export_to_pdf(self, mock_fpdf):
        """Test exporting table data to a PDF."""
        mock_tree = MagicMock()
        self.controller.view.tree = mock_tree
        mock_fpdf_instance = mock_fpdf.return_value

        with patch.object(self.controller, "create_name", return_value="test.pdf"):
            self.controller.export_to_pdf()

        mock_fpdf_instance.add_page.assert_called_once()
        mock_fpdf_instance.output.assert_called_once_with("test.pdf")


if __name__ == "__main__":
    unittest.main()