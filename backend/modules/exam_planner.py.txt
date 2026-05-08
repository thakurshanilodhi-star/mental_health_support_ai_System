import streamlit as st
from backend.services.exam_service import create_exam_plan

def show():
    st.header("📝 Exam Planner")

    subject = st.text_input("Enter Subject")

    if st.button("Generate Exam Plan"):
        if subject:
            plan = create_exam_plan(subject)

            st.subheader("Exam Plan:")
            for p in plan:
                st.write("• " + p)