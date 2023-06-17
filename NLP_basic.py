import nltk
import tensorflow as tf
import numpy as np
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
from nltk.corpus import stopwords


# Import Data and make a dataset

(train_data, test_data), info = tfds.load('imdb_reviews/plain_text',
                                          split=(tfds.Split.TRAIN, tfds.Split.TEST),
                                          with_info=True, as_supervised=True,
                                          )
encoder = info.features['text'].encoder
print(201 % 4)
nltk.download('stopwords')
print(stopwords.words('english'), end="/n")