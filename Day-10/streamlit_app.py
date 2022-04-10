import streamlit as st

# st.selectbox
st.header('st.selectbox')

option = st.selectbox(
    'Select your job type',
    ('Internship', 'Part-time', 'Full-time',),
    index = 1,
    help = 'Choose your job type to filter the result',
    disabled=0,
    
)

st.write('Your job type is ', option)
