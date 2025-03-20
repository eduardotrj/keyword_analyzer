from keybert import KeyBERT as KeyB


class Model:
    def __init__(self):
        self.scan_model = KeyB()

    def extract_keywords(self, text, num_keywords=20):
        """ Extract the most important keywords from the text.

        Args:
            text (_type_): int
            num_keywords (int, optional): Number of keywords extracted. Defaults to 20.

        Returns:
            _type_: List with keywords
        """
        keywords = self.scan_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=num_keywords)
        return [(kw[0],) for kw in keywords]  # Returning as a tuple for table compatibility