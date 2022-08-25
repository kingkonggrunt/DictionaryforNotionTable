import unittest

from tests import data
from src import dictionary

class TestDictionary(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:  # TODO response exception
        self.word = dictionary.Dictionary(word="oily")

    @classmethod
    def tearDownClass(self) -> None:
        pass

    def test_property_parts_of_speech(self) -> bool:
        assert self.word.parts_of_speech == ['noun', 'adjective']
  
    def test_property_definition(self) -> bool:
        assert self.word.definition == data.expected_oily_response[0]
    
    def test_property_meanings(self) -> bool:
        print(self.word.meanings)
        assert self.word.meanings == data.expected_oily_response[0]['meanings']


class TestMeanings(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:  # TODO response exception
        self.word = dictionary.Dictionary(word="oily")
        
    @classmethod
    def tearDownClass(self) -> None:
        pass
    
    def test_property_noun(self) -> bool:
        assert isinstance(self.word.noun.meaning, dict)
        assert isinstance(self.word.noun.part_of_speech, str)
        assert isinstance(self.word.noun.definition, list)
        assert isinstance(self.word.noun.synonyms, list)
        assert isinstance(self.word.noun.antonyms, list)
        assert isinstance(self.word.noun.example, (str, type(None)))
