import requests

#  Apni API key yaha paste karo
API_KEY = "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"


def generate_ai_response(prompt):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                #  FREE MODEL (no cost)
                "model": "openrouter/free",

                "messages": [
                    {
                        "role": "user",
                        "content": f"Give a helpful study plan for: {prompt}"
                    }
                ]
            }
        )

        data = response.json()

        #  Safe extraction
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"].strip()

        return None

    except Exception as e:
        print("AI ERROR:", e)
        return None