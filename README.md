# Lexi AI 🤖

**Project Status:** (Conceptual Prototype - Potenc.IA Course | Creators of the Future with AI)

A prototype of an AI assistant focused on ethical and hyper-personalized recommendations, built with Streamlit and the Google Gemini API.

# 🎯 The Problem
In the information age, we suffer from the **"paradox of choice"** (or decision fatigue). Current recommendation algorithms are superficial and fail in two main points:

1.  **They Ignore Negative Filters:** They don't understand niche preferences or specific moral/ethical restrictions (e.g., *"I want romance series, but that don't have graphic violence scenes"*).
2.  **They Generate Dependency:** Many AI systems are designed to maximize "engagement", encouraging emotional dependence and excessive use, instead of focusing on efficiency.

# ✨ The Solution: The "Virtual Persona"
Lexi AI solves this through a two-layer "Virtual Persona" system:

1.  **The "Mother-Persona":** It is the AI's main *SYSTEM_PROMPT*. It contains the Ethical Guardrails (the "don't be a therapist" rule), the AI's personality (helpful, but not intimate), and the logic of how it should build the user's persona.
2.  **The "User Persona":** It is the profile that the user builds interactively. It stores not only tastes (*I like K-pop and cottage core*), but mainly their filters and boundaries (*I hate horror movies, I love series about chicken's feet*).

The goal is to be an efficiency tool: a "second brain" that saves the user's research time, so they can use their rest time to rest.

# 🚀 Main Features (of the Prototype)
* **Chat Interface:** A clean and reactive interface built with Streamlit, featuring a modern, dark-themed UI.
* **Dynamic Profiling (Real-Time):** Users can define their "Likes" and "Negative Filters" via the sidebar. The "Update Profile" button instantly injects these preferences into the AI's context without losing the ongoing conversation history.
* **Privacy-First Architecture:** The project supports a "Bring Your Own Key" model. API keys entered in the UI are processed in **temporary RAM only** and are never saved to a database, ensuring user security.
* **Ethical Guardrails:** The AI is instructed (via the "Mother-Persona") to identify and redirect conversations that go out of the scope of recommendations (like requests for therapy), aiming for the user's mental health.

# 🧠 Key Concepts (Future Architecture)
This prototype proves "Phase 0", but the project's complete design (discussed in the conception) envisions a more robust system:

* **The "Invisible Robot" (Backend):** An asynchronous process that would perform data collection (Data Scraping) on social media (e.g., "fan edits" on TikTok) and forums (e.g., MyDramaList).
* **Topic Discovery (Topic Modeling):** Instead of using predefined tags, the "Robot" would use AI to discover relevant tags (like "funny" or "cute") by analyzing word frequency in fan discussions, allowing for niche recommendations.

# 🛠️ Technologies Used
* **Python**
* **Streamlit** (For the web interface)
* **Google Gemini API** (For the AI's brain)
* **GitHub Codespaces** (As a cloud development environment)

# 🤖 Development Methodology & Transparency
This project adopts an **AI-First approach**, where I acted as the Technical Product Manager and Prompt Engineer.

* **Core Logic (Human-in-the-Loop):** The Python code was generated with the assistance of **Google Gemini**, guided by my specific architectural requirements (the "Mother-Persona" system). I was responsible for supervising, reviewing, and iterating on the code to ensure the logic met the project's ethical goals.
* **Frontend (Manual Effort):** The CSS styling was manually written by me to achieve a custom look and dark theme (currently a work in progress), demonstrating a desire to customize the interface beyond standard Streamlit defaults.
* **Educational Goal:** The primary focus of this prototype was to exercise **Product Conception** and **Prompt Engineering**, leveraging AI as a tool to accelerate the coding phase while maintaining strict human control over the final output.

# 🏃‍♀️ How to Run the Prototype
This project was developed to run easily on GitHub Codespaces or locally.

### 1. Installation
* Clone or open this repository.
* Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 2. API Configuration (Choose one method)
* **Method A (Easy - UI):** simply run the app. You will be able to enter your Google Gemini API Key securely in the sidebar.
* **Method B (Developer):** Create a folder named `.streamlit` and a file inside it named `secrets.toml`. Paste your key there: `GEMINI_API_KEY = "YOUR_KEY_HERE"`.

### 3. Run the App
In the terminal, run:
```bash
streamlit run app.py
```
Streamlit will notify you to open the application in a new browser tab.

# 📆 Next Steps (Future Phases)
* [Phase 1 - Media]: Expand the prototype to connect to real databases (like Common Sense Media) to validate the filters.

* [Phase 2 - Style and Shopping]: Implement Computer Vision (CV) so the AI can analyze photos of clothes and recommend outfits based on styles (Cottage Core, Y2K).

* [Phase 3 - The Robot]: Build the "Invisible Robot" (backend worker) to perform data collection and topic discovery in real-time.
