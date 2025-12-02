import streamlit as st
import pandas as pd
import io

st.title("Data Cleaning Web App with Pandas")

st.markdown("""
Upload your data file (CSV or Excel) using the widget below. 
The app will perform basic data cleaning operations and display the results.
""")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    st.success("File uploaded successfully!")
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

  
    @st.cache_data # Cache the cleaning results for performance
    def clean_data(data_frame):
        cleaned_df = data_frame.dropna()
        cleaned_df.columns = [col.lower().replace(' ', '_') for col in cleaned_df.columns]
        return cleaned_df


    if st.button("Clean and Process Data"):
        st.subheader("Cleaning Data...")
        cleaned_df = clean_data(df.copy())

       
        st.subheader("Cleaned Data Result")
        st.write(f"Original shape: {df.shape}, Cleaned shape: {cleaned_df.shape}")
        st.dataframe(cleaned_df)

       
        csv = cleaned_df.to_csv(index=False)
        st.download_button(
            label="Download Cleaned Data as CSV",
            data=csv,
            file_name='cleaned_data.csv',
            mime='text/csv',
        )

else:
    st.info("Please upload a file to begin the data cleaning process.")
