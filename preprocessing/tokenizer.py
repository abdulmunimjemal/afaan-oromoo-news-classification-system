import re
import unicodedata


def word_tokenize(text):
    # TODO: Buil a more powerful tokenizer with edge cases handler
    words = text.split()
    words = [word.strip() for word in words]
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
        text = text.replace(accent, normalized)
    normalized_text = unicodedata.normalize(
        'NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    return normalized_text
