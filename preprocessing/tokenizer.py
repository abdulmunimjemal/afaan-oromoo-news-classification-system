import re
import unicodedata


def word_tokenize(text):
    # TODO: Build a more powerful tokenizer with edge cases handler
    words = text.split()
    words = [word.strip().lower() for word in words]
    return words


def sentence_tokenize(text):
    sentences = re.split(r'\.', text)
    sentences = [sentence.strip() for sentence in sentences]
    return sentences


def tokenize_with_punctuation(text):
    tokens = re.findall(r'\b\w+\b|\S', text)
    return tokens


def normalize(text):
    # Handle accents and variations
    # TODO: Add More replacements later
    replacements = {"kh": "k", "’": "h"}
    for original, normalized in replacements.items():
        text = text.replace(original, normalized)
    text = re.sub(r"\b'\b", "h", text)
    normalized_text = unicodedata.normalize(
        'NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    return normalized_text


class AfaanOromooTokenizer:
    """
    Afaan Oromoo tokenizer

    Usage:
        >>> tokenizer = AfaanOromooTokenizer()
        >>> tokenizer.word_tokenize("Akkam Akkam")
    """

    def __init__(self):
        pass

    def tokenize(self, text):
        text = normalize(text)
        return word_tokenize(text)
