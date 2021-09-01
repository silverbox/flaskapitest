# Overview

test

It's test for sentiment classification by BERT with ktrain library.
Service is consist with nginx and flask-uwsgi container.
This main logic of prediction is based on the following Udemy cource.
https://www.udemy.com/course/nlp-with-bert-in-python/
About the model I tested is made at google collaboratory.
make_model.py will work to make model. but I didn't test. beacause It's too slow on my machine.

# test
curl -X POST -d '{ "Review" : "it is boring movie"}' http://localhost:8881/get_sentiment
curl -X POST -d '{ "Review" : "it is great movie"}' http://localhost:8881/get_sentiment
