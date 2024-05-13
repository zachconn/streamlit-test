import streamlit as st
import pandas as pd 
import numpy as np
import os
import csv

if st.button("Logout"):
    st.switch_page("login-page.py")
 
res = pd.read_csv("Experience-Reservation-Streamlit-Test.csv")
st.dataframe(res)

st.write("""
Give Kids The World Experience Reservations
""")
with st.chat_message("user"):
 st.write("Hello!")

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
     res.loc[len(res)] = list1
     
 
st.dataframe(list1)
st.dataframe(res)


tab1, tab2, tab3 = st.tabs(["Star Experience", "Rockin' Spa", "Olivia's Oasis"])
