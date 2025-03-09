import streamlit as st
import pandas as pd
import datetime
import csv 
import os

# File to store mood data
MOOD_FILE = "mood_log.csv"

# Load mood data from CSV file
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

# Save mood data to CSV file
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Apply custom CSS for styling and responsiveness
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #74EBD5 0%, #9FACE6 100%);
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        padding: 20px;
    }
    h1, h2, h3 {
        color: #333;
        text-align: center;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stSelectbox, .stTextInput {
        padding: 10px;
        border-radius: 8px;
    }
    .css-1aumxhk, .stAlert {
        text-align: center;
    }
    .css-1v0mbdj, .stDataFrame {
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
    }
    @media (max-width: 768px) {
        .stApp {
            padding: 10px;
        }
        .stButton > button {
            width: 100%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("Mood Tracker")

today = datetime.date.today()

# Mood input section
st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Funny", "Neutral"])

# Button to log mood
if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully")

# Load and display mood data
data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_counts)

# Let me know if you want any more tweaks or features! 🚀
