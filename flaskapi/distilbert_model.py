import os
import ktrain

def get_prediction(x):
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1" # use only CPU in prediction
    predictor = ktrain.load_predictor('/flaskapi/distilbert')
    sent = predictor.predict([x])
    return sent[0]