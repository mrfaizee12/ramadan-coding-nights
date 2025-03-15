import streamlit as st
import requests

# Custom CSS for better UI with dark gradient background
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            color: white;
        }
        .stApp {
            background: linear-gradient(135deg, #1a1a2e, #16213e);
        }
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #FF1C1C;
        }
        .stTitle {
            color: #FFD700; /* Yellow */
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
        }
        .stContainer {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            text-align: center;
            color: white;
        }
        .stInstructions {
            color: #E0E0E0; /* Light Gray */
            text-align: center;
            font-size: 1.2rem;
        }
        .footer {
            text-align: center;
            color: white;
            margin-top: 20px;
            font-size: 14px;
        }
        .footer a {
            color: #ff4b4b;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"**{joke_data['setup']}**  \n\n *{joke_data['punchline']}*"
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        return "**Why did the programmer quit his job?**  \n\n *Because he didn't get array!*" 

def main():
    st.markdown('<h1 class="stTitle">😂 Random Joke Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="stInstructions">Click the button below to generate a random joke.</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)

    if st.button("Tell me a Joke!"):
        with st.spinner("Fetching a joke... 😂"):
            joke = get_random_joke()
        st.success(joke)

    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown(
        """
        <div class='footer'>
             <p>Joke from Official Joke API</p>
             <p>Built with ❤ by <a href='https://github.com/mrfaizee12'>Faizee</a> using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
