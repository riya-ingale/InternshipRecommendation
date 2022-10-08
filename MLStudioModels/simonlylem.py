# downloading resources and importing libraries

# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from .tokenizelem import tokenize_lem
def similarity_matrix_w_lem_wo_tfidf(df):
    '''
    returns a similarity matrix, in the form of a dataframe, between different internships by using the 
    details section
    
    INPUT:
    df - dataframe with 'Skills Required' as one of the columns
    
    OUTPUT:
    sim - similarity matrix(dataframe) with internship id as column and row labels 
    '''
    details = df['Skills Required']
    vect = CountVectorizer(tokenizer= tokenize_lem, stop_words = 'english')
    tfidf = TfidfTransformer()
    
    mat = vect.fit_transform(details).toarray()
    sim = np.dot(mat, mat.T)
    sim = pd.DataFrame(sim, columns=df.id, index = df.id)
    return sim