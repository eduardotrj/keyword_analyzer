from keybert import KeyBERT as KeyB
import re
import os


""" 
✶ To use OpenAi LLM. ✶
"""
# import openai
# from keybert.llm import OpenAI
# from keybert import KeyLLM

# class IA_Config:
#     client = openai.OpenAI(api_key=MY_API_KEY)
#     llm = OpenAI(client)
#     kw_model = KeyLLM(llm)


class Model:
    
    """ Class to manage data.
    """
    def __init__(self):
        
        # Change for IA model.
        # self.scan_model = IA_Config.kw_model
        self.scan_model = KeyB()
        
        
    def extract_text(self, path):
        documents_texts = {}
        
        for filename in os.listdir(path):
                if filename.endswith(".txt"):  # Check for .txt files
                    
                    documents_texts[filename] = ""
                    
                    file_path = os.path.join(path, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        
                        documents_texts[filename] = file.read()  # Read the content of the file
                        
                        #print(f"\nContents of {filename}:\n{documents_texts[filename]}")
                        
        return documents_texts                        
    
    
    
    
        
                        
        

    def extract_keywords(self, text: str="", num_keywords: int=50):
        """ Extract the most important keywords from the text.

        Args:
            text (str): Text to analyze.
            num_keywords (int, optional): Number of keywords extracted. Defaults to 50.

        Returns:
            _type_: List with keywords
        """
        keywords = self.scan_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words='english', top_n=num_keywords)
        
        return [(kw[0],) for kw in keywords]  # Returning as a tuple for table compatibility
    
    
    def count_words(self, words: tuple, text: str):
        
        """
            Count how many times is a word in the text.
            
        Args:
            words (tuple): Keywords.
            text (str): Text to analyze.

        Returns:
            (dict): Dictionary {keywords (str): times (int)}.
        """
        words_in_text = re.findall(r'\b\w+\b', text.lower()) 
        
        # List comprehension  
        # word_counts = {
        #     word[0]: words_in_text.count(word[0])
        #     for word in words
        #     if words_in_text.count(word[0]) > 1
        # }
        
        word_counts = {}
        for word in words:
            word = word[0]      # Get word from 
            times = words_in_text.count(word)
            if times > 1:       # Only takes repeated words
                word_counts[word] = times

        return word_counts
     
     
     
    def get_phrases(self, words: dict, text: str):
        
        """ Extract all phrases where a keyword is.
        
        Args:
            words (dict): Keywords.
            text (str): Text to analyze.

        Returns:
            (dict): Dictionary {keywords (str): phrases (list with strings)}.
        """
        sentences = re.split(r'(?<=[.!?])\s+', text.lower())
              
        keyword_sentences = {}                
        for word in words.keys():
            
            keyword_sentences[word] = []
            for sentence in sentences:
                
                # To avoid get wrong sentences.
                pattern = r'\b' + word + r'\b'
                match = re.search(pattern, sentence)
                
                if match:
                    keyword_sentences[word].append(sentence.capitalize())

        return keyword_sentences
    
    
    def get_document(self, words: dict, files: dict):
        """_summary_

        Args:
            words (dict): Keywords
            files (dict): All documents to analyze.

        Returns:
            (dict): Dictionary {keywords (str): files (list with strings)}.
        """
        keywords_files = {}
        
        for word in words.keys():
            keywords_files[word] = []
            
            for file, text in files.items():
                if word in text.lower():
                    keywords_files[word].append(file.replace(".txt", ", "))
        
        # List comprehension:            
        # keywords_files = { word: [file.replace(".txt", ", ") for file, 
        #                           text in files.items() if word in text.lower()] 
        #                   for word in words.keys()
        # }
                    
        return keywords_files
  
    
    
        
    
        
            
        
        

     
