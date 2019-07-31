import unittest
from sentence import Sentence

class SentenceGeneratorTestCase(unittest.TestCase):
    def test_sentence_generator(self):
        random_sentence = Sentence()
        self.assertEqual(random_sentence.generate(), ("Colorless green ideas sleep furiously"))
