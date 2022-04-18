import streamlit as st 

st.title('st.secrets | Day-17')
st.caption('st.secrets allows you to store confidential information such as API keys, database passwords or other credentials.')

st.write("DB username: ", st.secrets["owner"]["name"])
st.write("DB password: ", st.secrets["owner"]["password"])
st.write("My cool secrets: ", st.secrets["my_cool_secrets"]["things_i_like"])
st.write("Database state: ", st.secrets["database"]["enabled"])
st.write("ports: ", st.secrets["database"]["ports"])


import os
st.write("Has environment variable been set: ", os.environ["title"]==st.secrets["title"])
