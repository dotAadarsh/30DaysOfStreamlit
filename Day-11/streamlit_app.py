import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'Select the content type',
    ['Coding questions', 'Video', 'Reading', 'Interactive tutorials', 'Online courses', 'Quiz'],
    ['Video', 'Quiz', 'Reading'], 
    disabled = 0,help = "help"
)

st.write('You selected: ', options)