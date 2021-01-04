import pandas as pd
import numpy as np
import ktrain
from ktrain import text
import tensorflow as tf

data_test = pd.read_excel('/flaskapi/IMDB-Movie-Reviews-Large-Dataset-50k/test.xlsx', dtype= str)
data_train = pd.read_excel('/flaskapi/IMDB-Movie-Reviews-Large-Dataset-50k/train.xlsx', dtype = str)

(train, val, preproc) = text.texts_from_df(train_df=data_train, text_column='Reviews', label_columns='Sentiment',
                   val_df = data_test,
                   maxlen = 400,
                   preprocess_mode = 'distilbert')

model = text.text_classifier(name = 'distilbert', train_data = train, preproc=preproc)
learner = ktrain.get_learner(model = model,
                             train_data = train,
                             val_data = val,
                             batch_size = 6)

learner.fit_onecycle(lr = 2e-5, epochs=2)
predictor = ktrain.get_predictor(learner.model, preproc)

predictor.save('/flaskapi/distilbert')

data = ['this movie was really bad. acting was also bad. I will not watch again',
        'the movie was really great. I will see it again', 'another great movie. must watch to everyone']

predictor.predict(data)