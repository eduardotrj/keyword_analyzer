import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from keybert import KeyBERT as KeyB

class TableView:
    """ Create a main window with 3 columns
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Keyword Analyzer")
        self.model = KeyB()
        self.create_widgets()
        
    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load Document", command = self.load_document)
        self.load_button.pack(pady=10)
        self.create_table()
        
    def create_table(self):
        """ Build a table with 3 columns inside by using Treeview class.
        """
        columns = ("Word (Total Occurrences)", "Documents", "Sentences containing the word")
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
            
        self.tree.pack(expand=True, fill='both')
        
        
    def populate_table(self, data):
        """insert information inside of the columns

        Args:
            data (_type_): _description_
        """
        self.tree.delete(*self.tree.get_children())  # Clear previous data
        for row in data:
            self.tree.insert("", tk.END, values=row)
            
            
    def load_document(self):
        """ Load any txt document
        """
        file_path = askopenfilename(defaultextension=".txt", filetypes=[("Text Documents","*.txt")]) 
        # file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                keywords = self.extract_keywords(text)
                self.populate_table(keywords)
    
    def extract_keywords(self, text, num_keywords=20):
        """ Extract the most important keywords from the text.

        Args:
            text (_type_): int
            num_keywords (int, optional): Number of keywords extracted. Defaults to 20.

        Returns:
            _type_: List with keywords
        """
        keywords = self.model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=num_keywords)
        return [(kw[0],) for kw in keywords]
            
            
if __name__ == "__main__":
    root = tk.Tk()
    app = TableView(root)
    root.mainloop()
    
    
    ##KeyBert
        