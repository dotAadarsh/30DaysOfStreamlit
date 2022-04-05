
# 30DaysOfStreamlit | Day-3

## Code
```
import streamlit as st
st.header('st.button')
if st.button('Hello'):
	st.write('Hi there, Its aadarsh here. Have a good day!')
else:
	st.write('Say hello by tapping the button')
```
## Explanation
Importing the `streamlit` library to  create the Streamlit app
> import streamlit as st

creating a header text for the app

> st.header('st.button')

Using the conditional statements `if` and `else` for printing alternative messages

```
if st.button('Hello'):
	st.write('Hi there, Its aadarsh here. Have a good day!')
else:
	st.write('Say hello by tapping the button')
```
`st.button()` function accepts the `label` input argument of `Hello`, which is the text that the button displays.

`st.write` function is used to print text messages

## Fire up the command line terminal
> streamlit run streamlit_app.py

## Result

![day3](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-1.PNG)