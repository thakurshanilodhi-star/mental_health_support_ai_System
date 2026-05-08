import streamlit as st
from backend.services.pyq_service import analyze_pyq

def show():
    st.header("📂 PYQ Analyzer")

    text = st.text_area("Paste Previous Year Questions")

    if st.button("Analyze"):
        if text:
            result = analyze_pyq(text)
            st.write(result)