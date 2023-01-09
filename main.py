import pandas as pd
import streamlit as st
import functions



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
  

# Success Message
if functions.get_df is None: 
  text = "Error: There's a problem with the drop file"
  colored_text = f"<span style='color:red'>{text}</span>"
  st.write(colored_text, unsafe_allow_html=True)
else: 
  st.write("Successfully read Drop File")

# Instruction Text
st.write("Upload an Excel File to convert to a data frame below")

# Test File
st.download_button(
  label="Download Test File", 
  data = functions.convert_excel,
  mime="application/vnd.ms-excel")

# Upload the Sales Order
uploaded_file = st.file_uploader("Choose a file")

df = []

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, header=4)
    st.write(df)
else: 
  text = "Upload an excel file"
  colored_text = f"<span style='color:blue'>{text}</span>"
  st.write(colored_text, unsafe_allow_html=True)

process = st.button("Process", help="Press this when you've loaded the correct file")

if process:
  # functions.prep_opo(df)
  # functions.process_opo(df)
  st.write("Well if you're reading this something happened. Don't hold your breath")

