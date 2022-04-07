import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1
st.write('Hello, *streamlit* :wave:')

# Example 2
st.write(123456)

# Example 3
df = pd.DataFrame({
    'First coloumn': [1,2,3,4],
    'Second coloumn': [10,20,30,40]
})

st.write(df)

# Example 4
st.write('Below is a DataFrame:', df, 'Above is a DataFrame')

# Example 5

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip = ['a', 'b', 'c'] 
)

st.write(c)


# Further Reading

st.markdown('''> Displaying text using markdown :pencil2:''')
st.header('This is header', anchor=None)
st.subheader('This is subheader')
st.caption('This is caption')
st.text('This is some text.')
st.latex(r'''
a^2 + b^2 = \lparen a +b \rparen ^2
''')
code = '''void print(){
    printf("Hello Streamlit!");
    }'''

st.code(code, language = 'c')