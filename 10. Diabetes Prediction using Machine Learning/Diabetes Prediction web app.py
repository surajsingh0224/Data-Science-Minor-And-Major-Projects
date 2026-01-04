import numpy as np 
import pickle 
import streamlit as st 

loaded_model = pickle.load(open('C:/Users/Suraj Singh/Desktop/Data Science/projects/10. Diabetes Prediction using Machine Learning/trained_model.sav', 'rb'))

 # creating a function for prediction 

def Diabetes_prediction(input_data): 
    
    
    # Change input data into numpy array 
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance 
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1) 

    # print(std_data)

    prediction = loaded_model .predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else: 
        return 'the person is diabetic'

def main(): 
    # Title for webpage 
    st.title('Diabetes prediction web application')
    
    # getting the input data from the user 
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input("Skin Thickness")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    Age = st.text_input("Age of the person")
    
    # code for prediction 
    diagnosis = ''
    # creating a button for prediction 
    if st.button("Diabetes Test Result"):
        diagnosis = Diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
    
if __name__ == '__main__': 
    main() 
    
    

















