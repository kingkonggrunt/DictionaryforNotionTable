import requests

from .meaning import Meaning
from .exceptions import WordNotFoundError

class Dictionary:
    """Class object interface for the freeDictionaryAPI

    The API output of word is saved under the `definition` property.
    The `meanings` property contains only the meanings on the word from the definition.
    The `parts_of_speech` property lists whether the word is a 'noun', 'verb', 'adjective' etc.

    For each parts of speech meaning the word contains, the class dynamically assigns
    the meaning of the word to a property equal to the parts of speech. ie 'noun' to self.noun

    Example Usage:
    definition = Dictionary('Profligate')

    definition.parts_of_speech
    # ['noun', 'verb', 'adjective']

    definition.noun # TODO change this to list to reflect multi definition system
    # {'definition': 'An abandoned person; one openly and shamelessly vicious; a dissolute person.', 'synonyms': [], 'antonyms': []}

    definition.verb.synonyms
    # ['overcome']
    """

    def __init__(self, word: str):
        """

        :param str word: The API fetches the word from Wiktionary.org


        """
        self.word = word
        self.definition = self.word

        self.parts_of_speech = self.definition
        self.meanings = self.definition

        # noun, verb, adjective etc meanings are assigned to self.noun, self.verb, etc
        for part in self.parts_of_speech:
            setattr(self, part, self._find_part_meaning(part))

    def _find_part_meaning(self, partofspeech: str) -> Meaning:
        """Find the meaning for specific partofspeech and return a Meaning object for that meaning

        :param str partofspeech: noun, verb, adjective ... etc
        :return Meaning: See Meaning documentation. Returning a Meaning object allows for usage
        like `self.noun.definition`
        """
        for meaning in self.meanings:
            if meaning['partOfSpeech'] == partofspeech:
                return Meaning(meaning)

    @property
    def definition(self) -> dict:
        """Property. Returns the API output for the word
        In instances where the word has multiple etymologies, only the first one is taken

        :return dict: API output
        """
        return self._definition

    @definition.setter
    def definition(self, word):
        api = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        # the output of the api is an array containing a json object for each etymology of the word
        try:
            self._definition = requests.get(f"{api}{word}").json()[0]
        except Exception as exc:
            raise WordNotFoundError(word) from exc

    @property
    def meanings(self) -> list:
        """Returns all meanings for the word

        :return dict: meanings are further organised into dictionaries, one for each parts of speech
        """
        return self._meanings

    @meanings.setter
    def meanings(self, definition):
        self._meanings = definition['meanings']

    @property
    def parts_of_speech(self) -> list:
        """Returns parts of speech (or word classes) for the word

        :return list: eg ['noun', 'verb', 'adjective']
        """
        return self._parts_of_speech

    @parts_of_speech.setter
    def parts_of_speech(self, definition):
        self._parts_of_speech = [part['partOfSpeech'] for part in definition['meanings']]

    def __repr__(self):
        return f"Dictionary({self.word})"

    def __str__(self):
        return str(self.definition)
    