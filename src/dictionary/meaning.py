class Meaning:
    """Meaning object interface for different meanings of a word.
    See Dictionary class docstring to see how this class dynamically assigns different
    meanings to a Meaning object
    """
    def __init__(self, meaning: dict):
        self.meaning = meaning

        # components of the api output are arrays containing single json objects
        self.part_of_speech = self.meaning['partOfSpeech']
        self.definition = self.meaning['definitions'][0]
        self.synonyms = self.meaning['synonyms']
        self.antonyms = self.meaning['antonyms']
        self.example = self.meaning.get('example')

    def __repr__(self):
        return f"Meaning({self.meaning})"

    def __str__(self):
        return str(self.definition)
