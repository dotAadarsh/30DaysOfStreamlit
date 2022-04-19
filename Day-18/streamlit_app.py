import streamlit as st 
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input csv') 
uploaded_file = st.file_uploader("choose file", type='csv', accept_multiple_files=False, help = 'upload the file with the .csv format')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('Dataframe')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
    
else:
    st.info('please upload a csv file')
