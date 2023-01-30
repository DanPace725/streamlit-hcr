# Import Libraries
import pandas as pd
import streamlit as st
import functions
import mimetypes


# Header
with st.container():
  st.title("Hard Card Reconciliation")
  st.subheader("Version: A.01")
  st.write("This web app will process the Options Per Order file and will download a .csv file for further processing.")
  text_md = """ So far it does the following things:
    - Returns only certain headers
    - Drops blank values
    - Renames "Feat ID#" to "Part ID"
    - Returns Modified Dataframe """
  st.write(text_md)

# Sidebar ----
with st.sidebar:
  st.subheader("IDs to Drop")
  st.table(functions.get_df())

# Success Message
if functions.get_df is None: 
  text = "Error: There's a problem with the drop file"
  colored_text = f"<span style='color:red'>{text}</span>"
  st.write(colored_text, unsafe_allow_html=True)
else: 
  st.write("Successfully read Drop File")

# Instruction Text
st.write("Input the Serial number")

# Input Serial number and define naming logic
serial_input = st.text_input("Enter Serial Number Here")
serial = serial_input
output_filename = serial + "_clean" + ".xlsx"

uploaded_files = st.file_uploader("Choose multiple files", type=["xlsx"], multiple=True)

if len(uploaded_files) > 0:
    st.write("Excel Files Read Successfully")
else: 
  text = "Upload excel files"
  colored_text = f"<span style='color:blue'>{text}</span>"
  st.write(colored_text, unsafe_allow_html=True)

process = st.button("Process", help="Press this when you've loaded the correct files")

if process:
  for i, uploaded_file in enumerate(uploaded_files):
    df = pd.read_excel(uploaded_file, header=4)
    df1 = functions.prep_opo(df)  
    df2 = functions.process_opo(df1)
    df2['Part ID'] = df2['Part ID'].astype(int)
    df2 = df2.round(2)
    st.write("Well if you're reading this something happened. Don't hold your breath")
    st.write("File Cleaned")
  
    if df2 is not None:
      clean_df = functions.convert_df(df2)
      filename = f"{i}_{serial}.csv"
    
      if st.download_button(
        label='Download cleaned file',
        data=clean_df, 
        file_name= filename,
        mime='text/csv'):  
        st.write('File downloaded!')
        st.write("Tada!")
