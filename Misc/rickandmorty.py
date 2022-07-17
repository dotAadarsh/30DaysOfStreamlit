import streamlit as st

st.title("OOH WEE!")

st.header("Rick and Morty")

st.subheader("American adult animated science fiction sitcom")

st.image("https://upload.wikimedia.org/wikipedia/commons/9/9e/Rick_and_Morty_title_card.png", caption = "Justin Roiland and Dan Harmon, Public domain, via Wikimedia Commons")

st.write('**Rick and Morty** is one of the best animated series on television. The show is about the adventures of Rick, a mad scientist, and his grandson, Morty. The series is hilarious and has a lot of heart.')

code = '''def rick():
     print("Boom! Big reveal! I turned myself into a code block")'''

st.code(code, language='python')

if st.button("Just don't click this button"):
     st.image('https://c.tenor.com/5IFS2BehSGUAAAAC/morty-you-dirty-little-doggy.gif')

dimension = st.slider('Select your dimension', 0, 200, 137)
st.write("I'm from C-", dimension, ' dimension')

fav = st.selectbox(
     'Who is your favourite character?',
     ('Rick Sanchez', 'Morty Smith', 'Birdperson', 'Summer Smith', 'Mr. Poopybutthole'))

st.write('You favourite character is ', fav)

st.info('Nobody exists on purpose. Nobody belongs anywhere. We are all going to die. Come lets built apps with Streamlit')
