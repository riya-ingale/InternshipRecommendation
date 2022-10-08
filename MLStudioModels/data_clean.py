# downloading resources and importing libraries

# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')

# import pandas as pd
# import numpy as np

# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.stem import PorterStemmer, WordNetLemmatizer
# from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

# import re

def dataclean(df):
    df.loc[df['Title'] == 'Business Development (Sales)', 'Skills Required'] = 'Sales, Marketing'
    df.loc[df['Title'] == 'Human Resources (HR)', 'Skills Required'] = 'Problem Solving, Pulic Relations'
    df.loc[df['Title'] == 'Graphic Design', 'Skills Required'] = 'Creativity'
    df.loc[df['Title'] == 'Digital Marketing', 'Skills Required'] = 'Digital Marketing'
    df.loc[df['Title'] == 'Marketing', 'Skills Required'] = 'Marketing'
    df.loc[df['Title'] == 'Content Writing', 'Skills Required'] = 'Engish Proficiency'
    df.loc[df['Title'] == 'Personal Assistance', 'Skills Required'] = 'Communication Skills'
    df.loc[df['Title'] == 'Web Development', 'Skills Required'] = 'Full Stack Development'
    df.loc[df['Title'] == 'Social Media Marketing', 'Skills Required'] = 'Social Media Marketing'
    df.loc[df['Title'] == 'Virtual Assistance', 'Skills Required'] = 'Communication  Skills'
    df.loc[df['Title'] == 'Business Analytics', 'Skills Required'] = 'Data Analysis'
    df.loc[df['Title'] == 'Data Entry', 'Skills Required'] = 'Microsoft Excel'
    df.loc[df['Title'] == 'Property Surveying', 'Skills Required'] = 'Communication Skills'
    df.loc[df['Title'] == 'Subject Matter Expert (Medical)', 'Skills Required'] = 'Medical Expert'
    df.loc[df['Title'] == 'Qliksense Development', 'Skills Required'] = 'AI'
    df.loc[df['Title'] == 'Education Counseling', 'Skills Required'] = 'Counseling'
    df["Skills Required"].fillna("Communication Skills", inplace = True)
    df['Skills Required'].str.lower()
    df['Location'].str.lower()
    df.insert(0, 'id', range(0, 0 + len(df)))
    return df


