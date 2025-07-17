import streamlit as st
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier


st.title('My KNN Model')
df=pd.read_csv('employee.csv')
df.dropna(inplace=True)#Delete duplicate value
le=LabelEncoder()#Making object
df['Department']=le.fit_transform(df['Department'])
x=df.drop('Stays (1=Yes, 0=No)',axis='columns')
y=df['Stays (1=Yes, 0=No)']
model=KNeighborsClassifier()
model.fit(x,y)
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