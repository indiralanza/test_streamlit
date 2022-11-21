import streamlit as st 

st.title("streamlit Forms & Submit Demo")

#with st.form(key = "form1"):
my_form = st.form(key = "form1")
name = my_form.text_input(label = "Enter the model name")
number = my_form.slider("Enter your age", min_value=10, max_value = 100 )
submit = my_form.form_submit_button(label = "Submit this form")

col1, col2 = st.columns(2)

with col1:
    with st.form('Form1'):
        st.selectbox('Select flavor', ['Vanilla', 'Chocolate'], key=1)
        st.slider(label='Select intensity', min_value=0, max_value=100, key=4)
        submitted1 = st.form_submit_button('Submit 1')

with col2:
    with st.form('Form2'):
        selectbox=st.selectbox('Select Topping', ['Almonds', 'Sprinkles'], key=2)
        slider=st.slider(label='Select Intensity', min_value=0, max_value=100, key=3)
        submitted2 = st.form_submit_button('Submit 2')
        if submitted2:
            st.write(selectbox, slider)

st.text(number)

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")


file_expander = st.sidebar.beta_expander(‘Expander Title’)
