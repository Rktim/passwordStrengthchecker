import re
import streamlit as st

def check_password_strength(p):
    len_error = len(p) < 12 
    digit_error = re.search(r'\d', p) is None
    uppercase_error = re.search(r'[A-Z]', p) is None
    lowercase_error = re.search(r'[a-z]', p) is None
    special_error = re.search(r'[@#$%!*?^&+=-]', p) is None  # More special characters included

    errors = {
        "length": len_error,
        "digit": digit_error,
        "uppercase": uppercase_error,
        "lowercase": lowercase_error,
        "special": special_error
    }
    
    error_count = sum(errors.values())

    if error_count == 0:
        return "Very Strong Password!!"
    elif error_count == 1:
        return "Strong Password!!"
    elif error_count == 2:
        return "Moderate Password.."
    elif error_count == 3:
        return "Weak Password!!"
    else:
        return "Very Weak Password!!"

def detailed_feedback(errors):
    feedback = []
    if errors["length"]:
        feedback.append("Password must be at least 12 characters long.")
    if errors["digit"]:
        feedback.append("Password must include at least one digit.")
    if errors["uppercase"]:
        feedback.append("Password must include at least one uppercase letter.")
    if errors["lowercase"]:
        feedback.append("Password must include at least one lowercase letter.")
    if errors["special"]:
        feedback.append("Password must include at least one special character (e.g., @, #, $, %, etc.).")
    
    return feedback

st.title("Password Checker 🧐")

st.markdown(
    """
    <style>
    .custom-font {
        font-family: Arial;
        font-size: 40px;
        color: Red;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

password = st.text_input("Enter your password:")

if password:
    strength = check_password_strength(password)
    feedback = detailed_feedback({
        "length": len(password) < 12,
        "digit": re.search(r'\d', password) is None,
        "uppercase": re.search(r'[A-Z]', password) is None,
        "lowercase": re.search(r'[a-z]', password) is None,
        "special": re.search(r'[@#$%!*?^&+=-]', password) is None
    })
    
    st.markdown(f'<p class="custom-font">{strength}</p>', unsafe_allow_html=True)
    
    if feedback:
        st.write("### Suggestions to improve your password:")
        for line in feedback:
            st.write(f"- {line}")

st.write("Made by Raktim Kalita [raktmxx@gmail.com]")
