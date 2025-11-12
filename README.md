# Lexi AI 🤖
- **Project Status:** (Conceptual Prototype - Potenc.IA Course | Creators of the Future with AI)

- A prototype of an AI assistant focused on ethical and hyper-personalized recommendations, built with Streamlit and the Google Gemini API.

# 🎯 The Problem
In the information age, we suffer from the **"paradox of choice"** (or decision fatigue). Current recommendation algorithms are superficial and fail in two main points:

1. **They Ignore Negative Filters:** They don't understand niche preferences or specific moral/ethical restrictions (e.g., "I want romance series, but that don't have graphic violence scenes").

2. **They Generate Dependency:** Many AI systems are designed to maximize "engagement", encouraging emotional dependence and excessive use, instead of focusing on efficiency.

# ✨ The Solution: The "Virtual Persona"
Lexi AI solves this through a two-layer "Virtual Persona" system:

1. **The "Mother-Persona":** It is the AI's main *SYSTEM_PROMPT*. It contains the Ethical Guardrails (the "don't be a therapist" rule), the AI's personality (helpful, but not intimate), and the logic of how it should build the user's persona.

2. **The "User Persona":** It is the profile that the user builds. It stores not only tastes (*I like K-pop and cottage core*), but mainly their filters and boundaries (*I hate horror movies*, *I love series about chicken's feet*).

The goal is to be an efficiency tool: a "second brain" that saves the user's research time, so they can use their rest time to rest.

# 🚀 Main Features (of the Prototype)
- **Chat Interface:** A clean and reactive interface built with Streamlit.

- **Secrets Management:** The project uses Streamlit's *secrets.toml* and *.gitignore* to protect the API key, allowing the code to be public without exposing sensitive data.

- **Ethical Guardrails:** The AI is instructed (via the "Mother-Persona") to identify and redirect conversations that go out of the scope of recommendations (like requests for therapy), aiming for the user's mental health.

- **Persistent Chat:** The conversation history is saved in the session (using *st.session_state*).

# 🧠 Key Concepts (Future Architecture)
This prototype proves "Phase 0", but the project's complete design (discussed in the conception) envisions a more robust system:

- **The "Invisible Robot" (Backend):** An asynchronous process that would perform data collection (Data Scraping) on social media (e.g., "fan edits" on TikTok) and forums (e.g., MyDramaList).

- **Topic Discovery (Topic Modeling):** Instead of using predefined tags, the "Robot" would use AI to discover relevant tags (like "funny" or "hot edit") by analyzing word frequency in fan discussions, allowing for niche recommendations.

# 🛠️ Technologies Used
- **Python**

- **Streamlit** (For the web interface)

- **Google Gemini API** (For the AI's brain)

- **GitHub Codespaces** (As a cloud development environment)

# 🏃‍♀️ How to Run the Prototype
This project was developed to run easily on GitHub Codespaces.

1. **Start the Codespace:** Open this repository in a new Codespace.

2. **Create your Secrets:**

    - Create a new folder in the project root called *.streamlit*.
      
    - Inside it, create a file called *secrets.toml*.
      
    - Paste your API key into this file.

3. **Install the Dependencies:**

    - Create a *requirements.txt* file and add *streamlit* and *google-generativeai*.
      
    - In the Codespaces terminal, run: *pip install -r requirements.txt*.

4. **Run the App:**
   
    - In the terminal, run: *streamlit run app.py*.
      
    - Codespaces will notify you to open the application in a new browser tab.

# 📆 Next Steps (Future Phases)
- **[Phase 1 - Media]:** Expand the prototype to connect to real databases (like Common Sense Media) to validate the filters.

- **[Phase 2 - Style and Shopping]:** Implement Computer Vision (CV) so the AI can analyze photos of clothes and recommend outfits based on styles (Cottage Core, Y2K).

- **[Phase 3 - The Robot]:** Build the "Invisible Robot" (backend worker) to perform data collection and topic discovery in real-time.
