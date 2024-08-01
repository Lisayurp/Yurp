import streamlit as st
import re

st.title("KidzCareHub")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define pairs of patterns and responses
pairs = [
    (r"my head hurts(.*)", "You should take some painkillers and rest. If it persists, consult a doctor."),
    (r"(.*) fever", "You should take some rest, stay hydrated, and monitor your temperature. Consult a doctor if necessary."),
    (r"(.*) cough", "You may have a cold or another respiratory issue. Rest and drink fluids. See a doctor if symptoms persist."),
    (r"(.*) stomach", "Avoid heavy meals and try drinking herbal tea. If the pain is severe or persists, consult a doctor."),
    (r"(.*) tired(.*)", "Make sure you're getting enough rest and managing stress. If fatigue continues, consult a healthcare professional."),
    (r"(.*) advice(.*)", "I'm not a doctor, but it's important to consult a healthcare professional for medical advice."),
    (r"quit", "Thank you. Take care!")
]

# Function to respond to user input based on defined patterns
def respond(user_input):
    user_input = user_input.lower()
    for pattern, response in pairs:
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I didn't understand that. Can you please provide more details?"

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = respond(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(f"Rhea: {response}")
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": f"Rhea: {response}"})

# Custom CSS for background gradient
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #4169e1, #ffa07a, #ffffe0);
        color: #333;
        font-family: Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)
