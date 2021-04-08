import streamlit as st
from stop_words import get_stop_words

st.write("hello!")
st.write(stop_words.get_stop_words("de"))
