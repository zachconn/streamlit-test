import streamlit as st
import pandas as pd 

st.write("""
Test Documentation
""")
with st.chat_message("user"):
 st.write("Hello!")
 st.line_chart(np.random.randn(100,2))
