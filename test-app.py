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

def form_callback(list1):
 with open('Experience-Reservation-Streamlit-Test.csv', 'a+') as f:
  writer = csv.writer(f)
  writer.writerow(list1)

with st.form(key="my_form",clear_on_submit=True):
    
    st.write("Enter Note")
    
    child_first_name = st.text_input("Child's First Name")
    child_last_name = st.text_input("Child's Last Name")
    experience_type = st.selectbox("Which experience would you like to book today?", ("Star Making", "Star Viewing", "Rockin' Spa", "Olivia's Oasis"))
    experience_date = st.date_input("Select a date!")
    experience_time = st.time_input("Select a time!")
    
    submitted = st.form_submit_button("Submit")

    list1 = [experience_type, "", child_first_name, child_last_name, experience_date, experience_time, "", ""]
    if submitted:
     st.write(list1)
     newdf = pd.DataFrame(list1)
     pd.concat([res,newdf])
     form_callback(list1)

st.dataframe(res)


tab1, tab2, tab3 = st.tabs(["Star Experience", "Rockin' Spa", "Olivia's Oasis"])
