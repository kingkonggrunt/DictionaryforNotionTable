from distutils.command.build import build
import unittest

from src.notion import builders

class TestRichTextBuilder(unittest.TestCase):
    def test_patch(self):
        patch = builders.RichTextBuilder()
        patch.add_rich_text(text='I love pie')
        patch.add_rich_text(text='I love dank memes')
        
        expected = {'rich_text': [{'type': 'text', 'text': {'content': 'I love pie'}, 'annotations': {}}, {'type': 'text', 'text': {'content': 'I love dank memes'}, 'annotations': {}}]}
        assert patch.get_patch() == expected
