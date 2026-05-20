# 💼 Career Advisor Chatbot

An AI-powered Career Advisor Chatbot built using **Google Gemini GenAI API** and **Streamlit**.

This chatbot helps students, freshers, and early-career professionals with career guidance, resume improvement, interview preparation, skill roadmaps, and job role suggestions.

---

## 📌 Project Overview

The main goal of this project is to build a **multi-turn conversational chatbot** for the career guidance domain.

Instead of creating a simple chatbot demo, this project follows a modular and production-style structure where API logic, configuration, prompts, logging, and UI are separated into different files.

---

## 🎯 Domain Selected

### Career Advisor Chatbot

The chatbot can help users with:

- Career guidance
- Resume improvement
- Interview preparation
- Skill roadmaps
- Job role suggestions
- Learning path planning
- Fresher job preparation

---

## 🚀 Features

- Gemini API integration
- Secure API key management using `.env`
- Streamlit chat-style interface
- Multi-turn conversation history
- Structured career guidance responses
- Prompt engineering using system prompts
- Error handling
- Logging of user questions and bot responses
- Modular project structure

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv
- Logging module

---

## 📂 Project Structure

```text
career_chatbot/
│
├── app.py
├── config.py
├── gemini_client.py
├── prompts.py
├── logger.py
├── requirements.txt
├── .gitignore
├── README.md
└── images/
    ├── input.png
    └── output.png
```

---

# 🧠 What We Actually Did Step-by-Step

---

## Step 1: Created the Project Folder

We created a project folder named:

```text
career_chatbot
```

This folder contains all chatbot-related files.

---

## Step 2: Created a Virtual Environment

We created a virtual environment to manage project dependencies separately.

```bash
python -m venv venv
```

Activated it using:

```bash
venv\Scripts\activate
```

---

## Step 3: Installed Required Libraries

We installed the required Python libraries:

```bash
pip install streamlit google-generativeai python-dotenv
```

These libraries are used for:

- `streamlit` → building the chatbot UI
- `google-generativeai` → connecting with Gemini API
- `python-dotenv` → loading API key securely from `.env`

---

## Step 4: Created `.env` File

We created a `.env` file to store the Gemini API key securely.

```text
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

This keeps the API key hidden from the main code.

---

## Step 5: Created `config.py`

The `config.py` file loads environment variables from `.env`.

It stores:

- Gemini API key
- Gemini model name

This helps avoid hardcoding sensitive information inside the code.

---

## Step 6: Created `prompts.py`

The `prompts.py` file contains the system prompt.

This prompt tells the chatbot how to behave as a professional Career Advisor.

It includes rules like:

- give career guidance
- keep answers professional
- use simple language
- focus on freshers and students
- provide practical suggestions

---

## Step 7: Created `gemini_client.py`

The `gemini_client.py` file handles Gemini API communication.

It is responsible for:

- sending user questions to Gemini
- receiving AI-generated responses
- handling API errors
- keeping API logic separate from UI code

---

## Step 8: Created `logger.py`

The `logger.py` file handles logging.

It records:

- user questions
- chatbot responses
- errors

This is useful for debugging and monitoring the chatbot.

---

## Step 9: Created `app.py`

The `app.py` file is the main Streamlit application.

It handles:

- chatbot title
- chat input box
- user messages
- assistant messages
- conversation history
- loading spinner
- displaying responses

This file connects the UI with the Gemini client.

---

## Step 10: Added Multi-turn Conversation

We used:

```python
st.session_state.messages
```

to store chat history.

This allows the chatbot to show previous user and assistant messages during the session.

---

## Step 11: Ran the Application

We ran the chatbot using:

```bash
streamlit run app.py
```

The app opens in the browser and allows users to ask career-related questions.

---

## Step 12: Prepared GitHub Files

We added:

- `README.md`
- `.gitignore`
- `requirements.txt`
- screenshots inside `images/`

We also excluded sensitive and unnecessary files like:

```text
.env
venv/
app.log
__pycache__/
```

---

# 📸 Project Screenshots

## Input Screen

![Input Screen](images/input.png)

---

## Output Screen

![Output Screen](images/output.png)

---

# 💬 Example Questions

Users can ask:

```text
How can I become a Data Analyst?
```

```text
What skills are needed for AI/ML Engineer fresher?
```

```text
How should I answer Tell me about yourself?
```

```text
Create a 30-day roadmap for learning Python and SQL.
```

---

# ▶️ How to Run the Project

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_LINK
cd career_chatbot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Create `.env` File

```text
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

---

## 6. Run Streamlit App

```bash
streamlit run app.py
```

---

# 🔐 Security

The API key is stored in the `.env` file and excluded from GitHub using `.gitignore`.

This prevents the secret key from being exposed publicly.

---

# 📌 Future Improvements

- Add resume upload feature
- Add job role recommendation
- Add PDF resume analyzer
- Store chat history in database
- Deploy on Streamlit Cloud
- Add voice input support

---

# 👨‍💻 Author

## Embadi Anji

- Data Analyst / AI-ML Aspirant
- Python | SQL | Power BI | Machine Learning | GenAI