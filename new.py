import streamlit as st
import pickle

with open('knn.pkl','rb') as f:
    model = pickle.load(f)

st.title('My KNN Model')
id = 1
age=st.number_input('Enter age')
salary=st.number_input('Enter Salary')
exp=st.number_input('Enter year')
dept=st.number_input('Enter Dept:(0-HR;1-IT;2-Sales)')
pred=model.predict([[id, age,salary,exp,dept]])
if st.button('Analyze'):
    if pred==1:
        st.sucess('done')
    else:
        st.warning('Not')