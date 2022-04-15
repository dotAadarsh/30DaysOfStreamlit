import streamlit as st
import streamlit.components.v1 as components

HtmlFile = open("/workspace/30DaysOfStreamlit/Day-14/index.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 

st.header('Streamlit Component')
st.subheader('360° Image VR - Example')

components.html(source_code, width = None, height=500)

st.markdown('Reference - A-Frame | [Building a 360° Image Gallery ](https://aframe.io/docs/1.3.0/guides/building-a-360-image-gallery.html)')

st.markdown('**Image credit** - Maximilian Schönherr, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons')