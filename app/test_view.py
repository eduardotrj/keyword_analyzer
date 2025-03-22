import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from view import View


class TestView(unittest.TestCase):

    def setUp(self):
        """Initialize a View instance with a mocked controller."""
        self.root = tk.Tk()
        self.root.withdraw()  # Prevents window from actually appearing
        self.mock_controller = MagicMock()
        self.view = View(self.root, self.mock_controller)

    def test_widgets_created(self):
        """Check if the main widgets are created."""
        self.assertIsInstance(self.view.load_button, tk.Button)
        self.assertIsInstance(self.view.print_button, tk.Button)
        self.assertIsInstance(self.view.tree, tk.ttk.Treeview)

    def test_button_commands(self):
        """Ensure buttons call the correct controller methods."""
        self.view.load_button.invoke()
        self.mock_controller.get_keyworkds.assert_called_once()

        self.view.print_button.invoke()
        self.mock_controller.export_to_pdf.assert_called_once()

    def test_table_creation(self):
        """Check if the table has the expected columns."""
        expected_columns = (
            "Word (Total Occurrences)",
            "Documents",
            "Sentences containing the word"
        )
        self.assertEqual(self.view.tree["columns"], expected_columns)
        for col in expected_columns:
            self.assertEqual(self.view.tree.heading(col)["text"], col)

    def test_populate_table(self):
        """Test that populate_table correctly inserts data into the treeview."""
        keywords = {"python": 2, "test": 3}
        files = {"python": ["file1.txt"], "test": ["file2.txt"]}
        sentences = {"python": ["Sentence with many important Keywords."], "test": ["Another testing string."]}

        self.view.populate_table(keywords, files, sentences)

        children = self.view.tree.get_children()
        self.assertEqual(len(children), 5)  # 2 keywords + 1 sentence each + separator

        first_row = self.view.tree.item(children[0])["values"]
        self.assertEqual(first_row, ["python (2)", "file1.txt", ""])

        second_row = self.view.tree.item(children[1])["values"]
        self.assertEqual(second_row, ["", "", "Python is great."])

    @patch("app.view.MessageBox.showinfo")
    def test_alert(self, mock_messagebox):
        """Test alert method calls messagebox with correct arguments."""
        self.view.alert("Warning", "Test message")
        mock_messagebox.assert_called_once_with("Warning", "Test message")


if __name__ == "__main__":
    unittest.main()