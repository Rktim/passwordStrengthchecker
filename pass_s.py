import re
import streamlit as st

def check_password_strength(p):
    len_error=len(p)<8
    digit_error=re.search(r'\d',p) is None
    uppercase_error=re.search(r'[A-Z]',p) is None
    lowercase_error=re.search(r'[a-z]',p) is None
    special_error=re.search(r'[@#$%!*?^&]',p) is None
    
    error=sum([len_error,digit_error,uppercase_error,lowercase_error,special_error])
    
    if error==0:
        return "Strong Password!!"
    elif error<=2:
        return "Moderate Password.."
    elif error<2:
        return "Weak Password!!"

st.title("Password Checker🧐!!")


st.markdown(
    """
    <style>
    .custom-font {
        font-family:  Ariel;
        font-size: 40px;
        color: Red;
        font-weight:bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

password = st.text_input("Enter your password:")

if password:
    strength = check_password_strength(password)
    st.markdown(f'<p class="custom-font">{strength}</p>', unsafe_allow_html=True)
    
    
st.write("made by-Raktim Kalita [raktmxx@gmail.com]")