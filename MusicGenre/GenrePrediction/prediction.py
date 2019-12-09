import sys
import numpy as np
# For export model
from sklearn.externals import joblib

# nltk
import nltk
# Download nltk package
nltk.download('punkt')
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# Stop words
from nltk.corpus import stopwords
nltk.download('stopwords')
eng_stopwords = set(stopwords.words('english'))
#lemmatizer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


# Preprocess a song
def preprocess_a_lyric(input):
  tmp_lyric = [word.lower() for word in nltk.word_tokenize(input) if word.isalpha()]
  tmp_lyric = ' '.join([lemmatizer.lemmatize(word) for word in tmp_lyric if word not in eng_stopwords])
  return tmp_lyric


def predict_a_song(input, clf):
  #load_model_dir = 'Model/genrePredict.pkl'
  #clf = joblib.load(load_model_dir) 
  out = preprocess_a_lyric(input)
  return clf.predict([out])[0]
  

def main(argv):
    if len(argv) != 2:
        print('usage python3 predict.py input')
        sys.exit()

    f = open(argv[1], "r")
    
    data = f.read()
    load_model_dir = 'Model/genrePredict.pkl'
    clf = joblib.load(load_model_dir)
    print("Genre of this lyric is ", predict_a_song(data, clf))
