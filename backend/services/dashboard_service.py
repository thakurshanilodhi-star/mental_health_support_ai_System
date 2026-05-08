# Dashboard stats

from backend.models.session_model import get_sessions

def get_total_study_time(user_id):
    sessions = get_sessions(user_id)

    total = 0
    for s in sessions:
        total += s["duration"]

    return total