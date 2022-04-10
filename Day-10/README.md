# 30DaysOfStreamlit | Day-10

## st.selectbox
  
[st.selectbox](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox) - Display a select widget.
> st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)

*Example*
``` 
option = st.selectbox(
             'Select your job type',
             ('Internship', 'Part-time', 'Full-time',),
             index = 1,
             help = 'Choose your job type to filter the result',
             disabled=0,
             )
             
st.write('Your job type is ', option)
```
## Result
![day10](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-10.png)