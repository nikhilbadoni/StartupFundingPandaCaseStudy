import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('And I am loving it')
st.write('This is a normal text')
st.markdown("""
#### My Fav Movies 
- OMG
- Hello World
""")
            
st.code("""
def foo():
        return foo**2

x = foo(2)
""")
st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame({
    'name': ['Nitish', 'Ankit', 'Akhi'],
    'marks': [50,60,70],
    'package': [10,12,14]
})

st.dataframe(df)

st.metric('Revenue', '3L','-3%')

st.json({
    'name': ['Nitish', 'Ankit', 'Akhi'],
    'marks': [50,60,70],
    'package': [10,12,14]
})
st.image('download.png')

# creating Layout

st.sidebar.title("Sidebar's Title ")
col1,col2 = st.columns(2)

with col1:
    st.image('download.png')

with col2:
    st.image('download.png')

# Showing Status

st.error('Login Failed')
st.success('Login Successful')
st.info('Login Successful')
st.warning('Login Successful')

bar = st.progress(0)

for i in range(0,101):
    bar.progress(i)


email = st.text_input('Enter Email')
number = st.number_input('Enter age')
st.date_input('Enter Registration Date')

email = st.text_input('Enter Email')
password = st.text_input('Enter Password')
gender = st.selectbox('Select Gender',['Male', 'Female', 'Others'])

btn = st.button('Login')

if btn:
    if email == 'nikhil@gmail.com' and password == '1234':
        st.balloons()
        st.success('Login Successful')
        st.write(gender)
    else:
        st.error('Login Failed')


file = st.file_uploader('Upload a CSV File')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())