import streamlit as st
from backend.services.focus_service import end_session

def show():
    st.header("⏱ Focus Session")

    subject = st.text_input("Enter Subject")
    duration = st.number_input("Duration (minutes)", min_value=1)

    if st.button("Complete Session"):
        end_session(1, subject, duration)
        st.success("Session Saved Successfully")