import regex

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