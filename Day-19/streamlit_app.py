import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your streamlit')

with st.expander('About this app', expanded=False):
    st.write('Its a Day-19 challenge - to learn how we can layout the streamlit app')
    st.image('https://media.giphy.com/media/gskdRMXaRv4e0Qt2sx/giphy-downsized-large.gif', width=220,)

st.sidebar.header('Input')
username = st.sidebar.text_input('What is your name')
language = st.sidebar.selectbox('Whats your favourite language?', ['C', 'CPP', 'Java', 'Python', 'Javascript'])
age = st.sidebar.slider('Whats your age?', 13, 100)


st.header('your info')

col1, col2, col3 = st.columns(3)

with col1: 
    if username != '':
        st.write(f'Name: {username}' )
    else:
        st.write('👈 Please enter your name')

with col2:
    if language != '':
        st.write(f'Favourite language: {language}')
    else:
        st.write('👈 Choose your favourite language')

with col3: 
    st.write(f'Age: {age}')

with st.container(): 
    with st.expander('Click to expand'):
        st.write('Inside container')
        st.image('https://media.giphy.com/media/3o6wO7N2pXvW83NLna/giphy.gif')

import time

with st.empty():
     for seconds in range(10):
         st.write(f"⏳ {seconds} seconds have passed")
         time.sleep(1)
     st.write("✔️ 10 seconds over!")


placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
     st.write("This is one element")
     st.write("This is another")

# Clear all those elements:
placeholder.empty()

