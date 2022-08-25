import requests
import unittest

from tests import data

class StatusError(BaseException):
    def __init__(self, status_code: int, message="Status code is not 200"):
        self.status_code = status_code
        self.message = message
        super.__init__(self.message)
        
    def __str__(self) -> str:
        return f"{self.status_code} -> {self.message}"
        

class TestAPI(unittest.TestCase):
    def test_dictionary_response_unchanged(self):
        """This test tests if the saved expected output differs from the api's real output"""
        api = "https://api.dictionaryapi.dev/api/v2/entries/en"
        test_word = "oily"
        response = requests.get(f"{api}/oily")
        if response.status_code != 200:
            raise StatusError(response.status_code)
        # print(data.expected_oily_response)
        assert response.json() == data.expected_oily_response
        