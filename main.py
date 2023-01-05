import pandas as pd
import openpyxl
import streamlit as st
from functions import fetch_and_read_csv
import variables

# Header
with st.container():
  st.title("Hard Card Reconciliation")
  st.subheader("...Work in Progress...")
  st.write("This App is my second attempt to get a csv file read from github.")

# Sidebar ----
with st.sidebar:
  read_csv = st.checkbox(
    "Read CSV File")
  upload_file = st.checkbox(
    "Upload a file")
  
# Fetch File
df = fetch_and_read_csv(variables.url)

# Success Message
if df.empty: 
  st.write("There's a problem with the drop file")
else: 
  st.write("Successfully read Drop File")

# Upload the Sales Order
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  dataframe = pd.read_excel(uploaded_file)
  st.write(dataframe)