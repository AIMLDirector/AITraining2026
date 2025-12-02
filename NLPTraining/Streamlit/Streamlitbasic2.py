import streamlit as st
import pandas as pd
import numpy as np

st.title('Creating a View for DataFrames in Streamlit')
st.write('Welcome to the app! Here is some basic text.')
data = {
    'Column A': [1, 2, 3, 4, 5],
    'Column B': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Column C': np.random.randn(5)
}
df = pd.DataFrame(data)
st.write("You can interact with the DataFrame above. Try sorting or filtering the data!")
st.markdown("<h3 style='text-align: center; color: #FF5733;'>You can interact with the DataFrame above. Try sorting or filtering the data!(Orange)</h3>", unsafe_allow_html=True)
# st.header("Interactive DataFrame Display")
st.dataframe(df)

st.header("Static Table Display")
st.table(df)

