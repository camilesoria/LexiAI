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

# --- SIDEBAR CONFIGURATION ---
st.sidebar.title("👤 Your Profile")

# 1. Input field for user likes
user_likes = st.sidebar.text_area(
    "What do you like?",
    placeholder="Ex: music genres, yellow, learning languages...",
    help="Lexi will prioritize these topics."
)

# 2. Input field for what to AVOID (User filters)
user_dislikes = st.sidebar.text_area(
    "What to avoid? (Triggers/Filters)",
    placeholder="Ex: violence, orange, sad movies...",
    help="Lexi will never recommend things with these themes."
)

# --- 1. DYNAMIC PROMPT CONSTRUCTION ---

# The fixed part (System Rules)
BASE_SYSTEM_PROMPT = """
You are an AI assistant named 'Lexi'. Your main goal is to help the user find media recommendations
(drama, series, movies, books, anime) and styles (fashion and decor). You must be empathetic and helpful.

CHECK THE USER PROFILE FIRST: If the user has provided interests in the 'USER INTERESTS' section,
USE THEM IMMEDIATELY. Do not ask generic questions like "what do you like?" if the info is already there.
RESPECT FILTERS: Never recommend anything listed in 'STRICT NEGATIVE FILTERS'.
BE CONCISE: Go straight to the point.

IMPORTANT ETHICAL GUIDELINE: You must NEVER act as a therapist
or give mental health advice. If the user seems sad or vents,
you should gently redirect them to a professional, stating that your scope is only recommendation.

You should answer in the user's language, be concise and double-check facts when possible.
"""

# The dynamic part
# If the user wrote something, add it to the prompt. If not, leave it empty.
user_context = ""
if user_likes:
    user_context += f"\nUSER INTERESTS: {user_likes}"
if user_dislikes:
    user_context += f"\nSTRICT NEGATIVE FILTERS (DO NOT RECOMMEND): {user_dislikes}"

# Combining everything into the Final Prompt
FINAL_PROMPT = BASE_SYSTEM_PROMPT + user_context

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
    
    with st.sidebar.expander("ℹ️ Privacy & Terms of Use"):
            st.markdown("""
            **1. Data Privacy:**
            * Your API Key and Conversation History are processed **only for this session** in temporary RAM memory.
            * They are **never** saved to any database, log file, or permanent storage by this application.
            
            **2. Security Disclaimer:**
            * **User Responsibility:** You are responsible for the security of your own device and network. We are not liable for malware or spyware on the user's side.
            * **Third-Party Liability:** This application is hosted on **Streamlit Community Cloud**. We are not responsible for any security breaches, hacks, or data leaks affecting the hosting platform or Google's API servers.
            
            **3. "As-Is" Service:**
            * This is a **student prototype** provided for educational purposes only.
            * It is provided "as-is" without warranty of any kind.
            """)
        
    API_KEY = st.sidebar.text_input(
        "Enter your Google Gemini API Key:",
        type="password",
        help="Your key will not be stored persistently. Obtain your key from Google AI Studio."
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
        system_instruction=FINAL_PROMPT 
    )
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Initialize chat history in session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# --- 5. HANDLE PROFILE UPDATE  ---

if st.sidebar.button("💾 Update Profile"):
    try:
        # 1. Retrieve the existing chat history
        if "chat" in st.session_state:
            current_history = st.session_state.chat.history
        else:
            current_history = []
        
        # 2. Start a new chat session with the updated model
        st.session_state.chat = model.start_chat(history=current_history)
        
        # 3. Rerun the app
        st.rerun()
        
    except Exception as e:
        st.error(f"Error updating profile: {e}")

# --- 6. CHAT INTERFACE ---

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