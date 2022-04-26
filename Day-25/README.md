# 30DaysOfStreamlit | Day-25

## st.session_state

[st.session_state](https://docs.streamlit.io/library/api-reference/session-state) - a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks.
*Example*
```
import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)
```
### References 
- [st.session_state](https://docs.streamlit.io/library/api-reference/session-state) 
- [Add statefulness to apps](https://docs.streamlit.io/library/advanced-features/session-state)

## Result

![day25](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-25.PNG)