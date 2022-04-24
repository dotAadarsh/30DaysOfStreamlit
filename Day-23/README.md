
# 30DaysOfStreamlit | Day-23

## st.experimental_get_query_params

`st.experimental_get_query_params()` - Return the query parameters that is currently showing in the browser's URL bar.

### Function signature
> st.experimental_get_query_params()

*Example*
Let's say the user's web browser is at http://localhost:8501/?search_query=streamlit&type=playlist. Then, you can get the query parameters using the following:
```python
st.experimental_get_query_params()
{"search_query": ["streamlit"], "type": ["playlist"]}
```
Reference - [Streamlit Docs | st.experimental_get_query_params](https://docs.streamlit.io/library/api-reference/utilities/st.experimental_get_query_params)

## Result

![day23](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-23.PNG)