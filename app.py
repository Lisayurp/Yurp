import streamlit as st

st.title("Welcom to KidzCareHub")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! I'm Rhea, I will be your pediatric assitant.")

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

prompt = st.chat_input("What's up") 

if prompt: 
    response = respond(prompt) 
    st.write(f"Rhea: {response}") 
user_input = input(f"user:" )



    # Check if user wants to quit
if user_input.lower() == "quit":
        st.write("Rhea: Thank you. Take care!")
else:
        # Get response based on user input
        response = respond(user_input)
        st.write("Rhea:", response)

if __name__ == "__main__":
    chatbot()

    
