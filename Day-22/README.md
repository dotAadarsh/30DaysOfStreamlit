
# 30DaysOfStreamlit | Day-22

## st.form

`st.form` - creates a form that batches elements together with a "Submit" button.

### Function signature
> st.form(key, clear_on_submit=False)

*Example code*
```python
# Using the "with" syntax
with st.form(key='my_form'):
	text_input = st.text_input(label='Enter some text')
	submit_button = st.form_submit_button(label='Submit')
```
Reference - [Streamlit Docs | st.form](https://docs.streamlit.io/library/api-reference/control-flow/st.form)

## Result

![day22](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-22.PNG)