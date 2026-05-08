import streamlit as st
from backend.models.session_model import get_sessions

def show():
    st.header("📚 Study Log")

    sessions = get_sessions(1)

    if sessions:
        for s in sessions:
            st.write(f"Subject: {s['subject']} | Duration: {s['duration']} min")
    else:
        st.write("No sessions found")