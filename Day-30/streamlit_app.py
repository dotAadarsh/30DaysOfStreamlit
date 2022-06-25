import streamlit as st

st.set_page_config(page_title="Yt-img-app", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)


st.title('Yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
st.sidebar.title("#30DaysOfStreamlit - Day 30")

with st.expander('About this app'):
    st.write('This app retrieves the thumbnail image feom the youtube video')

st.sidebar.header('Setting')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]


yt_url = st.text_input('Paste Youtube URL', 'https://youtu.be/R2nr1uZ8ffc')

def get_ytid(input_url):
    if 'youtu.be' in input_url:
        ytid = input_url.split('/')[-1]
    if 'https://www.youtube.com/watch?v=' in input_url:
        ytid = input_url.split('=')[-1]
    return ytid

if yt_url != '':
    ytid = get_ytid(yt_url)

    yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
    st.image(yt_img)
    st.write('YouTube video thumbnail image URL: ', yt_img)
else:
    st.write('Enter URL to continue')