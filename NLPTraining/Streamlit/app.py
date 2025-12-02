import streamlit as st
import pandas as pd
import numpy as np

st.title("creating my first app using streamlit")
name = st.text_input("enter your name")
s1 = st.text_input("subject")  
age = st.number_input("enter your age")

data = pd.DataFrame(
    np.random.randn(10, 3), columns =  ['a', 'b', 'c'])
st.line_chart(data)
st.bar_chart(data)

if st.button("submit"): 
    st.write(f"welcome to the app! my name is {name} and learning {s1} and my age is {age}")
