import regex
import spacy
nlp = spacy.load("en_core_web_sm")



def clean_text(series, keep_punctuation=".,;?!"):
    """
    Clean a pandas Series by removing non-alphanumeric characters while keeping specified punctuation symbols.

    Parameters:
    - series (pd.Series): The pandas Series to clean.
    - keep_punctuation (str): Punctuation symbols to keep. Default is ".,;?!".

    Returns:
    - pd.Series: Cleaned pandas Series.
    """
    pattern = f'[^a-zA-Z0-9\\s{keep_punctuation}]'
    
    cleaned_series = series.str.replace(pattern, '', regex=True)
    
    return cleaned_series

def tokenize_text(text):
    """
    The `tokenize_text` function takes in a text as input and returns a list of tokens, where each token
    represents a word or punctuation mark in the text.
    
    :param text: The `text` parameter is a string that represents the text you want to tokenize
    :return: The function `tokenize_text` returns a list of tokens, where each token is a string.
    """
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens

def tokenize_text_with_numbers(text):
    """
    The function `tokenize_text_with_numbers` takes in a text as input, tokenizes it using the `nlp`
    function, and returns a list of tokens excluding any digits.
    
    :param text: The `text` parameter is a string that represents the text you want to tokenize
    :return: The function `tokenize_text_with_numbers` returns a list of tokens (words) from the input
    text, excluding any tokens that are digits (numbers).
    """
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_digit]
    return tokens