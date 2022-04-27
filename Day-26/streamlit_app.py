import streamlit as st  
import requests
from numpy import random

st.title('#1 Bored API app')

st.sidebar.header('Bored API')
selected_type = st.sidebar.selectbox('Select an activity type', ['education', 'recreational', 'social', 'diy', 'cooking', 'relaxation'])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1: 
    with st.expander('Abou the app'):
        st.write('Are you bored? The bored API provides the suggestion of activities that you can do when you are bored. This app is powered by Bored API')
with c2:
    with st.expander('JSON data'):
        st.write(suggested_activity)


st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1: 
    st.metric(label='Number of participants', value = suggested_activity['participants'], delta = '')
with col2: 
    st.metric(label='Type of activity', value = suggested_activity['type'].capitalize(),delta='')
with col3: 
    st.metric(label= 'Price', value = suggested_activity['price'], delta = '')


st.title('#2 Art Institute of Chicago API')
st.sidebar.header('Art Institute of Chicago API')
option = st.sidebar.selectbox("Select an art query", ['abstract', 'architecture', 'drama', 'massacre'])

art_url = f'https://api.artic.edu/api/v1/artworks/search?q={option}&query[term][is_public_domain]=true&limit=20&fields=id,title,image_id'
json_data = requests.get(art_url)
art = json_data.json()

st.write(art['info']['license_text'])
x = random.randint(20)


id = art['data'][x]['image_id']
title = art['data'][x]['title']

image_url = art['config']['iiif_url']

col1, col2 = st.columns(2)
with col1:
    st.json(art['data'][x])
    new = st.button('New Art')
with col2:
        st.image(f'{image_url}/{id}/full/843,/0/default.jpg')
        st.subheader(title)
        
        