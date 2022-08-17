import requests
from .partsofspeech import PartsOfSpeech


class Dictionary(PartsOfSpeech):
    """An interface for api.dictionaryapi.dev"""
    
    def __init__(self, word):
        self.definition = word
        self.meanings = self.definition
        self.parts_of_speech = self.definition
        
        # Make sure a property exists in partsofspeech.py for all parts 
        for parts in self.parts_of_speech:
            setattr(self, parts, self.meanings)
            
    @property
    def definition(self):
        return self._definition
    
    @definition.setter
    def definition(self, word):
        api = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        self._definition = requests.get(f"{api}{word}").json()
        
    @property
    def meanings(self):
        return self._meanings
    
    @meanings.setter
    def meanings(self, definition):
        self._meanings = self.definition[0]['meanings']
    
    @property
    def parts_of_speech(self):
        return self._parts_of_speech
    
    @parts_of_speech.setter
    def parts_of_speech(self, definition):
        self._parts_of_speech = [part['partOfSpeech'] for part in definition[0]['meanings']]
        
        
    