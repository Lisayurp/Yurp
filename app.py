import streamlit as st
import re

st.set_page_config(page_title="Rhea", page_icon="🏥", layout="wide")

st.title("🌟!Welcome to KidzCareHub!🌟")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define pairs of patterns and responses
pairs = [
    (r"check up", "Infants should have check-ups at 2-4 weeks, 2, 4, 6, 9, and 12 months. Toddlers typically need visits at 15, 18, and 24 months, then annually after age 3."),
    (r"developmental milestones", "Developmental milestones include physical, cognitive, and social-emotional skills such as sitting up, walking, talking, and interacting with others. Specific milestones vary by age."),
    (r"normal development", "Regular check-ups with your pediatrician can monitor development. If you have concerns, discuss them with your pediatrician who may recommend evaluations or referrals to specialists."),
    (r"vaccinations", "Vaccination schedules vary but typically include vaccines for diseases like hepatitis, polio, measles, mumps, rubella, chickenpox, and HPV. Your pediatrician can provide a schedule based on age and health."),
    (r"sleep habits", "Establish a consistent bedtime routine, ensure a sleep-conducive environment, limit screen time before bed, and encourage regular sleep and wake times."),
    (r"balanced diet", "A balanced diet includes a variety of fruits, vegetables, whole grains, proteins (like meat, beans, and nuts), and dairy. Limit sugars and unhealthy fats."),
    (r"fruits and vegetables", "Offer a variety of colorful fruits and vegetables, make them easily accessible, involve your child in meal preparation, and model healthy eating habits yourself."),
    (r"foods to avoid", "Avoid giving young children foods that are choking hazards, such as whole nuts and hard candies. Also, limit sugary drinks and high-sodium foods."),
    (r"water intake", "Children should drink water throughout the day. The amount varies by age, but generally, aim for about 1-1.5 liters for young children and more for older children and teens."),
    (r"picky eater", "Continue to offer a variety of foods without pressuring them to eat. Make mealtime pleasant, involve your child in food choices, and be patient."),
    (r"quit", "Thank you for using KidzCareHub. Take care and stay healthy!")
]

# Function to respond to user input based on defined patterns
def respond(user_input):
    user_input = user_input.lower()
    for pattern, response in pairs:
        if re.search(pattern, user_input):
            return response
    return "I'm not sure about that specific topic. Could you try asking about check-ups, development, vaccinations, sleep, diet, or other common pediatric care topics?"

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
    "KidzCareHub is your friendly pediatric care assistant. "
    "Ask questions about child health, development, nutrition, and more. "
    "Remember, this app provides general information and should not replace professional medical advice."
)

# Custom CSS for a new design
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        font-size: 3em;
        margin-bottom: 30px;
    }
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 15px !important;
        padding: 15px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stChatMessage [data-testid="stChatMessageContent"] {
        background-color: transparent !important;
        color: #34495e;
        font-size: 1.1em;
    }
    .stChatMessage [data-testid="stChatMessageAvatar"] {
        background-color: #3498db !important;
    }
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        padding: 10px 15px;
        font-size: 1.1em;
    }
    .stSidebar {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
