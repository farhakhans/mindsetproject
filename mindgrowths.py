import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="🚀 Mindset Revolution", page_icon="🌟", layout="wide")

# Custom Styling with Gradient Background, Name Animation & Falling Flowers
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            color: white;
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(-10px);}
            to {opacity: 1; transform: translateY(0px);}
        }
        @keyframes bounce {
            0%, 100% {transform: translateY(0);}
            50% {transform: translateY(-10px);}
        }
        @keyframes spin {
            from {transform: rotate(0deg);}
            to {transform: rotate(360deg);}
        }
        @keyframes pulse {
            0% {transform: scale(1);}
            50% {transform: scale(1.1);}
            100% {transform: scale(1);}
        }
        @keyframes zoomInOut {
            0% {transform: scale(1);}
            50% {transform: scale(1.3);}
            100% {transform: scale(1);}
        }
        @keyframes fall {
            0% { transform: translateY(-10px) rotate(0deg); opacity: 1; }
            100% { transform: translateY(100px) rotate(180deg); opacity: 0; }
        }
        .title {
            color: #FF6F61;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            animation: fadeIn 2s ease-in;
        }
        .emoji-bounce {
            display: inline-block;
            font-size: 50px;
            animation: bounce 1.5s infinite;
        }
        .emoji-spin {
            display: inline-block;
            font-size: 50px;
            animation: spin 3s linear infinite;
        }
        .emoji-pulse {
            display: inline-block;
            font-size: 50px;
            animation: pulse 2s infinite;
        }
        .highlight {
            background: #ff12;
            color: blue;
            padding: 5px 10px;
            border-radius: 10px;
            font-weight: bold;
            display: inline-block;
            animation: zoomInOut 2s infinite;
        }
        .falling-flower {
            display: inline-block;
            font-size: 30px;
            position: relative;
            animation: fall 2s infinite linear;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Header with Animated Emoji
st.markdown("<h1 class='title'>🚀 Mindset Revolution Hub <span class='emoji-spin'>✨</span></h1>", unsafe_allow_html=True)
st.markdown("<h3><span class='zoom'>Welcome to a New Era of Self-Growth! </sp🌱✨</h3>", unsafe_allow_html=True)
st.markdown("Elevate your mindset with daily motivation, challenges, reflections, and gratitude! <span class='emoji-pulse'>💖</span>", unsafe_allow_html=True)

# Random Quote Generator
quotes = [
    "🌟 The future belongs to those who believe in the beauty of their dreams. —Eleanor Roosevelt",
    "🔥 Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. —Christian D. Larson",
    "🚀 Do what you can, with what you have, where you are. —Theodore Roosevelt",
    "🌈 Start where you are. Use what you have. Do what you can. —Arthur Ashe"
]

st.markdown("---")
st.markdown("<h2>🎭 Daily Boost: Your Inspirational Quote <span class='emoji-bounce'>💡</span></h2>", unsafe_allow_html=True)
st.success(random.choice(quotes))

# Challenge Input
st.markdown("---")
st.markdown("<h2>⚡ Take on Today's Challenge <span class='emoji-spin'>💪</span></h2>", unsafe_allow_html=True)
challenge_input = st.text_input("What's one challenge you want to conquer today? 💪")
if challenge_input:
    st.success(f"🔥 Stay strong! Facing: {challenge_input}. Keep pushing forward! 🚀")
else:
    st.warning("Share your challenge and let's overcome it together! 💡")

# Learning Reflection
st.markdown("---")
st.markdown("<h2>💡 Reflect & Evolve <span class='emoji-pulse'>📖</span></h2>", unsafe_allow_html=True)
reflection = st.text_area("What lessons did you learn from today’s journey? 📝")
if reflection:
    st.success(f"🌱 Insightful! Your reflection: {reflection}")
else:
    st.info("Reflecting is key to growth! Take a moment to pen down your insights. ✍️")

# Achievements Section
st.markdown("---")
st.markdown("<h2>🏅 Celebrate Your Victories <span class='emoji-bounce'>🎉</span></h2>", unsafe_allow_html=True)
achievement = st.text_input("What’s something awesome you accomplished? 🎉")
if achievement:
    st.balloons()
    st.success(f"🎇 Fantastic! You achieved: {achievement}")
else:
    st.info("Every milestone matters! Share your triumphs. 🏆")

# Gratitude Section
st.markdown("---")
st.markdown("<h2>💖 Gratitude Corner <span class='emoji-spin'>🙏</span></h2>", unsafe_allow_html=True)
gratitude = st.text_area("What are you grateful for today? 🌻")
if gratitude:
    st.success(f"🙏 Gratitude noted: {gratitude}. Keep appreciating the little things! 😊")
else:
    st.info("Taking a moment to be thankful creates a positive mindset. 💛")

# Footer with Animated Name & Falling Flowers
st.markdown("---")
st.markdown("""
    <p style='text-align:center; font-size:18px;'>✨ Growth is an exciting journey! Keep soaring higher! <span class='emoji-bounce'>🚀</span></p>
    <p style='text-align:center;'>🔹 <strong>Designed with Passion & Creativity by 
    <span class='highlight'>Farhana Khan</span></strong> 
    <span class='falling-flower'>🌸</span>
    <span class='falling-flower'>🌺</span>
   
    </p>
""", unsafe_allow_html=True)
