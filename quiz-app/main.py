import time  # Importing time module for adding delays
import streamlit as st  # Importing Streamlit for UI
import random  # Importing random for selecting random questions

st.title("📝 Quiz Application")  # Setting the title of the app

questions = [
    {"question": "What is the capital of Pakistan?", "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"], "answer": "Islamabad"},
    {"question": "Which is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
    {"question": "Who developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "answer": "Albert Einstein"},
    {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": "Au"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi Apparatus"], "answer": "Mitochondria"},
    {"question": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "What is the national language of Pakistan?", "options": ["English", "Sindhi", "Punjabi", "Urdu"], "answer": "Urdu"},
    {"question": "Who wrote the famous play 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "answer": "William Shakespeare"},
    {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "Which is the longest river in the world?", "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "answer": "Nile River"},
    {"question": "What is the boiling point of water at sea level?", "options": ["90°C", "95°C", "100°C", "105°C"], "answer": "100°C"},
    {"question": "Which metal is liquid at room temperature?", "options": ["Mercury", "Gold", "Silver", "Lead"], "answer": "Mercury"},
    {"question": "What is the currency of Japan?", "options": ["Yuan", "Won", "Yen", "Rupee"], "answer": "Yen"}
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)  # Selecting a random question initially

question = st.session_state.current_question  # Fetching the current question

st.subheader(question["question"])  # Displaying the question

selected_options = st.radio("Choose your answer", question["options"], key="answer")  # Displaying answer options

if st.button("Submit Answer"):  # Checking if the submit button is clicked
    if selected_options == question["answer"]:
        st.success("✔ Correct!")  # Displaying success message
        st.balloons()  # Adding balloon effect for correct answer
    else:
        st.error("Incorrect! the correct answer is " + question["answer"])  # Displaying error message for incorrect answer
    
    time.sleep(3)  # Adding delay before moving to the next question

    st.session_state.current_question = random.choice(questions)  # Selecting a new random question

    st.rerun()  # Rerunning the app to display the next question
