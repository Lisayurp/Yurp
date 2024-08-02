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

# Define pairs of patterns and responses
pairs = [
    # General Health
    (r"vaccination", "The CDC recommends vaccinations like Hepatitis B, DTaP, Hib, IPV, MMR, Varicella, and others starting at birth and continuing through childhood."),
    (r"fever", "A fever is generally considered a temperature of 100.4°F (38°C) or higher. Monitor their temperature, you can use a digital thermometer for accurate readings. Ensure they stay hydrated, and use fever-reducing medications if necessary. Consult a doctor if the fever persists or is very high."),
    (r"bring (child|baby) to (doctor|pediatrician)", "Seek medical attention if your child has a high fever, difficulty breathing, persistent vomiting, rash, or is unusually lethargic."),
    (r"cold", "Encourage good hand hygiene, avoid close contact with sick individuals, and ensure your child receives their vaccinations."),

    # Nutrition
    (r"(what|how) (should|can) (my|a) toddler eat", "Offer a balanced diet with fruits, vegetables, whole grains, protein sources (meat, beans), and dairy."),
    (r"picky eater", "Yes, many children go through phases of picky eating. Encourage a variety of foods and model healthy eating habits."),
    (r"(when|age) (can|start) (child|baby) (drink|drinking) cow('s)? milk", "Cow's milk can typically be introduced after the age of 1, but it should not replace breast milk or formula entirely until later."),
    (r"(how much|amount of) water (should|drink|intake)", "Generally, children should drink about 5-7 cups of water daily, depending on age, activity level, and climate."),
    (r"(child|baby) (be )?allergic to (certain )?foods", "Yes, common food allergies include milk, eggs, peanuts, tree nuts, soy, wheat, fish, and shellfish. Consult an allergist for testing."),

    # Development
    (r"(age|when) (should|start) (child|baby) start walking", "Most children take their first steps between 9 and 15 months, but there's a wide range of normal development."),
    (r"encourage (child's|baby's) language development", "Read to your child, engage in conversation, sing songs, and encourage them to express themselves."),
    (r"signs of developmental delays", "Delays may include not meeting milestones in walking, talking, social interactions, or self-care skills. Consult a pediatrician if concerned."),
    (r"(when|age) (should|start) (child|baby) start school", "Most children start kindergarten around age 5, but readiness can vary. Check local school district requirements."),
    (r"(how much|amount of) screen time (is appropriate|should)", "The American Academy of Pediatrics recommends limiting screen time to one hour per day for children ages 2-5 and encouraging other activities."),

    # Behavior
    (r"handle (child's|baby's) tantrums", "Stay calm, acknowledge their feelings, and provide comfort. Try to redirect their attention or offer choices to help them regain control."),
    (r"(is it )?normal for children to be shy", "Yes, many children go through phases of shyness. Encourage social interactions without forcing them."),
    (r"discipline (my|a) child effectively", "Use positive reinforcement, set clear rules, and be consistent with consequences. Time-outs can be effective for younger children."),
    (r"strategies for managing a child's anxiety", "Talk openly about their fears, provide reassurance, establish routines, and consider relaxation techniques or professional help if needed."),
    (r"encourage (my|a) child to share", "Model sharing behavior, use role-playing, and praise them when they share."),

    # Common Illnesses
    (r"symptoms of strep throat", "Symptoms include sore throat, fever, red and swollen tonsils, and white patches on the throat. Consult a doctor for testing."),
    (r"treat (my|a) child's cold", "Ensure they rest, stay hydrated, and consider over-the-counter medications for symptom relief."),
    (r"(child|baby) has diarrhea", "Keep them hydrated with fluids and avoid sugary drinks. If diarrhea persists or is severe, contact a healthcare provider."),
    (r"signs of asthma in children", "Signs include coughing, wheezing, shortness of breath, and chest tightness, especially during physical activity or at night."),
    (r"prevent (my|a) child from getting lice", "Teach your child not to share hats, brushes, or personal items, and regularly check their scalp for signs of lice."),

    # Sleep
    (r"(how much|amount of) sleep (does|should) (my|a) child need", "Sleep needs vary by age, but toddlers typically need 11-14 hours, preschoolers 10-13 hours, and school-aged children 9-11 hours."),
    (r"(child|baby) (has|have) trouble sleeping", "Establish a bedtime routine, ensure a comfortable sleep environment, and limit screen time before bed."),
    (r"(safe|okay) for (my|a) child to sleep with a stuffed animal", "Yes, a stuffed animal can provide comfort. Just ensure it's safe and not a choking hazard for younger children."),
    (r"(when|age) can (my|a) child sleep in their own room", "Many children transition to their own room between 2 and 3 years old, but readiness can vary."),
    (r"(what is|about) sleep apnea (in children)?", "Sleep apnea is a condition where breathing stops and starts during sleep. Yes, children can have it, and symptoms include loud snoring and daytime sleepiness."),

    # Safety
    (r"keep (my|a) child safe in the car", "Use an age-appropriate car seat, ensure they are buckled in correctly, and follow state laws regarding car seat use."),
    (r"(when|age) (should|start) (my|a) child (use|start using) a booster seat", "Children should transition to a booster seat when they outgrow their forward-facing car seat, usually around age 4."),
    (r"childproof (my|a) home", "Secure furniture, cover outlets, use safety gates, and keep hazardous materials out of reach."),
    (r"signs of child abuse", "Signs can include unexplained injuries, changes in behavior, fear of going home, and regression in behavior or development."),
    (r"teach (my|a) child about stranger danger", "Teach them to recognize safe and unsafe situations, encourage them to trust their instincts, and practice scenarios with them."),

    # Mental Health
    (r"tell if (my|a) child is depressed", "Signs may include persistent sadness, withdrawal from activities, changes in appetite or sleep, and difficulty concentrating. Consult a professional if concerned."),
    (r"support (my|a) child's mental health", "Encourage open communication, validate their feelings, ensure they have healthy routines, and seek professional help if needed."),
    (r"(is it )?normal for children to experience anxiety", "Yes, many children experience anxiety, especially during transitions or stressful situations. Coping strategies and support can help."),
    (r"help (my|a) child manage stress", "Teach them relaxation techniques, encourage physical activity, and maintain open communication about their feelings."),
    (r"(when|if) (should I|to) seek help for (my|a) child's mental health", "If your child shows persistent signs of distress, such as significant mood changes, social withdrawal, or behavioral issues, consult a mental health professional."),

    # Chronic Conditions
    (r"(common )?symptoms of diabetes in children", "Symptoms include increased thirst, frequent urination, fatigue, and unexplained weight loss."),
    (r"manage (my|a) child's asthma", "Work with a doctor to create an asthma action plan, use prescribed medications, and avoid triggers."),
    (r"dietary changes (can|to) help manage (my|a) child's ADHD", "Focus on a balanced diet rich in fruits, vegetables, whole grains, lean proteins, and omega-3 fatty acids while limiting sugar and processed foods."),
    (r"(child|baby) has eczema", "Keep their skin moisturized, avoid known irritants, and consult a dermatologist for treatment options."),
    (r"help (my|a) child with allergies", "Identify and avoid allergens, have emergency medication available, and work with an allergist for management strategies."),

    # Common Concerns
    (r"(child|baby) has a rash", "Assess the rash, consider recent exposures (like new products or foods), and consult a doctor if it doesn't improve or if they have other symptoms."),
    (r"(when|if) (should I|to) be concerned about (my|a) child's growth", "If your child consistently falls below the growth chart or shows sudden changes in growth patterns, consult a pediatrician."),
    (r"(child|baby) (has|have) bad breath", "Ensure they practice good oral hygiene, stay hydrated, and consult a dentist if the problem persists."),
    (r"encourage (my|a) child to be active", "Provide opportunities for physical activity, make it fun, and be active together as a family."),
    (r"(when|age) (should|have) (my|a) child (have|get) their first dental visit", "The American Academy of Pediatric Dentistry recommends a dental visit by age 1 or within 6 months of the first tooth erupting."),

    # Seasonal Health
    (r"prevent (my|a) child from getting sick in winter", "Ensure they wash their hands frequently, stay warm, and receive their flu vaccine."),
    (r"(child|baby) has allergies during spring", "Limit outdoor activities during high pollen counts, keep windows closed, and consider allergy medications as advised by a doctor."),
    (r"protect (my|a) child from sunburn in summer", "Use sunscreen with at least SPF 30, have them wear protective clothing, and encourage shade during peak sun hours."),
    (r"(child|baby) gets a heat rash", "Keep the skin cool and dry, avoid tight clothing, and consult a doctor if it doesn't improve."),
    (r"help (my|a) child stay healthy during flu season", "Ensure they get vaccinated, practice good hygiene, and encourage a healthy diet to boost their immune system."),

    # Educational Concerns
    (r"help (my|a) child with homework", "Create a quiet study space, encourage a regular schedule, and be available to answer questions or provide guidance."),
    (r"(child|baby) is struggling in school", "Communicate with their teacher, assess for learning disabilities, and consider tutoring or additional support."),
    (r"encourage a love for reading", "Read together daily, provide a variety of books, and let your child choose their reading material."),
    (r"(when|age) (should I|to) start teaching (my|a) child about money", "You can start teaching basic concepts of money as early as age 4, gradually introducing more complex ideas as they grow."),
    (r"support (my|a) child's learning at home", "Create a supportive environment, provide resources, and encourage curiosity and exploration."),

    # Parenting Tips
    (r"foster independence in (my|a) child", "Allow them to make age-appropriate choices, encourage self-help skills, and praise their efforts."),
    (r"(what is|about) the importance of routine for children", "Routines provide structure, security, and predictability, which can help children feel safe and learn self-discipline."),
    (r"build (my|a) child's self-esteem", "Offer praise for their efforts, encourage them to try new things, and support them through challenges."),
    (r"teach (my|a) child to manage their emotions", "Model emotional regulation, teach them to identify their feelings, and encourage healthy coping strategies."),
    (r"(fun )?family activities (I can do|to do) with (my|a) child", "Go for walks, play board games, have movie nights, cook together, or explore nature."),

    # Health Screenings
    (r"key health screenings for children", "Key screenings include vision and hearing tests, developmental screenings, and blood pressure checks."),
    (r"(how often|frequency) (should|have) (my|a) child have check-ups", "Children should have regular check-ups at least once a year, with more frequent visits for specific health concerns."),
    (r"(what is|about) (the )?purpose of a well-child visit", "Well-child visits assess growth, development, and overall health, and provide an opportunity for vaccinations and parental questions."),
    (r"(when|age) (should|have) (my|a) child have their first eye exam", "The American Academy of Ophthalmology recommends an eye exam by age 1, with follow-ups at age 3 and before starting school."),
    (r"(what is|about) (the )?importance of lead screening", "Lead screening identifies children at risk for lead poisoning, which can affect development and health. It is typically done around age 1 or 2."),

    # Social Skills
    (r"help (my|a) child make friends", "Encourage social interactions through playdates, extracurricular activities, and teaching sharing and communication skills."),
    (r"(child|baby) is being bullied", "Talk to your child about their feelings, document incidents, and contact school officials for support and intervention."),
    (r"teach (my|a) child empathy", "Model empathetic behavior, discuss feelings, and encourage perspective-taking in social situations."),
    (r"(what is|about) (the )?role (of|does) play (have|in) (in|a) (a )?child's development", "Play is crucial for social, emotional, and cognitive development, helping children learn problem-solving and cooperation."),
    (r"encourage teamwork in (my|a) child", "Involve them in group activities, sports, and collaborative projects, emphasizing the importance of working together."),

    # First Aid
    (r"(child|baby) has a cut", "Clean the wound with soap and water, apply an antibiotic ointment, and cover it with a bandage. Seek medical attention for deep cuts or signs of infection."),
    (r"treat a burn on (my|a) child", "Cool the burn under running water for 10-20 minutes, cover it with a sterile bandage, and seek medical attention for serious burns."),
    (r"(child|baby) has a nosebleed", "Have them sit upright and pinch their nostrils together for 5-10 minutes. If it doesn't stop, seek medical advice."),
    (r"(what are|about) (the )?steps for CPR on a child", "Call for help, check for responsiveness, perform chest compressions, and give rescue breaths if trained. Follow local guidelines."),
    (r"prevent choking in young children", "Supervise eating, avoid small or hard foods, and teach them to chew thoroughly. Learn the Heimlich maneuver for emergencies."),

    # Travel Safety
    (r"safety measures (should I|to) take when traveling with children", "Use appropriate car seats, pack snacks and entertainment, and ensure regular breaks during long trips."),
    (r"keep (my|a) child safe while flying", "Use a child safety seat if possible, explain the flying process, and bring comfort items for takeoff and landing."),
    (r"tips for a road trip with kids", "Plan stops, have activities or games ready, and pack healthy snacks to keep them engaged."),
    (r"(should|wear) (my|a) child wear a seatbelt on a plane", "Yes, children should be secured with a seatbelt during takeoff, landing, and whenever instructed by the crew."),
    (r"teach (my|a) child to be safe in new environments", "Discuss safety rules, role-play scenarios, and encourage them to ask for help when needed."),

    # Parent Resources
    (r"(where|how) (can I|to) find reliable parenting resources", "Look for reputable websites like the CDC, AAP, and parenting organizations, as well as books by pediatric experts."),
    (r"(how|ways) (can I|to) connect with other parents", "Join local parenting groups, online forums, or social media communities to share experiences and advice."),
    (r"(what are|recommend) (some )?good parenting books", "Consider 'The Whole-Brain Child' by Daniel J. Siegel, 'How to Talk So Kids Will Listen' by Adele Faber, and 'Simplicity Parenting' by Kim John Payne."),
    (r"(what|available) support (is|for) (available for|new) new parents", "Look for local parenting classes, support groups, and resources from healthcare providers and community organizations."),
    (r"(how|ways) (can I|to) find a pediatrician for (my|a) child", "Ask for recommendations from friends or family, check with your insurance provider, and schedule interviews to find the right fit."),

    # Final Thoughts
    (r"(what is|about) the most important thing (I can do|to do) as a parent", "Provide love, support, and guidance while fostering independence and resilience in your child."),
    (r"(how|ways) (can I|to) maintain a healthy relationship with (my|a) child", "Communicate openly, spend quality time together, and actively listen to their thoughts and feelings."),
    (r"(what should I do|help) if I feel overwhelmed as a parent", "Seek support from friends, family, or professionals, and take time for self-care to recharge."),
    (r"(how|ways) (can I|to) help (my|a) child deal with change", "Prepare them for changes, maintain routines, and encourage them to express their feelings."),
    (r"(ways|how) to celebrate (my|a) child's achievements", "Offer praise, plan small celebrations, or create a recognition board at home to showcase their accomplishments."),

    # Unique Questions
    (r"(how|ways) (do I|to) know if (my|a) child is gifted", "Signs of giftedness may include advanced problem-solving skills, intense curiosity, and a strong memory. Consider testing if you're concerned."),
    (r"(how|ways) (can I|to) teach (my|a) child about diversity and inclusion", "Expose them to diverse cultures, read inclusive books, and discuss differences openly and positively."),
    (r"(effective ways|how) to reduce (my|a) child's screen time", "Set limits, encourage other activities, and model healthy screen habits as a parent."),
    (r"(how|ways) (can I|to) support (my|a) child during a family transition, like divorce", "Maintain open communication, reassure them of your love, and consider professional counseling if needed."),
    (r"(what is|about) the role of play in a child's learning", "Play fosters creativity, problem-solving skills, social interactions, and cognitive development, making it an essential part of learning."),

    # Fallback response
    (r".*", "I'm not sure about that specific topic. Could you try rephrasing your question or asking about a different pediatric care topic?")
]

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

