import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

class Decrip: 
    def __init__(self):
        pass

    def get_all_possibilities(self):
        code = input("Your encrypted code: ")
        letters = "abcdefghijklmnopqrstuvwxyz"
        pos = []
        
        for i in range(26):
            trying = ""
            for char in code.lower():
                if char in letters:
                    pos_used = letters.find(char)
                    new_pos = (pos_used - i) % 26
                    trying += letters[new_pos]
                else:
                    trying += char
            pos.append(f"Shift {i}: {trying}")
        return "\n".join(pos)

load_dotenv()

def generate():
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    decoder = Decrip()
    all_shifts = decoder.get_all_possibilities()

    model_id = "gemini-3-flash-preview"

    prompt = f"""
    The following is a list of 26 possible Caesar cipher decryptions for a piece of text.
    Please identify:
    1. Which 'Shift' contains the correct, readable English text?
    2. What does the message say?
    3. Explain the shift logic used.

    Possibilities:
    {all_shifts}
    """

    response = client.models.generate_content(
        model=model_id,
        contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
    )

    print("\n--- AI Analysis ---")
    print(response.text)

if __name__ == "__main__":
    generate()