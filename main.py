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
drop_df = fetch_and_read_csv(variables.url)
drop_df = pd.to_numeric(drop_df['Drop_id'],errors='coerce')


# Success Message
if drop_df.empty: 
  st.write("There's a problem with the drop file")
else: 
  st.write("Successfully read Drop File")

# Instruction Text
st.write("Upload and Excel File to convert to a data frame below")

# Upload the Sales Order
uploaded_file = st.file_uploader("Choose a file")



if uploaded_file is not None:
  dataframe = pd.read_excel(uploaded_file)
  st.write(dataframe)