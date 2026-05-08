import streamlit as st

# ---------------- IMPORT MODULES ----------------
from backend.modules import (
    daily_plan,
    focus_timer,
    dashboard,
    exam_planner,
    study_log,
    pyq_upload
)

# Voice import
from backend.core.voice_engine import speak

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Academic and Habit Assistant",
    layout="wide"
)

# ---------------- LOGO (TOP CENTER) ----------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("logo.png", width=250)

# ---------------- TITLE ----------------
st.title("Smart Academic and Habit Assistant")

# ---------------- ASSISTANT MESSAGE ----------------
message = (
    "Hello, I am your Smart Academic and Habit Assistant.\n\n"
    "I will help you improve:\n"
    "- Study planning\n"
    "- Focus and consistency\n"
    "- Discipline and execution\n\n"
    "Let us get started."
)

st.write(message)

# ---------------- VOICE (ONLY ONCE) ----------------
if "spoken" not in st.session_state:
    speak(message)
    st.session_state["spoken"] = True

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Daily Plan",
        "Focus Session",
        "Dashboard",
        "Exam Planner",
        "Study Log",
        "PYQ Analyzer"
    ]
)

# ---------------- ROUTING ----------------
if page == "Daily Plan":
    daily_plan.show()

elif page == "Focus Session":
    focus_timer.show()

elif page == "Dashboard":
    dashboard.show()

elif page == "Exam Planner":
    exam_planner.show()

elif page == "Study Log":
    study_log.show()

elif page == "PYQ Analyzer":
    pyq_upload.show()