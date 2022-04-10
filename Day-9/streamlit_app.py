import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# st.line_chart

st.header('st.line_chart()')
st.subheader('Display a line chart.')

chart_data = pd.DataFrame(
    np.random.randn(25,3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

# st.altair_chart 

st.header('st.altair_chart')
st.subheader('Display a chart using the Altair library.')

df = pd.DataFrame(
    np.random.randn(150,3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size = 'c', color='c', tooltip = ['a', 'b', 'c']
)

st.altair_chart(c, use_container_width=True)
