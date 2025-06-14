# My AI Project

This is a simple Python script that uses OpenAI's GPT-3.5 API to generate text responses.  
Perfect for demonstrating basic AI tool integration!

## How it works
- Takes a prompt from the user
- Sends it to OpenAI API
- Prints the AI's response

## Usage
1. Clone the repo
2. Install requirements: `pip install openai`
3. Set your OpenAI API key as an environment variable:  
   `export OPENAI_API_KEY=your_api_key_here`
4. Run the script: `python gpt_example.py`

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


