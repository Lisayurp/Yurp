import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "your-api-key-here"

def get_health_advice(symptom):
    prompt = f"Provide child-friendly advice for a parent whose child is experiencing {symptom}. Include when to see a doctor."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Streamlit interface
st.title("KidzCareHub")
st.write("Get friendly pediatric health advice")

symptom = st.text_input("What symptom is your child experiencing?")

if st.button("Get Advice"):
    if symptom:
        with st.spinner("Generating advice..."):
            advice = get_health_advice(symptom)
        st.write(advice)
    else:
        st.write("Please enter a symptom.")

st.sidebar.write("Note: This app provides general advice. Always consult a healthcare professional for medical concerns.")
