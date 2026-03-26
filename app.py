import streamlit as st
from gemini_helper import configure_gemini, generate_study_notes

# --- Page Config ---
st.set_page_config(page_title="Study Notes Generator", page_icon="📚")

# --- Title ---
st.title("📚 Study Notes Generator")
st.markdown("Enter a topic below and get AI-generated study notes instantly.")

# --- Load model once (cached) ---
@st.cache_resource
def load_model():
    return configure_gemini()

try:
    model = load_model()
except ValueError as e:
    st.error(f"Configuration error: {e}")
    st.stop()

# --- Input ---
topic = st.text_input(
    "Enter a topic:",
    placeholder="e.g. Decision Trees, Linear Regression, Data Warehousing..."
)

# --- Generate Button ---
if st.button("Generate Notes"):

    # Input validation
    if not topic.strip():
        st.warning("Please enter a topic before generating notes.")
    elif len(topic.strip()) < 3:
        st.warning("Topic is too short. Please be more specific.")
    else:
        with st.spinner("Generating your study notes..."):
            try:
                notes = generate_study_notes(topic.strip(), model)
                st.success("Notes generated!")
                st.markdown("---")
                st.markdown(notes)
            except Exception as e:
                st.error(f"Something went wrong: {e}")