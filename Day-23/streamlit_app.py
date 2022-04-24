import streamlit as st

st.header('Day - 23 | st.experimental_get_query_params')
st.caption("Return the query parameters that is currently showing in the browser's URL bar.")
st.write("Let's say the user's web browser has a search query as base_url/?firstname=dotaadarsh&fav_framework=streamlit")

st.header('Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())

st.header('3. Retrieving and displaying information from the URL')
firstname = st.experimental_get_query_params()['firstname'][0]
fav_framework = st.experimental_get_query_params()['fav_framework'][0]

st.write(f'First name: {firstname}')
st.write(f'Favourite framework: {fav_framework}')
