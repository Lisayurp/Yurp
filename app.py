import streamlit as st 

  

# Initialize session state for history 

if 'history' not in st.session_state: 

    st.session_state.history = [] 

  

def add_to_history(message): 

    st.session_state.history.append(message) 

  

def main(): 

    st.title("KidCare Bot - Your Pediatric Care Assistant") 

  

    st.sidebar.title("Navigation") 

    pages = ["Welcome", "General Inquiry", "Symptom Checker", "Development Milestones", "Nutrition and Diet", "Vaccination Schedule"] 

    choice = st.sidebar.radio("Go to", pages) 

  

    if choice == "Welcome": 

        st.write("Welcome to the KidCare Bot! How can I assist you today?") 

  

    elif choice == "General Inquiry": 

        if st.button("Are there any general questions regarding pediatric care you would like to know about?"): 

            add_to_history("User: Asked about general questions") 

  

            # Provide general information or answer question 

            st.write("KidCare Bot: Here is some information that might help you with pediatric care...") 

            st.markdown("- **Regular Check-ups**: Infants should have check-ups at 2-4 weeks, 2, 4, 6, 9, and 12 months. Toddlers typically need visits at 15, 18, and 24 months, then annually after age 3.") 

            st.markdown("- **Developmental Milestones**: These include physical, cognitive, and social-emotional skills such as sitting up, walking, talking, and interacting with others.") 

            st.markdown("- **Healthy Diet**: A balanced diet includes fruits, vegetables, whole grains, proteins, and dairy. Limit sugars and unhealthy fats.") 

            st.markdown("- **Safety Measures**: Childproof your home, supervise playtime, use safety gear, and teach safety rules.") 

  

    elif choice == "Symptom Checker": 

        if st.button("Is your child experiencing any symptoms that you'd like to know more about?"): 

            add_to_history("User: Interested in symptom checker") 

  

            # Ask for symptom description 

            symptoms = st.text_input("KidCare Bot: Please describe the symptoms:") 

            if symptoms: 

                add_to_history(f"User: Described symptoms - {symptoms}") 

  

                # Provide potential causes and advice on next steps 

                st.write("KidCare Bot: Here are some potential causes and advice on next steps for these symptoms...") 

                if "fever" in symptoms.lower(): 

                    st.markdown("- **Fever**: If your child has a fever, ensure they rest and stay hydrated. Use acetaminophen or ibuprofen as directed.") 

                    st.markdown("- **High Fever**: Seek medical advice if fever is high or persistent, or accompanied by other symptoms.") 
st.write (symptoms)
                if "cough" in symptoms.lower(): 

                    st.markdown("- **Cough**: For a persistent cough, use a humidifier and offer warm fluids. Seek medical advice if it worsens or lasts more than a week.") 

  

    elif choice == "Development Milestones": 

        if st.button("Would you like information on your child's developmental milestones?"): 

            add_to_history("User: Interested in developmental milestones") 

  

            # Ask for child's age 

            child_age = st.number_input("KidCare Bot: What is your child's age?", min_value=0, max_value=18) 

            if child_age: 

                add_to_history(f"User: Child's age is {child_age}") 

  

                # Provide milestones and tips for age-appropriate activities 

                st.write(f"KidCare Bot: Here are the developmental milestones and tips for age {child_age}...") 

                if child_age < 1: 

                    st.markdown("- **0-6 Months**: Focus on tummy time to strengthen muscles. Encourage reaching and grasping objects.") 

                    st.markdown("- **Language Development**: Begin to coo and make sounds in response to interactions.") 

                elif 1 <= child_age < 3: 

                    st.markdown("- **1-2 Years**: Support walking and climbing. Foster language development through talking and reading.") 

                    st.markdown("- **Social Skills**: Begin to play alongside other children and imitate simple actions.") 

                elif 3 <= child_age < 6: 

                    st.markdown("- **3-5 Years**: Promote social skills with group play. Encourage independence in daily tasks like dressing.") 

                    st.markdown("- **School Readiness**: Begin to recognize letters, numbers, and colors.") 

  

    elif choice == "Nutrition and Diet": 

        if st.button("Do you have any questions about your child's nutrition and diet?"): 

            add_to_history("User: Interested in nutrition and diet") 

  

            # Ask for specific aspect of nutrition 

            nutrition_topic = st.text_input("KidCare Bot: What specific aspect of nutrition are you interested in? (e.g., meal plans, vitamins)") 

            if nutrition_topic: 

                add_to_history(f"User: Asked about {nutrition_topic}") 

  

                # Provide advice and recommendations 

                st.write("KidCare Bot: Here is some advice and recommendations on that topic...") 

                if "meal plans" in nutrition_topic.lower(): 

                    st.markdown("- **Balanced Meals**: Include fruits, vegetables, whole grains, and proteins in every meal.") 

                    st.markdown("- **Healthy Snacks**: Offer yogurt, cut-up fruits, and whole-grain crackers as snacks.") 

                elif "vitamins" in nutrition_topic.lower(): 

                    st.markdown("- **Essential Vitamins**: Ensure your child gets enough vitamin D for bone health and vitamin C for immunity.") 

                    st.markdown("- **Supplements**: Discuss with your pediatrician before giving any supplements.") 

  

    elif choice == "Vaccination Schedule": 

        if st.button("Would you like to know about the recommended vaccination schedule for your child?"): 

            add_to_history("User: Interested in vaccination schedule") 

  

            # Ask for child's age 

            vaccination_age = st.number_input("KidCare Bot: What is your child's age?", min_value=0, max_value=18) 

            if vaccination_age: 

                add_to_history(f"User: Child's age is {vaccination_age}") 

  

                # Provide the recommended vaccination schedule 

                st.write(f"KidCare Bot: Here is the recommended vaccination schedule for age {vaccination_age}...") 

                if vaccination_age < 1: 

                    st.markdown("- **Birth-1 Year**: Vaccines include hepatitis B, rotavirus, DTaP, Hib, pneumococcal, polio, and influenza (seasonal).") 

                elif 1 <= vaccination_age < 6: 

                    st.markdown("- **1-5 Years**: Boosters for DTaP, MMR, varicella, polio, hepatitis A. Annual flu vaccine recommended.") 

                elif 6 <= vaccination_age < 12: 

                    st.markdown("- **6-11 Years**: Boosters for DTaP, HPV, meningococcal, and annual flu vaccine.") 

                elif 12 <= vaccination_age < 18: 

                    st.markdown("- **12-18 Years**: Boosters for Tdap, meningococcal, HPV, annual flu vaccine. Consider COVID-19 vaccine.") 

  

    # Display chat history in sidebar 

    st.sidebar.title("Chat History") 

    for item in st.session_state.history: 

        st.sidebar.write(item) 

  

    st.sidebar.markdown("---") 

    st.sidebar.write("Thank you for using KidCare Bot!") 

  

if __name__ == "__main__": 

    main() 

 

 

 

 
