import tensorflow as tf 
from keras.models import Sequential 
from keras import optimizers 
from keras.layers import Dense, Embedding, LSTM 
import numpy as np 
from keras.models import model_from_json 
from keras.models import load_model 
from keras import backend 
model = Sequential() 
from preprocessing import trueCreateFeatureVector 
batch_size =10
epochs =15
drop =0.01
r_drop =0.02
trainx,trainy,testx,testy,valx,valy = trueCreateFeatureVector('./trainables/testPost1','./trainables/trestneg1')
model.add(Embedding(23 , 23, input_length=10))
model.add(LSTM(10, dropout = 0.1, recurrent_dropout = 0.1, return_sequences = True, unroll = True, recurrent_activation = 'softmax',bias_initializer='RandomNormal',implementation=1)) 
model.add(LSTM(10, dropout = 0.1, recurrent_dropout = 0.1, return_sequences = True, unroll = True, recurrent_activation = 'softmax',bias_initializer='RandomNormal',implementation=1)) 
model.add(LSTM(10, dropout = 0.1, recurrent_dropout = 0.1, return_sequences = True, unroll = True, recurrent_activation = 'softmax',bias_initializer='RandomNormal',implementation=1)) 
model.add(LSTM(10, dropout = 0.1, recurrent_dropout = 0.1, unroll = True, recurrent_activation = 'softmax' ,bias_initializer='RandomNormal',implementation=1)) 
model.add(Dense(2, activation ='softmax', use_bias= True, kernel_initializer= 'glorot_uniform', kernel_regularizer=None, bias_regularizer =None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None))
optimizerx =  optimizers.Adam(lr=0.001) 
model.compile(loss ='categorical_crossentropy', optimizer = optimizerx,metrics=['accuracy']) 
print(model.summary()) 
model.fit(trainx,trainy, batch_size=batch_size, epochs=epochs, verbose=5) 
score,acc = model.evaluate(valx,valy,verbose=2,batch_size=4) 
print(acc) 
