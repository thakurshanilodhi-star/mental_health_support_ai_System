# Adaptive logic (simple)

def adjust_plan(focus_score):
    if focus_score < 3:
        return "Reduce workload"
    else:
        return "Increase difficulty"