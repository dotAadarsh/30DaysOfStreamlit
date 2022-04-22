import streamlit as st 
import time

st.title('Day-21 | st.progress')

with st.expander('About this app'):
    st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command')

a = st.button('click to execute')
if a ==True:
    progress_bar= st.progress(0)
    
    for percent_Complete in range(100):
        time.sleep(0.05)
        progress_bar.progress(percent_Complete)
    st.balloons()
