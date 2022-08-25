class Meaning:
    """Meaning object interface for different meanings (parts of speech) of a word.
    See Dictionary class docstring to see how this class dynamically assigns different
    meanings to a Meaning object
    """
    def __init__(self, meaning: dict):
        self._meaning = meaning

        # components of the api output are arrays containing single json objects
        self._part_of_speech = self._meaning['partOfSpeech']
        self._definition = self._meaning['definitions']
        self._synonyms = self._meaning['synonyms']
        self._antonyms = self._meaning['antonyms']
        self._example = self._meaning.get('example')

    def __repr__(self):
        return f"Meaning({self._meaning})"

    def __str__(self):
        return str(self._definition)

    @property
    def meaning(self) -> dict:
        return self._meaning

    @property
    def part_of_speech(self) -> str:
        return self._part_of_speech

    @property
    def definition(self) -> list:
        return self._definition

    @property
    def synonyms(self) -> list:
        return self._synonyms

    @property
    def antonyms(self) -> list:
        return self._antonyms

    @property
    def example(self) -> str:
        return self._example
