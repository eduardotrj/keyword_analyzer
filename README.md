# keyword_analyzer
Simple tool to read the most frequent used words in documents.




Keybert library is used, which allow to read the most common words. While it can allow to work with Large Language Models AI,
for this example is going to use a simple model, to avoid constraints such as the absence of "AVX-512"


This library allows to choose a number of Keywords to find in a document, 
but unfortunately doesn't allow to count the number of position of them, which requires a extra code after found the main list
of keywords.

To be able to find the different keywords along all the documents, is goint to use a number of 10 per document and after add all together
showing all repeated ones as in different documents.

