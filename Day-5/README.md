  

# 30DaysOfStreamlit | Day-5

## st.write
> st.write('Hello, *streamlit* :wave:')
## st.markdown
> st.markdown('''> Displaying text using markdown :pencil2:''')
## st.header
> st.header('This is header', anchor=None)
## st.subheader
> st.subheader('This is subheader')
## st.caption
> st.caption('This is caption')
## st.text
> st.text('This is some text.')
## st.latex
```
st.latex(r'''
a^2 + b^2 = \lparen a +b \rparen ^2
''')
```
## st.code
> code = '''void print(){
printf("Hello Streamlit!");
}'''
st.code(code, language = 'c')

## Result

  

![day5](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-5.PNG)