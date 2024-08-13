# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:55:11 2024

@author: Dell
"""


import numpy as np
import pickle
import streamlit as st

load_model=pickle.load(open('D:/machien learning/trained_model.sav','rb'))

def dib_predict(input_data):
    input_numpy_array=np.asarray(input_data)
    input_reshape=input_numpy_array.reshape(1,-1)


    pridi=load_model.predict(input_reshape)
    print(pridi)


    if (pridi[0]==0):
        return "Congo you are not dibetic."
    else:
        return "Sorry ! but you are dibetic."
    
    
def main():
    st.title("DIABETES PREDICTION HERE")
    Pregnancies=st.text_input('Number Of Pregnancies')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('BP Value')
    SkinThickness=st.text_input('SkinThickness')
    Insulin=st.text_input('Insulin Level')
    BMI=st.text_input('BMI Value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    Age=st.text_input('Age')
    
    
    diagonsis = ''
    if st.button('RESULT'):
        diagonsis = dib_predict([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagonsis)
    
    
    
    
if __name__=='__main__':
    main()
    