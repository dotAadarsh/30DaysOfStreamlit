import streamlit as st
import numpy as np
import pandas as pd
from time import time
from sqlalchemy.orm import sessionmaker

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(200000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1)
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(200000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1)
st.info(b1-b0)

st.header('st.experimental_memo')
# Function decorator to memoize function executions.

c0 = time()
@st.experimental_memo
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)

f10 = factorial(10)
c1= time()

f9 = factorial(9)  # Returns instantly!
c2 = time()

st.write(f'Factorial of 10 is {f10} with time {c1}')
st.write(f'Factorial of 9 is {f9} with time {c2}')
st.write(f9)

