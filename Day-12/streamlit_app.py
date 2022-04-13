import streamlit as st 

st.header('st.checkbox')
st.write ('Select the course(s) that you want')

CNC_Tech = st.checkbox('18MC601',help ='Select to opt CNC Tech', value = 1) 
Embeded_Systems = st.checkbox('18MC602', help ='Select to opt Embeded Systems')
Machine_Design = st.checkbox('18MC603', help ='Select to opt Machine Design')
Thermodynamics = st.checkbox('18MC604', help ='Select to opt Thermodynamics', value = 1)

if CNC_Tech:
     st.write("You have opted CNC Technology!🤖")

if Embeded_Systems: 
     st.write("Good luck with the embeded systems")

if Machine_Design:
     st.write("Here comes the machine design ⚙️")

if Thermodynamics:
    st.write('Its hot in here - let the thermodyanmics 🌡️ take care of it ')
