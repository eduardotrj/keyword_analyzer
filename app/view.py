import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox as MessageBox


class View:
    """ To handle UI components.
    """
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Keyword Analyzer")
        self.controller = controller
        
        
        self.create_widgets()
        self.size()
        
        
    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load Document", command = self.controller.get_keyworkds)
        self.print_button = tk.Button(self.root, text="Create PDF", command = self.controller.export_to_pdf)
        self.load_button.pack(pady=10)
        self.print_button.pack(pady=10)
        self.create_table()
        
    def size(self):
        """ Set the window size and position
        """
       
        # Calculate the center of the window.
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate the window size
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
        style = ttk.Style()
        style.configure("Treeview", rowheight=int(26))
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="w")
            
        self.tree.pack(expand=True, fill='both')

            
            
    def populate_table(self, keywords:dict, files: dict, sentence_list: dict):
        """ Insert information inside of the columns

        Args:
            keywords (dict): {keywords (str): times (int)}.
            files (dict): {keywords (str): files (list with strings)}
            sentence_list (dict): {keywords (str): phrases (list with strings)}.
        """
        self.tree.tag_configure('separate_line', background= "#B0E8EF")
        self.tree.delete(*self.tree.get_children())  # Clear previous data

   
        for keyword, number in keywords.items():
            keyword_numbers = keyword + " (" + str(number) + ")"
            # documents = files[keyword]
            documents = " ".join(str(file) for file in files[keyword]) 
            # sentences = senteces[keyword]
            self.tree.insert("", tk.END, values=(keyword_numbers, documents, "")) #, tags=('custom_height',)
            
            for sentence in sentence_list[keyword]:
                self.tree.insert("", tk.END, values=("", "", sentence))
                
            self.tree.insert("", tk.END, values=("","", ""), tags=('separate_line',) )
            
                
                
      
            
    def alert(self, title, message):
        MessageBox.showinfo(title, message)
            
            
   
