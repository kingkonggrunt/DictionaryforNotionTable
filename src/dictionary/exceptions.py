"""Class of Exceptions for the dictionary module"""

class WordNotFoundError(BaseException):
    """Word cannot be found in the DictionaryAPI (Wiktionary)"""
    def __init__(self, word, message="Word not found in dictionary"):
        self.word = word
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.word} - > {self.message}"
