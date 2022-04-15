import streamlit as st 
import pandas as pd 
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# streamlit_pandas_profiling component
st.header('streamlit_pandas_profiling')
df = pd.read_csv('/workspace/30DaysOfStreamlit/asserts/Day-4 Dataset/All_Comments_Final.csv')
pr = df.profile_report() 
st_profile_report(pr)