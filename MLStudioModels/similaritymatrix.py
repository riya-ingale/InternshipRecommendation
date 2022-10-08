# downloading resources and importing libraries

# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

from .tokenizemod import tokenize
def similarity_matrix(df):
    '''
    returns a similarity matrix, in the form of a dataframe, between different internships by using the 
    details section of df.
    
    INPUT:
    df - dataframe with 'details' as one of the columns
    
    OUTPUT:
    sim - similarity matrix(dataframe) with internship id as column and row labels 
    
    '''
    # df.insert(0, 'id', range(0, 0 + len(df)))
    details = df['Skills Required']
    vect = CountVectorizer(tokenizer= tokenize, stop_words = 'english')
    tfidf = TfidfTransformer()
    
    mat = tfidf.fit_transform(vect.fit_transform(details).toarray()).toarray()
    sim = np.dot(mat, mat.T)
    sim = pd.DataFrame(sim, columns=df.id, index = df.id)
    return sim