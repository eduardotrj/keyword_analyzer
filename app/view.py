import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox as MessageBox


class View:
    """ Create a main window with 3 columns
    """
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Keyword Analyzer")
        self.controller = controller
        
        
        self.create_widgets()
        self.size()
        
        
    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load Document", command = self.controller.get_keyworkds)
        self.load_button.pack(pady=10)
        self.create_table()
        
    def size(self):
        """ Set the window size and position
        
        """
       
        #Calculate the center of the window.
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        window_width = screen_width/2
        window_height = screen_height/2
        
        left = (screen_width / 2) - (window_width / 2)
        top = (screen_height / 2) - (window_height / 2)
        self.root.geometry('%dx%d+%d+%d' % (
            window_width, window_height,left, top
            )) 
        
        
        
        
    def create_table(self):
        """ Build a table with 3 columns inside by using Treeview class.
        """
        
        columns = ("Word (Total Occurrences)", "Documents", "Sentences containing the word")
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
            
        self.tree.pack(expand=True, fill='both')
        
        
    # def populate_table(self, data):
    #     """insert information inside of the columns

    #     Args:
    #         data (_type_): _description_
    #     """
        
    #     self.tree.delete(*self.tree.get_children())  # Clear previous data
    #     for row in data:
    #         self.tree.insert("", tk.END, values=row)
            
            
    def populate_table(self, keywords:dict, files: dict, senteces: dict):
        """insert information inside of the columns

        Args:
            data (_type_): _description_
        """
        
        self.tree.delete(*self.tree.get_children())  # Clear previous data
        # for row in data:
        #     self.tree.insert("", tk.END, values=row)
            
            
    
        
   
        for keyword, number in keywords.items():
            
            keyword_numbers = keyword + " (" + str(number) + ")"
            
            documents = files[keyword]
            
            sentences = senteces[keyword]
            
                
            self.tree.insert("", tk.END, values=(keyword_numbers, documents, sentences))    
                
                
                
                
      
            
    def alert(self, title, message):
        MessageBox.showinfo(title, message)
            
            
   
