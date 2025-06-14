import os
import openai

def main():
    prompt = input("Enter your prompt: ")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    print("AI response:", response.choices[0].message.content)

if __name__ == "__main__":
    main()
