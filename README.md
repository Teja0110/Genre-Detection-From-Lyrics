
# Genre Prediction Project
Bao Nguyen - Teja kalvakolanu - Nagasai Chandra


### Used Libraries
Django 2.1.2
Pandas
nltk
sys
numpy
joblib
sk-learn
Keras

### Usage
Change directory to .\MusicGenre and run
python manage.py runserver  (This will give u a local host address)


### Project Description

#### Data: 
	- lyrics.csv : Raw data https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics

#### Files:
	- data_preprocess.py : Pre process the data
	- trainning.py : Training in different models
	- Predict.py : Provide API to predict a genre by lyrics
	- similar lyrics.py: Song recommendation
	- valid.py : Generating the reasons

#### .\MusicGenre: Django project folder, includes all the files we mentioned above to running the web service and do prediction
	
