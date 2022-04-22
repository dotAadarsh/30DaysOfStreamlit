# 30DaysOfStreamlit | Day-21

## st.progress
 `st.progress`  displays a progress bar that updates graphically as the iteration progresses.

*Example code*
```
a = st.button('click to execute')
if a ==True:
	progress_bar= st.progress(0)
	for percent_Complete in  range(100):
	time.sleep(0.05)
	progress_bar.progress(percent_Complete)
st.balloons()
```
Reference - [Streamlit Docs | st.progress](https://docs.streamlit.io/library/api-reference/status/st.progress)


## Result
![day21](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-21.PNG)