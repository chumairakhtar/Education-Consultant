import streamlit as st
from ollama_api import fetch_ollama_suggestion

def chat_with_ollama():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_message = st.text_input("You:", key="chat_input")

    if st.button("Send", key="chat_send"):
        if user_message.strip():
            prompt = (
                "You are a helpful education consultant.\n"
                f"User says: {user_message}\n"
                "Respond clearly."
            )

            with st.spinner("🤖 Thinking..."):
                reply = fetch_ollama_suggestion(prompt, delay_seconds=1)

            st.session_state.chat_history.append(("You", user_message))
            st.session_state.chat_history.append(("Ollama", reply))

    for role, message in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**🧑 You:** {message}")
        else:
            st.markdown(f"**🤖 Ollama:** {message}")
