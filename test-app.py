import streamlit as st
import pandas as pd 
import numpy as np

st.write("""
Test Documentation
""")
with st.chat_message("user"):
 st.write("Hello!")
 st.line_chart(np.random.randn(100,2))

st.chat_input("Say something!")

with st.container():
  st.chat_input("Say Something!")

x = st.slider("Select a value")
st.write(x, "squared is", x * x)


tab1, tab2, tab3 = st.tabs(["Star Experience", "Rockin' Spa", "Olivia's Oasis"])
