import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Main Page
st.title("🌌 AI Multiverse Chatbot")
st.write("Talk to different AI personalities!")

# ---------------- Sidebar ----------------
st.sidebar.title("App Settings")

personality = st.sidebar.selectbox(
    "Choose Personality",
    [
        "Helpful Teacher",
        "Expert Hacker",
        "Funny Friend",
        "Panicked College Student",
        "1920s Mafia Boss",
        "Sarcastic Fitness Coach"
    ]
)

intensity = st.sidebar.slider(
    "Intensity Level",
    min_value=1,
    max_value=10,
    value=5
)

# ---------------- Avatar ----------------
if personality == "Helpful Teacher":
    bot_avatar = "👨‍🏫"
elif personality == "Expert Hacker":
    bot_avatar = "💻"
elif personality == "Funny Friend":
    bot_avatar = "😂"
elif personality == "Panicked College Student":
    bot_avatar = "😰"
elif personality == "1920s Mafia Boss":
    bot_avatar = "🕴️"
elif personality == "Sarcastic Fitness Coach":
    bot_avatar = "💪"
else:
    bot_avatar = "🤖"

# ---------------- User Input ----------------
user_message = st.text_input("Say something:")

if st.button("SEND"):

    if user_message:

        ai_instructions = f"""
You are acting as {personality}.

Act with an intensity level of {intensity}/10.

Reply to the user's message in the selected personality.

User message:
{user_message}
"""

        with st.spinner("Connecting to the AI Multiverse..."):

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=ai_instructions
            )

        with st.chat_message("user"):
            st.write(user_message)

        with st.chat_message("assistant", avatar=bot_avatar):
            st.write(response.text)

    else:
        st.warning("Please type a message first.")