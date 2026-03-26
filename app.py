import streamlit as st
from gemini_helper import generate_study_notes

# --- Page Config ---
st.set_page_config(page_title="Study Notes Generator", page_icon="📚")

# --- Title ---
st.title("📚 Study Notes Generator")
st.markdown("Enter a topic below and get AI-generated study notes instantly.")

topic = st.text_input("Enter a topic:", placeholder="e.g. Photosynthesis, World War II, Linear Regression")

if st.button("Generate Notes"):
    if not topic or len(topic.strip()) < 3:
        st.warning("Please enter a topic with at least 3 characters.")
    else:
        with st.spinner("Generating your study notes..."):
            try:
                notes = generate_study_notes(topic.strip())
                st.success("Notes generated!")
                st.markdown(notes)
            except Exception as e:
                st.error(f"Something went wrong: {e}")