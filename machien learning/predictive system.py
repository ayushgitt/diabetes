# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
load_model=pickle.load(open('D:/machien learning/trained_model.sav','rb'))

input=(8,183,64,0,0,23.3,0.672,32)
input_numpy_array=np.asarray(input)
input_reshape=input_numpy_array.reshape(1,-1)


pridi=load_model.predict(input_reshape)
print(pridi)


if (pridi[0]==0):
    print("Congo you are not dibetic.")
else:
    print("Sorry ! but you are dibetic.")