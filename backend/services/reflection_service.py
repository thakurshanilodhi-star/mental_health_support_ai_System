# Reflection save karega

from backend.models.reflection_model import save_reflection

def add_reflection(session_id, focus, distraction, clarity, next_step):
    save_reflection(session_id, focus, distraction, clarity, next_step)
    return "Reflection Saved"