import streamlit as st
import random

# --- Logo zentriert ---
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/6/6c/Star_Wars_Logo.svg' width='400'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Trennlinie ---
st.markdown("<hr style='border: 1px solid #444;'>", unsafe_allow_html=True)

# --- Zentrierter Header als HTML ---
st.markdown(
    "<h2 style='text-align: center; color: white;'>Möge die Macht mit dir sein!</h2>",
    unsafe_allow_html=True
)