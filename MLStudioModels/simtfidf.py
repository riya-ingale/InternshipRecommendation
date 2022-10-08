# downloading resources and importing libraries

# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import re
from .tokenizemod import tokenize
def similarity_matrix_wo_tfidf(df):
    '''
    returns a similarity matrix, in the form of a dataframe, between different internships by using the 
    Skills Required section
    
    INPUT:
    df - dataframe with 'skills required' as one of the columns
    
    OUTPUT:
    sim - similarity matrix(dataframe) with internship id as column and row labels 
    
    '''
    # df.insert(0, 'id', range(0, 0 + len(df)))
    details = df['Skills Required']
    vect = CountVectorizer(tokenizer= tokenize, stop_words = 'english')
    
    mat = vect.fit_transform(details).toarray()
    sim = np.dot(mat, mat.T)
    sim = pd.DataFrame(sim, columns=df.id, index = df.id)
    return sim