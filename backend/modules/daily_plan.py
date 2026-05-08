import streamlit as st
from backend.services.planner_service import generate_plan
from backend.core.voice_engine import speak


def show():
    st.title("Daily Study Planner")

    goal = st.text_input("Enter your study goal")

    if st.button("Generate Plan", key="generate"):

        if not goal:
            st.warning("Please enter a goal")
            return

        plan = generate_plan(goal)

        st.success("Study Plan Ready")
        st.write(plan)

        # 🔊 SAFE VOICE (IMPORTANT)
        try:
            speak(plan)
        except:
            pass