import streamlit as st
import smtplib
import random

from email_validator import validate_email, EmailNotValidError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from captcha.image import ImageCaptcha

options = st.secrets['OPTIONS']
server = st.secrets["SERVER"]
port = st.secrets["PORT"]
user_name = st.secrets["USERNAME"]
password = st.secrets["PASSWORD"]
recipient = st.secrets["RECIPIENT"]

def generate_captcha():
    captcha_text = "".join(random.choices(options, k=6)) # options is a string of characters that can be included in the CAPTCHA. It may be as simple or as complex as you wish. 
    image = ImageCaptcha(width=400, height=100).generate(captcha_text)
    return captcha_text, image

## Generate CAPTCHA
if 'captcha_text' not in st.session_state:
    st.session_state.captcha_text = generate_captcha()

captcha_text, captcha_image = st.session_state.captcha_text

## Contact Form

# Page configuration options
page_title = "Contact Form"
page_icon = ":email:"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Show the title of the app
st.header("📫 Contact Form")

col1, col2, col3, col4 =  st.columns([3, 0.25, 1, 0.25]) # column widths for a balanced distribution of elements in the page

captcha_input = None # initiate CAPTCHA

## CAPTCHA
with col3: # right side of the layout
    st.markdown('<p style="text-align: justify; font-size: 12px;">CAPTCHAs are active to prevent automated submissions. <br> Thank you for your understanding.</p>', unsafe_allow_html=True) # warning for user.
    captcha_placeholder = st.empty()
    captcha_placeholder.image(captcha_image, use_column_width=True)

    if st.button("Refresh", type="secondary", use_container_width=True): # option to refresh CAPTCHA without refreshing the page
        st.session_state.captcha_text = generate_captcha()
        captcha_text, captcha_image = st.session_state.captcha_text
        captcha_placeholder.image(captcha_image, use_column_width=True)

    captcha_input = st.text_input("Enter the CAPTCHA") # box to insert CAPTCHA
    

