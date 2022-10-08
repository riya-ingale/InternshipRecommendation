def similarity_matrix_cat(df):
    '''
    returns a similarity matrix, in the form of a dataframe, between different internships by using the 
    cat section
    
    INPUT:
    df - dataframe with 'Title' as one of the columns
    
    OUTPUT:
    sim - similarity matrix(dataframe) with internship id as column and row labels 
    '''
    cats = df['Title']
    vect = CountVectorizer(tokenizer= tokenize, stop_words = 'english')
    tfidf = TfidfTransformer()
    
    mat = vect.fit_transform(cats).toarray()
    sim = np.dot(mat, mat.T)
    sim = pd.DataFrame(sim, columns=df.id, index = df.id)
    return sim