def returnOverhead():
    f = open('output.py', 'w')
    f.write('import tensorflow as tf \n')
    f.write('from keras.models import Sequential \n')
    f.write('from keras import optimizers \n')
    f.write('from keras.layers import Dense, Embedding, LSTM \n')
    f.write('import numpy as np \n')
    f.write('from keras.models import model_from_json \n')
    f.write('from keras.models import load_model \n')
    f.write('from keras import backend \n')
    f.write('model = Sequential() \n')
    f.write('from preprocessing import trueCreateFeatureVector \n')
    f.close()

def addOthers():
    f = open('output.py', 'a')
    f.write('print(model.summary()) \n')
    f.write('model.fit(trainx,trainy, batch_size=batch_size, epochs=epochs, verbose=5) \n')
    f.write('score,acc = model.evaluate(valx,valy,verbose=2,batch_size=4) \n')
    f.write('print(acc) \n')
    f.close()
        
        
 




