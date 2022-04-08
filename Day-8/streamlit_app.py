import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1
st.subheader('Sldier')
age = st.slider('How old are you?', 0, 130, 40)
st.write("I'm", age, 'years old')

# Example 2
st.subheader('Range slider')
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (30.0, 70.0)
)
st.write('Values: ', values)

# Example 3
st.subheader('Range time slider')
appointment = st.slider(
    'Schedule your appointment: ',
    value =(time(9,30), time(12,45)) 
)
st.write("You're scheduled for: ", appointment)

# Example 4
start_time = st.slider(
    "When do you start?", 
    value = datetime(2020,1,1,9,30),
    format = "MM/DD/YY - hh:mm"
)
st.write("Start time: ", start_time)

# st.select_slider
st.subheader('st.select_slider')
size = st.select_slider(
     'Select the size',
     options=['S', 'M', 'L', 'XL', 'XXL'])
st.write('My size is', size)

# range select slider
st.subheader('Range select slider')
start_slider, end_slider = st.select_slider(
    'Select the range of size', 
    options= ['S', 'M', 'L', 'XL', 'XXL'],
    value=('S', 'L')
)
st.write('You selected the range between ', start_slider, 'and', end_slider)