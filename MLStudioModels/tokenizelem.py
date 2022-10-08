# downloading resources and importing libraries
import nltk
nltk.download('punkt')
nltk.download('wordnet')

# import pandas as pd
# import numpy as np

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import re
def tokenize_lem(sentences):
    '''
    tokenizes a bunch of sentences after normalizing it and returns lemmatized tokens.
    
    INPUT:
    sentences - a paragraph that needs to be tokenized
    
    OUTPUT:
    tokens - list of lemmatized tokens
    
    '''
    # normalizing, tokenizing, lemmatizing 
    sentences = re.sub('\W',' ',sentences) 
    sentences = re.sub('[0-9]',' ',sentences)

    tokens = word_tokenize(sentences)
    tokens = [i.strip() for i in tokens]
    
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(i) for i in tokens]
    return tokens