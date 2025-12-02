import streamlit as st


st.markdown("<h1 style='text-align: center; color: #FF5733;'>Custom HTML Title (Orange)</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='color: green;'>Another Custom Title (Green)</h1>", unsafe_allow_html=True)

st.markdown("""
<style>
.gradient-title {
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 42px;
    font-weight: bold;
}
</style>
<h1 class='gradient-title'>Gradient Streamlit Title</h1>
""", unsafe_allow_html=True)