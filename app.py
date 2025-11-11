import streamlit as st
import google.generativeai as genai
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Lexi AI",
    page_icon="🤖"
)

# --- LOAD EXTERNAL CSS ---
def load_css(file_name):
    # Resolve path relative to this script to avoid issues when Streamlit
    # changes the current working directory at runtime.
    
    try:
        css_path = Path(__file__).parent / file_name
        with open(css_path) as f:
            css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {css_path}")

# --- LOAD CSS ---
# Call the function to inject your CSS file
load_css("style.css")

# --- 1. PERSONA CONFIGURATION ---
SYSTEM_PROMPT = """
You are an AI assistant named 'Lexi'. Your main goal is to help the user find media recommendations
(drama, series, movies, books, anime) and styles (fashion and decor). You must be empathetic and helpful.

IMPORTANT ETHICAL GUIDELINE: You must NEVER act as a therapist
or give mental health advice. If the user seems sad or vents,
you should gently redirect them to a professional, stating that your scope is only recommendation.

You should answer in the user's language, be concise and double-check facts when possible.
"""
# --- 2. API KEY MANAGEMENT ---

# Try to get the API key from Streamlit secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    # If not found (User Method), prompt in the sidebar
    API_KEY = None

# Show text box in sidebar if key not found
if API_KEY is None:
    st.sidebar.header("🔑 API Configuration")
    API_KEY = st.sidebar.text_input(
        "Enter your Google Gemini API Key:",
        type="password",
        help="Obtain your key from Google AI Studio (formerly MakerSuite)."
    )

# --- 3. INITIALIZATION AND APP LOGIC ---

# Main title
st.title("Lexi AI 🤖")
st.caption("A prototype assistant with 'Ethical Guardrails'.")

# Only continue executing the rest of the app if the API_KEY exists
if not API_KEY:
    st.info("Please enter your Google Gemini API Key in the sidebar to get started.")
    st.stop() # Stop execution here if no key

# Configure the Google API (only after confirming API_KEY exists)
try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error(f"Error configuring Google API: {e}")
    st.stop()

# --- 4. MODEL INITIALIZATION ---

try:
    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        system_instruction=SYSTEM_PROMPT 
    )
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Initialize chat history in session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# --- 5. CHAT INTERFACE ---

# Show chat message history
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# User input at the bottom of the page
user_input = st.chat_input("Ask something to Lexi AI...")

if user_input:
    # Add user message to history and display
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send message to AI
    with st.spinner("Thinking..."):
        try:
            response = st.session_state.chat.send_message(user_input)

            # Show AI response
            with st.chat_message("assistant"):
                st.markdown(response.text)
        
        except Exception as e:
            st.error(f"Error talking to AI: {e}")