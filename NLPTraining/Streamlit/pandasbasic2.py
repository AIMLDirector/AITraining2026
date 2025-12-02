import streamlit as st
import pandas as pd

st.title("Pandas DataFrame Example")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("DataFrame Loaded:",df)

if st.checkbox("Remove the duplicate values"):
    if uploaded_file:
        df = df.drop_duplicates()
        st.write("DataFrame after removing duplicates:", df)
    else:
        st.write("Please upload a CSV file first.")

if st.checkbox("Remove the row with null values"):
    if uploaded_file:
        df = df.dropna()
        st.write("DataFrame after removing rows with null values:", df)
    else:
        st.write("Please upload a CSV file first.")
    
    cleaned_file = df.to_csv(index=False).encode('utf-8')
    st.download_button( label = "download the csv file", data = cleaned_file, file_name = 'cleaned_data.csv', mime = 'text/csv' )

# df = pd.read_csv(uploaded_file)
# df = df.drop_duplicates()
# df = df.dropna()
# cleaned_file = df.to_csv(index=False).encode('utf-8')
# st.download_button( label = "download the csv file", data = cleaned_file, file_name = 'cleaned_data.csv', mime = 'text/csv' )
