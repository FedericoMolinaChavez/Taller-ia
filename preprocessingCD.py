import numpy as np
import os
import pickle
from PIL import Image 
import glob 
import random 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "database/train")
def preprocessing():
    trainx , trainy, valx, valy, testx, testy = [],[],[],[],[],[]
    entirex, entirey = [], []
    for root, dirs, files in os.walk(image_dir):
        random.shuffle(files)
        for i in files:
            file = os.path.join(root, i)
            aux = i.split('.')
            if(aux[0] == 'dog'):
                entirey.append([0,1])
            else:
                entirey.append([1,0])
            pil_image = Image.open(file).convert("L")
            size = (100, 100)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")
            image_array = image_array/255
            entirex.append(image_array)
    
    trainx = entirex[0 : int(len(entirex)*0.8)]
    testx = entirex[int(len(entirex)*0.8):]

    valx = trainx[int(len(trainx)*0.9):]
    trainx = trainx[0:int(len(trainx)*0.9)]

    trainy = entirey[0 : int(len(entirey)*0.8)]
    testy = entirey[int(len(entirey)*0.8):]

    valy = trainy[int(len(trainy)*0.9):]
    trainy = trainy[0:int(len(trainy)*0.9)]
    with open("pickles/image_data.pickle", 'wb') as f:
        pickle.dump([np.array(trainx),np.array(trainy),np.array(testx),np.array(testy),np.array(valx),np.array(valy)], f)
    return (trainx,trainy,testx,testy,valx,valy)


def testPickle():
    objects = []
    with (open("./pickles/image_data.pickle", "rb")) as f:
        while True:
            try:
                objects.append(pickle.load(f))
            except EOFError:
                break
    print(objects)

preprocessing()