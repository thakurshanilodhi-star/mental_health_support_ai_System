import requests

#  Apni API key yaha paste karo
API_KEY = ""


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