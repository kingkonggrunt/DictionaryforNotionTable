class PartsOfSpeech:
    """list of properties that can be associated with a word's definition whether the word can be a noun, verb, adverb ... etc"""
    
    @property
    def noun(self):
        return self._noun
    
    @noun.setter
    def noun(self, meanings):
        meaning = [meaning['definitions'] for meaning in meanings if meaning['partOfSpeech'] == 'noun']
        self._noun = meaning[0]
        
    @property
    def verb(self):
        return self._verb
    
    @verb.setter
    def verb(self, meanings):
        meaning = [meaning['definitions'] for meaning in meanings if meaning['partOfSpeech'] == 'verb']
        self._verb = meaning[0]
        
    @property
    def adjective(self):
        return self._adjective
    
    @adjective.setter
    def adjective(self, meanings):
        meaning = [meaning['definitions'] for meaning in meanings if meaning['partOfSpeech'] == 'adjective']
        self._adjective = meanings[0]