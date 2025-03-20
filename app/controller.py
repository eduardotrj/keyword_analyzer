import tkinter as tk
from tkinter import filedialog
from app.model import Model
from app.view import View

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        
    def run(self):
        self.root.mainloop()
        

    def load_document(self):
        """ Load a text document. 
            Send the text to analyze with               Model.extract_keywords
            Get the results and send to print in        View.populate_table
        """
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                keywords = self.model.extract_keywords(text)
                self.view.populate_table(keywords)
                
                
    # Create a new funtion called from load document.
    # Function: call another model funtion to find the total number of keywords in a text.
    # Funtion: call another model funtion to get a list with each phrase with keylist.
    # Funtion: Send data to View.
    
    # Edit load_document to read all documents in a folder.


   
    
    
