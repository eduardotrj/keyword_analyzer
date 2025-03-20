from keybert import KeyBERT as KeyB
import re
import os


class Model:
    def __init__(self):
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
    
    
    
    def merge_files(self, list_files:dict):
        total_text = ""
        for text in list_files.values():
            total_text += text + ". "
   
        return total_text
        
                        
        

    def extract_keywords(self, text, num_keywords=50):
        """ Extract the most important keywords from the text.

        Args:
            text (_type_): int
            num_keywords (int, optional): Number of keywords extracted. Defaults to 20.

        Returns:
            _type_: List with keywords
        """
        keywords = self.scan_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words='english', top_n=num_keywords)
        
        return [(kw[0],) for kw in keywords]  # Returning as a tuple for table compatibility
    
    
    def count_words(self, words: tuple, text: str):
        words_in_text = re.findall(r'\b\w+\b', text.lower()) 
        
        word_counts = {
            word[0]: words_in_text.count(word[0])
            for word in words
            if words_in_text.count(word[0]) > 1
        }
        
        # word_counts = {}
        # for word in words:
        #     word = word[0]      # Get word from 
        #     times = words_in_text.count(word)
        #     if times > 1:       # Only takes repeated words
        #         word_counts[word] = times

        return word_counts
     
     
     
    def get_phrases(self, words: dict, text: str):
        sentences = re.split(r'(?<=[.!?])\s+', text.lower())
        
        keyword_sentences = { word: [sentence for sentence in sentences if word in sentence] for word in words.keys() }
             
        # keyword_sentences = {}                
        # for word in words.keys():
        #     print(word)
            
        #     keyword_sentences[word] = []
        #     for sentence in sentences:
                
        #         if word in sentence:
        #             keyword_sentences[word].append(sentence)

        return keyword_sentences
    
    
    def get_document(self, words: dict, files: dict):
        
        keywords_files = {}
        
        for word in words.keys():
            keywords_files[word] = []
            
            for file, text in files.items():
                if word in text.lower():
                    keywords_files[word].append(file)
                    
        return keywords_files
  
    
    
            
        
        

     
