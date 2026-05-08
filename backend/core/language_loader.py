# Language loader (basic demo version)

import json

def load_language(lang="en"):
    try:
        with open(f"backend/languages/{lang}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}