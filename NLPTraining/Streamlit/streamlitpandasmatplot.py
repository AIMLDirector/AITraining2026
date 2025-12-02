import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import altair as alt

st.title("Upload, Clean, and Visualize Data (Matplotlib)")

@st.cache_data
def load_and_clean_data(uploaded_file):
    """
    Loads an uploaded CSV file, drops rows with missing values,
    and returns a cleaned DataFrame.
    """
    try:
       
        df = pd.read_csv(uploaded_file)
        cleaned_df = df.dropna()
        cleaned_df.columns = [col.strip().lower().replace(' ', '_') for col in cleaned_df.columns]
        return cleaned_df
    except Exception as e:
        st.error(f"An error occurred during data loading or cleaning: {e}")
        return None

# --- UI: File Uploader ---
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df_cleaned = load_and_clean_data(uploaded_file)
    
    if df_cleaned is not None and not df_cleaned.empty:
        st.success("Data uploaded and cleaned successfully!")
        
        st.sidebar.subheader("Data Summary")
        st.sidebar.write(f"Rows: {df_cleaned.shape[0]}")
        st.sidebar.write(f"Columns: {df_cleaned.shape[1]}")

        # Use Tabs for a clean layout
        tab1, tab2 = st.tabs(["Cleaned Data Table", "Matplotlib Visualization"])

        with tab1:
            st.subheader("Cleaned Data Preview")
            st.dataframe(df_cleaned)

        with tab2:
            st.subheader("Visualization Setup")
            available_columns = df_cleaned.columns.tolist()
            if len(available_columns) >= 2:
                x_col = st.selectbox("Select Column for X-Axis (Categories)", available_columns)
                y_col = st.selectbox("Select Column for Y-Axis (Values/Metrics)", available_columns)
                
                # We need numeric data for the Y-axis plot. Check and aggregate.
                try:
                    plot_data = df_cleaned.groupby(x_col)[y_col].mean().reset_index()
                    fig, ax = plt.subplots(figsize=(10, 6))
                    ax.bar(plot_data[x_col], plot_data[y_col], color='skyblue')
                    ax.set_xlabel(x_col.capitalize())
                    ax.set_ylabel(f'Average {y_col.capitalize()}')
                    ax.set_title(f'Average {y_col.capitalize()} per {x_col.capitalize()}')
                    plt.xticks(rotation=45, ha='right') 
                    st.pyplot(fig)

                except TypeError:
                    st.warning(f"Please select appropriate columns. '{y_col}' must contain numeric data to calculate an average.")
                except Exception as e:
                    st.error(f"Could not generate plot: {e}")
            else:
                st.warning("Please upload a file with at least two columns to visualize data.")

    elif df_cleaned is not None and df_cleaned.empty:
        st.warning("The cleaning process resulted in an empty DataFrame. Check your data or cleaning logic (e.g., you dropped all rows).")

else:
    st.info("Upload a CSV file using the widget above to start the analysis.")
