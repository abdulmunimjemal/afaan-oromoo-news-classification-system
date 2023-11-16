from .tokenizer import AfaanOromooTokenizer
from .stopword_remover import StopwordRemover
from .stemmer import AfaanOromooStemmer
from .special_character_handler import SpecialCharacterHandler


class PreprocessingPipeline:
    """
    Afaan Oromoo Text Preprocessing Pipeline

    This class integrates the application of varios preprocessing steps on Afaan Oromoo text,

    Methods:
        - preprocess(text): Applies the preprocessing steps to the input text.

    Example:
     >>> pipeline = PreprocessingPipeline()
     >>> preprocessed_text = pipeline.preprocess("Garaan mataa caalti.")
     >>> print(preprocessed_text)
     "garaa mataa caal"
    """

    def __init__(self, stopwords=None):
        """
        Initialize the PreprocessingPipeline

        Parameters:
         - stopwrods (set)L A set of stop words. If not provided, default stopwords will be used.
        """
        self.tokenizer = AfaanOromooTokenizer()
        self.stopword_remover = StopwordRemover(stopwords)
        self.stemmer = AfaanOromooStemmer()
        self.special_char_handler = SpecialCharacterHandler()

    def preprocess(self, text: str) -> str:
        """
        Apply the preprocessing steps to the input text.

        Parameters:
         - text (str): The input text to be prepocessed

        Returns:
         - str: The preprocessed text.
        """
        # Step 1: Tokenize
        tokens = self.tokenizer.tokenize(text)

        # Step 2: Replace special character
        cleaned_text = self.special_char_handler.replace_special_characters(
            " ".join(tokens), " ")

        # Step 3: Remove stopwrods
        tokens_without_stopwords = self.stopword_remover.remove_stopwords(
            cleaned_text.split())

        # Step 4:
        stemmed_tokens = [self.stemmer.stem(token)
                          for token in tokens_without_stopwords]

        # Step 5: Join back and return
        preprocessed_text = " ".join(stemmed_tokens)

        return preprocessed_text
