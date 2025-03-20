import tkinter as tk
from tkinter import ttk

class TableView:
    """ Create a main window with 3 columns
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Keyword Analyzer")
        self.create_table()
        
    def create_table(self):
        """ Build a table with 3 columns inside by using Treeview class.
        """
        columns = ("Word (Total Occurrences)", "Documents", "Sentences conaining the word")
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
        for row in data:
            self.tree.insert("", tk.END, values=row)
            
            
if __name__ == "__main__":
    root = tk.Tk()
    app = TableView(root)
    root.mainloop()
    
    
    ##KeyBert
        