import streamlit as st
from recommender import get_recommendations, is_eligible
from ollama_api import fetch_ollama_suggestion
from chatbot import chat_with_ollama

st.set_page_config(page_title="AI Education Consultant")

st.title("🎓 Education Consultant - AI/ML/DL Project")
st.write("Get personalized computer science course recommendations with AI support.")

# =====================
# Recommendation Form
# =====================
name = st.text_input("Enter your Name")
father_name = st.text_input("Enter your Father Name")
degree = st.text_input("Enter your Bachelor Degree (e.g., BSCS, BSSE, BSIT)")
skills = st.text_input("Enter your Skills (comma-separated)")
goals = st.text_input("Enter your Career Goals")
experience = st.number_input("Experience in Skills (Years)", min_value=0, max_value=50, step=1)

if st.button("Get Recommendations"):
    if not all([name, father_name, degree, skills, goals]):
        st.warning("Please fill all fields.")
    else:
        st.subheader("👤 Student Profile")
        st.write(f"**Name:** {name}")
        st.write(f"**Father Name:** {father_name}")
        st.write(f"**Degree:** {degree}")
        st.write(f"**Skills:** {skills}")
        st.write(f"**Goals:** {goals}")
        st.write(f"**Experience:** {experience} year(s)")

        if not is_eligible(degree):
            st.error("❌ Only computer-related students are allowed.")
        else:
            st.success("✅ Eligible! Here are your recommended courses:")

            recommendations = get_recommendations(degree, skills)
            for idx, rec in enumerate(recommendations, 1):
                st.write(f"{idx}. {rec}")

            prompt = (
                f"Suggest a short personalized learning path for a {degree} student "
                f"with skills in {skills} who wants to become a {goals}."
            )

            with st.spinner("🤖 Getting AI suggestion..."):
                suggestion = fetch_ollama_suggestion(prompt, delay_seconds=2)

            st.subheader("🤖 AI Suggestion")
            st.write(suggestion)

# =====================
# Chatbot Section
# =====================
st.divider()
st.subheader("💬 Chatbot with Ollama")
chat_with_ollama()
