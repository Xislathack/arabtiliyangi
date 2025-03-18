import streamlit as st
import random

# --- Configuration ---
VOCAB_FILE = "vocabulary.txt"
WORDS_TO_DISPLAY = 4

# --- Functions ---
def get_words_from_file():
    try:
        with open(VOCAB_FILE, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def get_random_words(words, num_words):
    if len(words) >= num_words:
        return random.sample(words, num_words)
    return words

st.markdown(
    """
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic&display=swap" rel="stylesheet">
    </head>

    <style>
        body {
            font-family: 'Noto Naskh Arabic', serif;
        }
        /* You can add more CSS rules here to style other elements */
    </style>
    """,
    unsafe_allow_html=True,
)


# --- Streamlit App ---
st.title("Vocabulary Practice")

words = get_words_from_file()

if "displayed_words" not in st.session_state or st.button("Next Words"):
    st.session_state.displayed_words = get_random_words(words, WORDS_TO_DISPLAY)

if st.session_state.displayed_words:
    cols = st.columns(WORDS_TO_DISPLAY)  # Create 4 columns
    for i, word in enumerate(st.session_state.displayed_words):
        cols[i].write(word)  # Write each word in a column
else:
    st.write("Vocabulary list is empty.")
