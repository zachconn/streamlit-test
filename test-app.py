import streamlit as st
import pandas as pd 
import numpy as np
import os
import csv

res = pd.read_csv("Experience-Reservation-Streamlit-Test.csv")
st.dataframe(res)

st.write("""
Test Documentation
""")
with st.chat_message("user"):
 st.write("Hello!")
 st.line_chart(np.random.randn(100,2))

st.chat_input("Say something!")

with st.container():
  st.chat_input("Say Something!")

child_first_name = st.text_input("Child's First Name")
child_last_name = st.text_input("Child's Last Name")
experience_type = st.selectbox("Which experience would you like to book today?", ("Star Making", "Star Viewing", "Rockin' Spa", "Olivia's Oasis"))
experience_date = st.date_input("Select a date!")
experience_time = st.time_input("Select a time!")


f = open("Experience-Reservation-Streamlit-Test.csv", 'w')
writer = csv.writer(f, delimiter = ',')
writer.writerow([experience_type, 691329, child_first_name, child_last_name, experience_date, experience_time, "", ""])
f.close()


tab1, tab2, tab3 = st.tabs(["Star Experience", "Rockin' Spa", "Olivia's Oasis"])
