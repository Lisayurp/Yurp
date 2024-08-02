import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set up the page
st.set_page_config(page_title="KidzCareHub", page_icon="🏥", layout="wide")

# Initialize OpenAI LLM
llm = OpenAI(api_key='sk-None-JeDt7WpRoaTJpWXRCeGST3BlbkFJDiaYTqLYuPl7UPmgIzCS')  # Replace with your actual API key

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a pediatric care assistant named KidzCareHub. Answer the following question about child health, development, nutrition, or safety: {question}"
)

# Create an LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

st.title("🌟 Welcome to KidzCareHub! 🌟")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("I'm here to assist you"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response using OpenAI
    response = chain.run(question=prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(f"Rhea: {response}")
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": f"Rhea: {response}"})

# Sidebar with additional information
st.sidebar.title("About Rhea")
st.sidebar.info(
    "KidzCareHub is your comprehensive digital pediatric care assistant. "
    "Ask questions about child health, development, nutrition, safety, and more. "
    "Remember, this app provides general information and should not replace professional medical advice."
)

try:
    response = chain.run(question=prompt)
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    return
    
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
