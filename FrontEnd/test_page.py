import streamlit as st

st.write("Hello World")

if st.button("Hello"):
    st.experimental_rerun()
    
