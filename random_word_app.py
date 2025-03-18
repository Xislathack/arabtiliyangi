import streamlit as st
import random

# --- Configuration ---
ADMIN_KEY = "password"  # Replace with a strong secret key
VOCAB_FILE = "vocabulary.txt"  # File to store vocabulary

# --- Functions ---
def get_words_from_file():
    try:
        with open(VOCAB_FILE, "r", encoding="utf-8") as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        return

def save_words_to_file(words):
    with open(VOCAB_FILE, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")

def get_random_word(words):
    if words:
        return random.choice(words)
    else:
        return "No words in vocabulary."

# --- Streamlit App ---
st.title("Vocabulary Explorer")

# --- Initialize session state ---
if 'vocabulary' not in st.session_state:
    st.session_state.vocabulary = []  # Initialize as an empty list
if 'admin_mode' not in st.session_state:
    st.session_state.admin_mode = False
if 'page' not in st.session_state:
    st.session_state.page = "main"

# --- Header ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Vocabulary Explorer")
with col2:
    if st.button("Vocabularies"):
        st.session_state.page = "vocabularies"
    else:
        st.session_state.page = "main"

# --- Main Page ---
if st.session_state.page == "main":
    words = get_words_from_file()
    st.write("## Random Word")
    if st.button("Next Word") or 'word' not in st.session_state:
        st.session_state.word = get_random_word(words)
    st.write(f"## {st.session_state.word}")

    admin_key_input = st.text_input("Enter Admin Key", key="admin_input")  # Added key
    if admin_key_input == ADMIN_KEY:
        st.session_state.admin_mode = True
    else:
        st.session_state.admin_mode = False  # Ensure admin mode is set to False on wrong input

    # --- Admin Section (Conditionally Displayed) ---
    if st.session_state.admin_mode:
        st.subheader("Admin Controls")
        new_word = st.text_input("Add New Word")
        if st.button("Add Word"):
            words = get_words_from_file()
            words.append(new_word)
            save_words_to_file(words)

        words = get_words_from_file()
        if words:
            if words:  # Only show delete options if there are words
                word_to_delete = st.selectbox("Select Word to Delete", words)
                if st.button("Delete Word"):
                    words = get_words_from_file()
                    words.remove(word_to_delete)
                    save_words_to_file(words)

# --- Vocabularies Page ---
elif st.session_state.page == "vocabularies":
    st.subheader("Vocabulary List")
    if st.button("Back to Main"):
        st.session_state.page = "main"

    words = get_words_from_file()
    if words:
        for word in words:
            st.write(f"- {word}")
    else:
        st.write("No vocabulary words added yet.")

# --- Styling ---
st.markdown(
    """
    <style>
    /* ... (Your CSS styles here) ... */
    </style>
    """,
    unsafe_allow_html=True,
)