import streamlit as st

st.title("Welcome to my first Streamlit App")
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to KidzCareHub.")
    
import re

# Define pairs of patterns and responses
pairs = [
    (r"my head hurts(.*)", "You should take some painkillers and rest. If it persists, consult a doctor."),
    (r"(.*) fever", "You should take some rest, stay hydrated, and monitor your temperature. Consult a doctor if necessary."),
    (r"(.*) cough", "You may have a cold or another respiratory issue. Rest and drink fluids. See a doctor if symptoms persist."),
    (r"(.*) stomachache", "Avoid heavy meals and try drinking herbal tea. If the pain is severe or persists, consult a doctor."),
    (r"(.*) tired(.*)", "Make sure you're getting enough rest and managing stress. If fatigue continues, consult a healthcare professional."),
    (r"(.*) advice(.*)", "I'm not a doctor, but it's important to consult a healthcare professional for medical advice."),
    (r"quit", "Thank you. Take care!")
]

# Function to respond to user input based on defined patterns
def respond(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching
    for pattern, response in pairs:
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I didn't understand that. Can you please provide more details?"

# Example conversation loop
def chatbot():
    st.write("Hi, I'm your medical assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            st.write("Chatbot: Thank you. Take care!")
            break
        else:
            st.write("Chatbot:", respond(user_input))

if __name__ == "__main__":
    chatbot()
