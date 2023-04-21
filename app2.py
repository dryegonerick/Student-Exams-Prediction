import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# load the saved model using pickle
with open('lasso_model.pkl', 'rb') as f:
    lasso_loaded = pickle.load(f)

# define function to make prediction
def predict_grade(df):
    # make prediction using loaded model
    prediction = lasso_loaded.predict(df)

    # round prediction to nearest integer
    prediction = int(round(prediction[0]))

    # return predicted grade
    return prediction

# define function to create input form
def create_form():
    # create empty dictionary for input values
    inputs = {}
    # encode binary categorical features using label encoding
    label_encoder = LabelEncoder()
    # create input form for each feature
    inputs['school'] = st.radio("Student's school", ['GP', 'MS'])
    inputs['school'] = label_encoder.fit_transform([inputs['school']])[0]
    inputs['sex'] = st.radio("Student's sex", ['F', 'M'])
    inputs['sex'] = label_encoder.fit_transform([inputs['sex']])[0]
    inputs['age'] = st.slider('Age', 15, 22, 18)
    inputs['address'] = st.radio('Address type', ['U', 'R'], key='address')
    inputs['address'] = label_encoder.fit_transform([inputs['address']])[0]
    inputs['famsize'] = st.radio('Family size', ['LE3', 'GT3'], key='famsize')
    inputs['famsize'] = label_encoder.fit_transform([inputs['famsize']])[0]
    inputs['Pstatus'] = st.radio('Parents cohabitation status', ['T', 'A'], key='Pstatus')
    inputs['Pstatus'] = label_encoder.fit_transform([inputs['Pstatus']])[0]
    inputs['Medu'] = st.selectbox("Mother's education level", [0, 1, 2, 3, 4], key='Medu')
    inputs['Fedu'] = st.selectbox("Father's education level", [0, 1, 2, 3, 4], key='Fedu')
    inputs['guardian'] = st.selectbox('Legal guardian', ['mother', 'father', 'other'], key='guardian')
    inputs['guardian'] = label_encoder.fit_transform([inputs['guardian']])[0]
    inputs['traveltime'] = st.selectbox('Travel time to school (hours)', [1, 2, 3, 4], key='traveltime')
    inputs['studytime'] = st.selectbox('Weekly study time (hours)', [1, 2, 3, 4], key='studytime')
    inputs['schoolsup'] = st.radio('Extra educational support', ['yes', 'no'], key='schoolsup')
    inputs['schoolsup'] = label_encoder.fit_transform([inputs['schoolsup']])[0]
    inputs['famsup'] = st.radio('Family educational support', ['yes', 'no'], key='famsup')
    inputs['famsup'] = label_encoder.fit_transform([inputs['famsup']])[0]
    inputs['paid'] = st.radio('Extra paid classes within the course subject', ['yes', 'no'], key='paid')
    inputs['paid'] = label_encoder.fit_transform([inputs['paid']])[0]
    inputs['activities'] = st.radio('Extracurricular activities', ['yes', 'no'], key='activities')
    inputs['activities'] = label_encoder.fit_transform([inputs['activities']])[0]
    inputs['nursery'] = st.radio('Attended nursery school', ['yes', 'no'], key='nursery')
    inputs['nursery'] = label_encoder.fit_transform([inputs['nursery']])[0]
    inputs['higher'] = st.radio('Wants to take higher education', ['yes', 'no'], key='higher')
    inputs['higher'] = label_encoder.fit_transform([inputs['higher']])[0]
    inputs['internet'] = st.radio('Internet access at home', ['yes', 'no'], key='internet')
    inputs['internet'] = label_encoder.fit_transform([inputs['internet']])[0]
    inputs['romantic'] = st.radio('In a romantic relationship', ['yes', 'no'], key='romantic')
    inputs['romantic'] = label_encoder.fit_transform([inputs['romantic']])[0]
    inputs['absences'] = st.slider('Number of school absences', 0, 100, 5)
    inputs['internet_access'] = st.radio('Internet access at home', ['yes', 'no'], key='internet_access')
    inputs['internet_access'] = label_encoder.fit_transform([inputs['internet_access']])[0]
    inputs['total_study_time'] = st.slider('Total study time per week (hours)', 0, 50, 10)
    inputs['family_quality'] = st.slider('Quality of family relationships', 1, 5, 4)

    # convert input values to dataframe
    df = pd.DataFrame(inputs, index=[0])

    # return filled dataframe
    return df

# create Streamlit app
st.set_page_config(page_title='Student Grade Prediction')
st.title('Student Grade Prediction')

# create input form
df = create_form()

# create button to make prediction
if st.button('Predict Grade'):
    # make prediction and display result
    grade = predict_grade(df)
    st.success(f'The predicted final exam grade is: {grade}')

