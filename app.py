import streamlit as st
import re
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(api_key = 'sk-None-1Sed5BjJFyqRO5MCNbETT3BlbkFJRYElnAB7mQO0csnjMLbp')

st.set_page_config(page_title="KidzCareHub", page_icon="🏥", layout="wide")

st.title("🌟!Welcome to KidzCareHub!🌟")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []



# Function to respond to user input based on defined patterns
def respond(user_input):
    user_input = user_input.lower()
    for pattern, response in pairs:
        if re.search(pattern, user_input):
            return response
    return "I'm not sure about that specific topic. Could you try asking about common pediatric care topics like health, nutrition, development, or safety?"

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask a question about pediatric care"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = respond(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(f"KidzCareHub: {response}")
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": f"KidzCareHub: {response}"})

# Sidebar with additional information
st.sidebar.title("About KidzCareHub")
st.sidebar.info(
    "KidzCareHub is your comprehensive digital pediatric care assistant. "
    "Ask questions about child health, development, nutrition, safety, and more. "
    "Remember, this app provides general information and should not replace professional medical advice."
)

# Custom CSS for design
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #FFD1DC 0%, #FFF0F5 100%);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    h1 {
        color: #FF69B4;
        text-align: center;
        font-size: 3em;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(255,105,180,0.3);
    }
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 20px !important;
        padding: 15px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 4px 6px rgba(255,105,180,0.2);
        border: 2px solid #FFB6C1;
    }
    .stChatMessage [data-testid="stChatMessageContent"] {
        background-color: transparent !important;
        color: #8B4513;
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
        border: 2px solid #FFB6C1;
    }
    .stSidebar {
        background-color: rgba(255, 192, 203, 0.2);
        padding: 20px;
        border-radius: 15px;
    }
    .stButton > button {
        background-color: #FF69B4;
        color: white;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 1.1em;
        border: none;
        box-shadow: 0 4px 6px rgba(255,105,180,0.2);
    }
    .stButton > button:hover {
        background-color: #FF1493;
    }
    </style>
    """,
    unsafe_allow_html=True
)

