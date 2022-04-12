
# 30DaysOfStreamlit | Day-11

  

## st.multiselect

[st.multiselect](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect) - Display a multiselect widget.

> st.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)

  

*Example*

```
options = st.multiselect(
                    'Select the content type',
                    ['Coding questions', 'Video', 'Reading', 'Interactive tutorials', 'Online courses', 'Quiz'],
                    ['Video', 'Quiz', 'Reading'],
                    disabled = 0,help = "help"
                    )
```
## Result

![day11](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-11.png)