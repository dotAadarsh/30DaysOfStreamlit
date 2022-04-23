import streamlit as st

st.title('Day - 22 | st.form')

st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.write('**Order your coffee**')

    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta', 'Liberica', 'Excelsa'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    

    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')

st.header('2. Example of object notation')

form = st.form('my_form_2') 
selected_val = form.slider('Select a value', min_value=10, max_value=100)
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)

st.header('3. Columns inside forms')
with st.form('my_form_3'):
        col1, col2= st.columns(2)
        
        with col1:
            st.selectbox('Mode of payment', ['COD', 'Debit Card', 'Credit card'])
        with col2:
            st.text_area('Address', ' Rick Sanchez , No: 101, Dimension C-131')
        
        submitted = st.form_submit_button('Submit')

