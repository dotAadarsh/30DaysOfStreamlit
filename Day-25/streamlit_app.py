import streamlit as st

st.title('st.session_state') 

st.subheader('Counter example')

if "count" not in st.session_state:
  st.session_state.count = 0

increment = st.button("incement")
if increment:
  st.session_state.count+=1

st.write("count: ", st.session_state.count )

st.subheader('lbs to kg | kg to lbs example')
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs(): 
  st.session_state.lbs = st.session_state.kg*2.2046

st.caption('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.subheader('Option example')
col1, buff, col2 = st.columns([1,0.5,3])
option_names = ["a", "b", "c"]
next = st.button("Next option")

if next:
  if st.session_state["radio_options"] == 'a':
    st.session_state.radio_options = 'b'
  elif st.session_state["radio_options"] == 'b':
    st.session_state.radio_options = 'c'
  else:
    st.session_state.radio_options = 'a'

option = col1.radio("Pick an option", option_names, key = "radio_options")

if option == 'a':
  col2.write("You picked a: :apple:")
elif option == 'b':
  col2.write("You picked b: :smile:")
else :
  col2.write("You picked c : :heart:")

st.subheader('Output')
st.write("st.session_state object:", st.session_state)
