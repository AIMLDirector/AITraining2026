import streamlit as st

st.title('Creating my First Streamlit App')
st.write('Welcome to the app! Here is some basic text.')

user_input = st.text_input("Enter your name", "Type your name here")
if user_input:
    st.write(f'Hello, {user_input}!')