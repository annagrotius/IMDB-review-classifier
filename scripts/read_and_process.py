"""
Script that contains the functions for pre-processing the review files. 
This script allows you to process one file at a time. It is used on multiple files in a 
in the script feature_extraction.py.
"""

import spacy
import string

# Load the English package of spacy as nlp.
nlp = spacy.load("en_core_web_sm")        

def read_file(filepath):
    """ 
    Reads and returns the content of a file as a string.
    It takes a filepath as a positional argument.
    """
    with open(filepath, 'r', encoding = "utf-8") as infile:
        review_text = infile.read()

    return review_text


def text_to_tokens(text):
    """ 
    Returns a sequence of tokens
    """
    content = nlp(text)
    
    return(content)


def clean_tokens(content_as_tokens):
    """
    Remove all punctuation and stopwords from the movie review file content.
    Return a clean list of tokens, meaning there are no stop words nor punctuation. 
    """
    spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS  
    punct = string.punctuation
    tokens_clean = []
    for token in content_as_tokens:
        if token.text not in spacy_stopwords and token.text not in punct:
            tokens_clean.append(token)
    
    return tokens_clean


def part_of_speech_and_lemma(tokens_clean):
    """ Gets the pos of a word. Returns a list of tuples with
        the format (lemma, pos). Takes a list as positional argument."""
    token_and_pos = []
    for token in tokens_clean:
        token_and_pos.append((token, token.pos_))
    
    return token_and_pos


def preprocess(filepath):
    """
    Reads files and preprocesses the data of a file.
    """
    file_content = read_file(filepath)
    tokens = text_to_tokens(file_content)
    tokens_clean = clean_tokens(tokens)
    lemma_and_pos = part_of_speech_and_lemma(tokens_clean)
    
    return(file_content, tokens, tokens_clean, lemma_and_pos)
    
    
def main():
    
    file = './data/train/pos/3920_9.txt'
    file_content, tokens, tokens_clean, lemma_and_pos = preprocess(file)
    
    
if __name__ == '__main__':
    main()
