import re


class SpecialCharacterHandler:
    """
    Afaan Oromoo Special Character Handler

    This class provides methods for handling special characters in Afaan Oromoo text.

    Methods:
    - remove_special_characters(text): Removes special characters from the input text.
    - replace_special_characters(text, replacement=''): Replaces special characters with the specified replacement.

    Example:
    >>> handler = SpecialCharacterHandler()
    >>> cleaned_text = handler.remove_special_characters("Hello, Afaan Oromoo!")
    >>> print(cleaned_text)
    "Hello Afaan Oromoo"
    """

    def remove_special_characters(self, text):
        """
        Remove special characters from the input text.

        Parameters:
        - text (str): The input text containing special characters.

        Returns:
        - str: The text with special characters removed.
        """
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        return cleaned_text

    def replace_special_characters(self, text, replacement=''):
        """
        Replace special characters in the input text with the specified replacement.

        Parameters:
        - text (str): The input text containing special characters.
        - replacement (str): The string to replace special characters with. Defaults to an empty string.

        Returns:
        - str: The text with special characters replaced.
        """
        cleaned_text = re.sub(r'[^\w\s]', replacement, text)
        return cleaned_text
