# Focus session handle karega

from backend.models.session_model import save_session

def end_session(user_id, subject, duration):
    save_session(user_id, subject, duration)
    return "Session Saved"