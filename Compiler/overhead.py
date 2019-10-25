class Overhead():
    def __init__(self, sess):
        self.session = sess 
    def returnOverhead(self):
        f = open('intermediate.py' 'w')
        f.write('import tensorflow as tf')
        f.write('from tensorflow.keras.models import Sequential')
        f.write('from tensorflow.keras import optimizers')
        f.write('from tensorflow.keras.layers import Dense, Embedding, LSTM')
        f.write('import numpy as np')
        f.write('from tensorflow.keras.models import model_from_json')
        f.write('from tensorflow.keras.models import load_model')
        f.write('from tensorflow.keras import backend')
        
        
 




