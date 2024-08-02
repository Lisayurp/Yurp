import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set up the page
st.set_page_config(page_title="KidzCareHub", page_icon="🏥", layout="wide")

# Initialize OpenAI LLM
llm = OpenAI(api_key='sk-4Yrq0ICDnFpHbFhP7qaEAV97-HiEBQDyEash8AjxVVT3BlbkFJ4DOsXwAVLGgDGFjCQzL0NlKwDV6YFN_sE224DQLlgA')  # Replace with your actual API key

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
if user_input := st.chat_input("I'm here to assist you"):
    # Display user message in chat message container
    st.chat_message("user").markdown(user_input)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # Generate response using OpenAI
        response = chain.run(question=user_input)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(f"KidzCareHub: {response}")
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": f"KidzCareHub: {response}"})
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Sidebar with additional information
st.sidebar.title("About KidzCareHub")
st.sidebar.info(
    "KidzCareHub is your comprehensive digital pediatric care assistant. "
    "Ask questions about child health, development, nutrition, safety, and more. "
    "Remember, this app provides general information and should not replace professional medical advice."
)

# Custom CSS for design with pink background
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
