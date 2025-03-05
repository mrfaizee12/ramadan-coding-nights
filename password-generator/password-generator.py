import streamlit as st  # Streamlit library import kr rahay hain jo UI elements ko handle karegi
import random  # Random module import kr rahay hain jo random values generate karega
import string  # String module import kr rahay hain jo letters, digits, aur special characters ko handle karega

# Function jo password generate karega
# length: password ki length specify karega
# use_digits: agar True hoga to digits include hongi
# use_special: agar True hoga to special characters include honge
def generator_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Initially sirf alphabets ko include kar rahay hain

    if use_digits:
        characters += string.digits  # Agar user ne digits include karni hon to add kar rahay hain

    if use_special:
        characters += string.punctuation  # Agar user ne special characters include karne hon to add kar rahay hain

    return ''.join(random.choice(characters) for _ in range(length))  # Random characters choose kr k password return kr rahay hain

st.title("Password Generator")  # Streamlit ka title set kar rahay hain

# Slider jo user ko password ki length choose karne dega
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

# Checkbox jo user ko decide karne dega k digits include karni hain ya nahi
use_digits = st.checkbox("Include Digits")

# Checkbox jo user ko decide karne dega k special characters include karne hain ya nahi
use_special = st.checkbox("Include Special Characters")

# Button jo password generate karega jab user click karega
if st.button("Generate Password"):
    password = generator_password(length, use_digits, use_special)  # Function call kar k password generate kar rahay hain
    st.write(f"Generated Password: `{password}`")  # Generated password ko display kar rahay hain

st.write("------------------------")  # UI ko separate karne ke liye horizontal line add kar rahay hain

# Footer jo developer ka naam aur GitHub profile show karega
st.write("Build with ❤ by [Faizan Anjum](https://github.com/mrfaizee12)")