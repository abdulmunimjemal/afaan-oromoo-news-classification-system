import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
import unittest
from preprocessing.special_character_handler import SpecialCharacterHandler
from preprocessing.stopword_remover import StopwordRemover
from preprocessing.stemmer import AfaanOromooStemmer
from preprocessing.tokenizer import AfaanOromooTokenizer
from preprocessing.preprocessing_pipeline import PreprocessingPipeline


class TestPreprocessingPipeline(unittest.TestCase):
    def setUp(self):
        self.tokenizer = AfaanOromooTokenizer()
        self.stopword_remover = StopwordRemover()
        self.stemmer = AfaanOromooStemmer()
        self.special_character_handler = SpecialCharacterHandler()
        self.preprocessing_pipeline = PreprocessingPipeline()
        self.test_string = "Akkam ooltan? nagaadhaa! re'een keessan na nyaatte!"

    def test_tokenizer(self):
        tokens = self.tokenizer.tokenize(self.test_string)
        self.assertEqual(
            tokens, ["akkam", "ooltan?", "nagaadhaa!", "reheen", "keessan", "na", "nyaatte!"])

    def test_special_character_handler(self):
        tokens = self.tokenizer.tokenize(self.test_string)
        tokens = self.special_character_handler.remove_special_characters(" ".join(tokens))
        self.assertEqual(
            tokens, " ".join(["akkam", "ooltan", "nagaadhaa", "reheen", "keessan", "na", "nyaatte"]))

    def test_stopword_remover(self):
        tokens = self.tokenizer.tokenize(self.test_string)
        tokens = self.special_character_handler.remove_special_characters(" ".join(tokens)).split()
        tokens = self.stopword_remover.remove_stopwords(tokens)
        
        self.assertEqual(
            tokens, ["akkam", "ooltan", "nagaadhaa", "reheen", "nyaatte"])

    def test_stemmer(self):
        tokens = self.tokenizer.tokenize(self.test_string)
        tokens = self.special_character_handler.remove_special_characters(" ".join(tokens)).split()
        tokens = self.stopword_remover.remove_stopwords(tokens)
        stemmed_tokens = [self.stemmer.stem(token) for token in tokens]
        self.assertEqual(
            stemmed_tokens, ["akkam", "oolt", "nagaa", "reh", "nyaat"])

    def test_preprocess(self):
        cleaned_text = self.preprocessing_pipeline.preprocess(self.test_string)
        self.assertEqual(
            cleaned_text, "akkam oolt nagaa reh nyaat")


if __name__ == "__main__":
    unittest.main()
