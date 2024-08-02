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

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFB6C1;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        color: #FF1493;
        text-align: center;
        font-size: 3em;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(255,20,147,0.3);
    }
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 20px !important;
        padding: 15px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 4px 6px rgba(255,20,147,0.2);
    }
    .stChatMessage [data-testid="stChatMessageContent"] {
        background-color: transparent !important;
        color: #333;
        font-size: 1.1em;
    }
    .stChatMessage [data-testid="stChatMessageAvatar"] {
        background-color: #FF69B4 !important;
    }
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 25px;
        padding: 12px 20px;
        font-size: 1.1em;
        border: 2px solid #FF69B4;
    }
    .stSidebar {
        background-color: rgba(255, 192, 203, 0.2);
        padding: 20px;
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
 
