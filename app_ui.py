import streamlit as st
import cv2
import numpy as np
from PIL import Image
from processor import ask_vault_ai
from gtts import gTTS
import os
import base64

# --- 1. PAGE SETTINGS & HACKER THEME ---
st.set_page_config(page_title="AI Secure Vault", page_icon="🔐", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    p, h1, h2, h3, label, .stChatMessage { color: #00ff41 !important; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #00ff41; color: black; border-radius: 10px; font-weight: bold; border: none; }
    .stChatInputContainer { border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. VOICE FUNCTION (SINGLE VOICE FIX) ---
def speak_text(text):
    try:
        if os.path.exists("response.mp3"):
            os.remove("response.mp3")
        
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        
        with open("response.mp3", "rb") as f:
            audio_bytes = f.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()
            # Sirf HTML Autoplay use kar rahe hain taaki double voice na aaye
            audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_base64}">'
            st.markdown(audio_tag, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Voice Error: {e}")

# --- 3. FACE DETECTION SETUP ---
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- 4. MAIN UI LOGIC ---
st.title("🛡️ NEURAL SECURE VAULT")

if not st.session_state.authenticated:
    st.subheader("SYSTEM LOCKED: Face ID Required")
    img_file = st.camera_input("Scan Identity")

    if img_file:
        img = Image.open(img_file)
        img_np = np.array(img)
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            st.success("✅ IDENTITY VERIFIED. ACCESS GRANTED.")
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ UNKNOWN ENTITY. ACCESS DENIED.")
else:
    # VAULT GRANTED
    st.sidebar.success("🔓 OWNER LOGGED IN")
    if st.sidebar.button("🔒 EMERGENCY LOCK"):
        st.session_state.authenticated = False
        st.rerun()

    st.write("### 🤖 Vault Intelligence Active")
    
    query = st.chat_input("Query your encrypted documents...")
    
    if query:
        with st.chat_message("user"):
            st.write(query)
            
        with st.spinner("⚡ Processing Neural Link..."):
            response = ask_vault_ai(query)
            with st.chat_message("assistant"):
                st.write(response)
                speak_text(response)