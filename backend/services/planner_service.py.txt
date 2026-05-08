from backend.core.llm_engine import generate_ai_response


def generate_plan(goal):

    ai_response = generate_ai_response(
        f"Create a short and simple study plan for {goal}"
    )

    # ✅ If AI works
    if ai_response:
        return ai_response

    # 🔥 Fallback (AI fail)
    return (
        f"Start with basics of {goal}. "
        f"Then practice questions and revise regularly."
    )