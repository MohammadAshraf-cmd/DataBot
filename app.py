import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to generate chatbot response
def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state['messages'],  # Use session messages for continuous conversation
        max_tokens=60  # Adjust token length as needed
    )
    return response.choices[0].message['content'].strip()

# Initialize session state for storing conversation history
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a well-read journalist and are aware of the recent performance of India in the Paralympics 2024."}
    ]

# Streamlit app layout
st.title("Shaktiman Chatbot")
st.write("Let's Start!")

# User input box
user_input = st.text_input("You:", placeholder="Ask me anything about India's Paralympics performance...")

# Check if user has entered something
if user_input:
    # Append user message to session state
    st.session_state['messages'].append({"role": "user", "content": user_input})

    # Generate chatbot response
    response = generate_text(user_input)

    # Append chatbot response to session state
    st.session_state['messages'].append({"role": "assistant", "content": response})

    # Display the conversation history
    for msg in st.session_state['messages']:
        if msg['role'] == 'user':
            st.write(f"You: {msg['content']}")
        elif msg['role'] == 'assistant':
            st.write(f"Chatbot: {msg['content']}")
