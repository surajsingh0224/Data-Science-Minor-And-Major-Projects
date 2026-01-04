import numpy as np 
import pickle

loaded_model = pickle.load(open('C:/Users/Suraj Singh/Desktop/Data Science/projects/10. Diabetes Prediction using Machine Learning/trained_model.sav', 'rb')) # Reading the binary format

input_data = (3,126,88,41,235,39.3,0.704,27) 
# Change input data into numpy array 
input_data_as_numpy_array = np.asarray(input_data)
# reshape the array as we are predicting for one instance 
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1) 

# print(std_data)

prediction = loaded_model .predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
    print("The person is not diabetic")
else: 
    print("the person is diabetic")