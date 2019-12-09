import pandas as pd
import nltk
import random
import sys
import os
# from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

print(os.getcwd())
data_frame = pd.read_csv('GenrePrediction/Data/sample_data.csv')
tf_transformer = pickle.load(open('GenrePrediction/Model/tfidf.pkl', 'rb'))
matrix = tf_transformer.transform(data_frame['lyrics'])

def similar_songs(lyric):
    tf_new = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), stop_words='english', lowercase=True,
                             vocabulary = tf_transformer.vocabulary_)
    x_matrix = tf_new.fit_transform([lyric])
    cosine_similarities = linear_kernel(matrix, x_matrix).flatten()
    related_docs_indices = [i for i in cosine_similarities.argsort()[::-1]]
    list_5_similar_songs = [(index, cosine_similarities[index]) for index in related_docs_indices][0:5]
    main_output = ''
    for i in list_5_similar_songs:
        output = ' Song Name: ' + data_frame.iloc[i[0]]['song'] + ' by ' + data_frame.iloc[i[0]]['artist'] + \
                 ' of genre ' + data_frame.iloc[i[0]]['genre'] + ' with similarity score ' + str(round(i[1],4)) + '. '
        main_output = main_output + output
    return main_output


