import streamlit as st  # Import Streamlit for building the web app

# Custom CSS for UI Styling
st.markdown("""
    <style>
        /* Background color for better visibility */
        body {
            background-color: #f4f4f4;
        }
        /* App main container gradient background */
        .stApp {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: white;
            font-family: Arial, sans-serif;
        }
        /* Styling for input fields */
        .stTextInput, .stNumberInput, .stSelectbox {
            background-color: white !important;
            color: black !important;
            border-radius: 8px;
            padding: 10px;
        }
        /* Button styling */
        .stButton>button {
            background-color: #ff7f50;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            transition: 0.3s ease;
        }
        /* Button hover effect */
        .stButton>button:hover {
            background-color: #ff4500;
        }
        /* Success message styling */
        .stSuccess {
            background-color: #32cd32;
            color: white;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
        }
        /* Footer styling */
        .footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            color: white;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)  # Injecting CSS for better styling

def main():
    st.title("🔥 Stylish Calculator 🔥")  # App title with emojis for better UI
    st.write("Enter two numbers and choose an operation")  # Instruction text for the user

    col1, col2 = st.columns(2)  # Splitting the input fields into two columns

    with col1:
        num1 = st.number_input("Enter first number", value=0.0)  # Input field for first number

    with col2:
        num2 = st.number_input("Enter second number", value=0.0)  # Input field for second number

    # Dropdown to select operation
    operation = st.selectbox("Choose operation", ["Addition (+)", "Subtraction (-)", "Multiplication (x)", "Division (/)"])

    if st.button("Calculate"):  # Calculate button
        try:
            if operation == "Addition (+)":
                result = num1 + num2  # Performing addition
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2  # Performing subtraction
                symbol = "-"
            elif operation == "Multiplication (x)":
                result = num1 * num2  # Performing multiplication
                symbol = "x"
            elif operation == "Division (/)":
                if num2 == 0:  # Handling division by zero
                    st.error("Error: Division by Zero!")
                    return
                result = num1 / num2  # Performing division
                symbol = "/"

            # Displaying the result
            st.markdown(f'<div class="stSuccess">{num1} {symbol} {num2} = {result}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")  # Error handling for any exceptions

    # Footer with your name
    st.markdown('<div class="footer">Developed by Faizee 🚀</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()  # Running the main function
