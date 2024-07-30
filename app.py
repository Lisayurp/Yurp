import streamlit as st

st.title("KidzCareHub ChatBot")
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to KidzCareHub.")

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    
import re

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
    user_input = user_input.lower()# Convert input to lowercase for case-insensitive matching
    for pattern, response in pairs:
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I didn't understand that. Can you please provide more details?"

def chatbot():
    st.write("Hi, I'm your medical assistant. How can I help you today?")
    

# Example conversation loop

    # Text input for user
    user_input = st.text_input("You:")
    
    # Check if user wants to quit
    if user_input.lower() == "quit":
        st.write("Chatbot: Thank you. Take care!")
    else:
        # Get response based on user input
        response = respond(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
            
