import tkinter as tk
from tkinter import filedialog
from app.model import Model
from app.view import View
from fpdf import FPDF
import datetime


class Controller:
    
    """ Manages interactions between model and view.
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        
        
    def run(self):
        self.root.mainloop()
        
        
    def get_keyworkds(self):
        """ 1. Read the documents. 
            2. Get Keywords, number, documents associate and the phrases.
            3. Sent to the view to fill the table with the information.
        """
        files = self.load_documents() 
        
        text = self.merge_files(files)
        keywords = self.model.extract_keywords(text)
        keywords_number = self.model.count_words(keywords, text)
        keywords_files = self.model.get_document(keywords_number, files)
        keyword_sentences = self.model.get_phrases(keywords_number, text)
        
        self.view.populate_table(keywords_number, keywords_files, keyword_sentences)

        
        
    def load_documents(self):
        documents_texts =[]
        folder_path = filedialog.askdirectory(title="Select a Folder")
        
        # Check if the folder path exist.
        if folder_path:
            # print(f"Selected folder: {folder_path}")
            documents_texts = self.model.extract_text(folder_path)
            return documents_texts
        
        # Generate an alert if not path have been selected. 
        else:
            self.view.alert("Alert", "No folder was selected.")
            print("No folder was selected.")
        

    def export_to_pdf(self):
        self.model.export_to_pdf(self.view.tree)
        
        
    def export_to_pdf(self):
        tree = self.view.tree
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=6)

        # Add a title to the PDF
        pdf.cell(200, 10, txt="List of Keywords", ln=True, align='C')

        # Add a header row
        pdf.cell(40, 10, txt="Word (Total Occurrences)", border=1, align='C')
        pdf.cell(30, 10, txt="Documents", border=1, align='C')
        pdf.cell(120, 10, txt="Sentences containing the word", border=1, align='C')
        pdf.ln() 

        # Iterate through Treeview rows and add to PDF
        for child in tree.get_children():
            values = tree.item(child, "values")
            
            
            pdf.cell(40, 10, txt=str(values[0].encode('utf-8')), border=1, align='C')  # Name
            pdf.cell(30, 10, txt=str(values[1].encode('utf-8')), border=1, align='C')  # Age
            pdf.cell(120, 10, txt=str(values[2].encode('utf-8')), border=1, align='C')  # City
            pdf.ln()  # Move to the next line
            
        name_file = self.create_name()

        # Save the PDF to a file
        pdf.output(name_file)
        print("PDF exported successfully!")
        
        
        
    def merge_files(self, list_files:dict):
        # Unifies all the texts of the documents into a single one
        total_text = ""
        for text in list_files.values():
            total_text += text + ". "
   
        return total_text
    
    
    def create_name(self):
        # Create a unique name using the current time.
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M")
        filename = f"Keywords_analysis_{formatted_time}.pdf"
        return filename


    # def load_document(self):
    #     """ Load a text document. 
    #         Send the text to analyze with               Model.extract_keywords
    #         Get the results and send to print in        View.populate_table
    #     """
    #     pass          

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


   
    
    
