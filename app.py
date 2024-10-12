import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to generate chatbot response based on prompt
def generate_text():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state['messages'],  # Maintain the entire conversation
        max_tokens=60  # Adjust token length as needed
    )
    return response.choices[0].message['content'].strip()

# Initialize session state for storing conversation history
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a well-known nutritionist and are aware of all the benefits of each and every food intake."}
    ]

# Streamlit app layout
st.title("Nutrition Chatbot")
st.write("Ask the chatbot about the benefits of different foods and nutrition-related questions!")

# User input box
user_input = st.text_input("You:", placeholder="Ask me anything about nutrition or food benefits...")

# Check if the user has entered something
if user_input:
    # Append the user's message to the session state
    st.session_state['messages'].append({"role": "user", "content": user_input})

    # Generate the chatbot response
    response = generate_text()

    # Append the chatbot's response to the session state
    st.session_state['messages'].append({"role": "assistant", "content": response})

    # Clear the input field after submission by setting the query parameter
    st.experimental_set_query_params(user_input="")

# Display the conversation history
for msg in st.session_state['messages']:
    if msg['role'] == 'user':
        st.write(f"You: {msg['content']}")
    elif msg['role'] == 'assistant':
        st.write(f"Chatbot: {msg['content']}")
