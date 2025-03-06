import streamlit as st
st.set_page_config(page_title="growth mindset project", page_icon="🧠")
st.title("Growth Mindset Challenge: Web App with Streamlit")
st.header("Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential."
"This AI-powered app helps you to build a growth mindset with reflection,challenges,and achievements!✵")

st.header("⁂ Today's Growth Mindset Quote")
st.write(" Imagination is more important than knowledge,The important thing is not to stop questioning,"
"Anyone who has never made a mistake has never tried anything new,"
" and Life is like riding a bicycle. To keep your balance, you must keep moving.")

st.header("🕊 What's Your Challenge Today?")
user_input = st.text_input("Describe a Challenge you 're facing:")

if user_input:
    st.success(f"💪you 're facing: {user_input}. Keep pushing forward towards your goal!▶")

else:
    st.warning("Tell us about your challenge to get started!")

    st.header(" Reflect on Your Learning" )
    reflection = st.text_area("Write your reflections here:")

    if reflection:
        st.success(f"✨Great Insight! Your reflection: {reflection}")
    else:
        st.info("Reflection on past experience help you grow! Share your difficulties")
st.header("Celebrate your wins!")
acheivement = st.text_input("Share something you've recently accomplished.")
if acheivement:
  st.success(f"Amazing! You achieved:{acheivement}")
else:
  st.info("Big or small , every acheivement counts! Share one now")

st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination")
st.write("Created by Rt_Kumari")