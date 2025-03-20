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
        
    def get_keyworkds(self):
        
        # text = self.load_document()
        files = self.load_documents()  # {'doc1.txt': 'Let me beg…
        
        text = self.model.merge_files(files)

        keywords = self.model.extract_keywords(text)
        
        keywords_number = self.model.count_words(keywords, text)
        
        keywords_files = self.model.get_document(keywords_number, files)
        
        keyword_sentences = self.model.get_phrases(keywords_number, text)
        
        
        self.view.populate_table(keywords_number, keywords_files, keyword_sentences)
                
        # print(keywords)
        # self.view.populate_table(keywords)
        
        
    def load_documents(self):
                
        documents_texts =[]
        
        folder_path = filedialog.askdirectory(title="Select a Folder")
        
        if folder_path:
            # print(f"Selected folder: {folder_path}")
            
            documents_texts = self.model.extract_text(folder_path)
            
            return documents_texts
            
        else:
            self.view.alert("Alert", "No folder was selected.")
            print("No folder was selected.")
        



    def load_document(self):
        """ Load a text document. 
            Send the text to analyze with               Model.extract_keywords
            Get the results and send to print in        View.populate_table
        """
        pass          

        # for txt in ('filter_path'):
        #     documents_texts.append( (open('txt')).read())
     
        # txt.append('txt(docum)', append=read.txt(_Documents_textss_,s) )
        
        
        
        
        # file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        # if file_path:
        #     with open(file_path, "r", encoding="utf-8") as file:
        #         text = file.read()
                
        #     if text:
        #         return text
            
        #     else:
        #         self.view.alert("Alert", "Not any text found in this document.")
        #         return "empty"
                
    
        
        
        
                
                
                
                
        
                
                
    # Create a new funtion called from load document.
    # Function: call another model funtion to find the total number of keywords in a text.
    # Funtion: call another model funtion to get a list with each phrase with keylist.
    # Funtion: Send data to View.
    
    # Edit load_document to read all documents in a folder.


   
    
    
