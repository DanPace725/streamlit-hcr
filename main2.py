# Import Libraries
import pandas as pd
import streamlit as st
import functions
import mimetypes
import zipfile
import io
import tempfile



# Header
with st.container():
  st.title("Hard Card Reconciliation")
  st.subheader("Version: A.01")
  st.write("This web app will process the Options Per Order file and will download a .csv file for further processing.")
  

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


# Upload Files
uploaded_files = st.file_uploader("Choose multiple files", type=["xlsx"], accept_multiple_files=True)

if len(uploaded_files) > 0:
    st.write("Excel Files Read Successfully")
else: 
  text = "Upload excel files"
  colored_text = f"<span style='color:blue'>{text}</span>"
  st.write(colored_text, unsafe_allow_html=True)

process = st.button("Process", help="Press this when you've loaded the correct files")

if process:
 # Create a new zip file
  zip_filename = "processed_files.zip"
  zip_file = zipfile.ZipFile(zip_filename, "w")

  # Loop through files and process each one
  for i, uploaded_file in enumerate(uploaded_files):
      filename = uploaded_file.name
      df = pd.read_excel(uploaded_file, header=4)
      df = functions.prep_opo(df)  
      df = functions.process_opo(df)
      df['Part ID'] = df['Part ID'].astype(int)
      df = df.round(2)
      st.write("File Cleaned")

      if not df.empty:
          clean_df = df
          new_filename = f"{filename.split('.')[0]}_clean.csv"

          # Write the cleaned file to a temporary file
          temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False)
          clean_df.to_csv(temp_file.name, index=False)
          temp_file.seek(0)
          # Add the temporary file to the zip file
          zip_file.write(temp_file.name, arcname=new_filename)
          temp_file.close()

  # Close the zip file
  zip_file.close()
  with open(zip_filename, 'rb') as f:
    zip_data = f.read()

  if st.download_button(
    label='Download Zip File',
    data=zip_data,
    file_name=zip_filename,
    mime='application/zip'):  
    st.write('Zip file downloaded!')
 



