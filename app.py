import streamlit as st
import openai

# Initialize the OpenAI API with your API key
openai.api_key = 'sk-4Yrq0ICDnFpHbFhP7qaEAV97-HiEBQDyEash8AjxVVT3BlbkFJ4DOsXwAVLGgDGFjCQzL0NlKwDV6YFN_sE224DQLlgA'

def get_response(data_description, question):
    # Combine the data description and question into a single prompt
    prompt = f"""
    You are a pediatric care assistant named Rhea. Here is your background:
    {data_description}
    
    Based on this information, please answer the following question: {question}
    """
    
    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can change this to another model if needed
        messages=[
            {"role": "system", "content": "You are a helpful pediatric care assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract the response text
    return response.choices[0].message['content'].strip()

# Streamlit app
st.title("KidzCareHub")

data_description = """
Welcome to KidzCareHub, your trusted pediatric care assistant. I'm Rhea, here to provide you with helpful information and advice on your child's health, nutrition, development, and well-being. Whether you have questions about common childhood illnesses, developmental milestones, or general parenting tips, I'm here to help guide you with reliable information. Please remember, while I strive to offer accurate and helpful guidance, it's always best to consult with a healthcare professional for medical advice and treatment.
"""

question = st.text_input("Enter A Question")

if st.button("Get Answer"):
    if question:
        answer = get_response(data_description, question)
        st.write(answer)
    else:
        st.write("Please enter a question.")
