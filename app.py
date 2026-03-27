import streamlit as st
from gemini_helper import generate_study_notes

# --- Page Config ---
st.set_page_config(
    page_title="Study Notes Generator",
    page_icon="📚",
    layout="wide"
)

# --- Sidebar ---
with st.sidebar:
    st.title("📚 About This App")
    st.markdown("---")
    st.write(
        "This app uses Google Gemini AI to instantly generate structured "
        "study notes on any topic you enter."
    )
    st.markdown("**Notes include:**")
    st.markdown("- 📌 Overview\n- 🧠 Key Concepts\n- 🌍 Real-World Example\n- ❓ Practice Questions")
    st.markdown("---")
    st.subheader("🛠️ How to Use")
    st.markdown(
        """
        1. Type a topic in the input box
        2. Click **Generate Notes**
        3. Read your structured notes
        4. Download them as a `.txt` file
        5. Try another topic — history stays for your session!
        """
    )
    st.markdown("---")
    st.caption("Powered by Google Gemini 2.0 Flash · INFO 4330 Project")

# --- Main Area ---
st.title("📝 Study Notes Generator")
st.markdown("Enter a topic below and get AI-generated study notes instantly.")

topic = st.text_input(
    "Enter a topic:",
    placeholder="e.g. Photosynthesis, World War II, Linear Regression"
)

if st.button("Generate Notes", type="primary"):
    if not topic or len(topic.strip()) < 3:
        st.warning("Please enter a topic with at least 3 characters.")
    else:
        with st.spinner("Generating your study notes..."):
            try:
                notes = generate_study_notes(topic.strip())
                st.success("Notes generated!")
                st.markdown("---")
                st.markdown(notes)
                st.markdown("---")

                # --- Download Button ---
                st.download_button(
                    label="⬇️ Download Notes as .txt",
                    data=notes,
                    file_name=f"{topic.strip().replace(' ', '_')}_notes.txt",
                    mime="text/plain"
                )

                # --- Save to Session History ---
                if "history" not in st.session_state:
                    st.session_state.history = []
                if topic.strip() not in st.session_state.history:
                    st.session_state.history.append(topic.strip())

            except Exception as e:
                st.error(f"Something went wrong: {e}")

# --- Session History ---
if "history" in st.session_state and st.session_state.history:
    st.markdown("---")
    st.subheader("🕓 Topics Searched This Session")
    for i, past_topic in enumerate(reversed(st.session_state.history), 1):
        st.write(f"{i}. {past_topic}")