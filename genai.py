import openai
openai.api_key = "xxxx"
def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
print("Waiting for input...")
user_input = input("Ask me anything: ")
print(generate_text(user_input))
