# keyword_analyzer
Simple tool to read the most frequent used words in documents.


Keybert library is used (thanks to Maarten Grootendorst), which allow to read the most common words. While it can allow working with Large Language Models AI, the example can be used with Embedding Models or LLM.

This library allows to choose a number of Keywords to find in a document. By applying  some more code it was possible to find times per phrase, the documents where they are, and the phrases where are used. 

Initially, the number of keywords was limited to 50 in order to reduce the number of those that were used several times throughout the different documents.

Have been built an interface to show how the code, while the limitations of Tkinter Tree, don't allow to increase in the height of each row.

I added an export to PDF, but it was not time enough to improve the exit document because in order to reduce the time, was limited to getting the information directly from Tkinder elements.

