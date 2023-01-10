import pandas as pd
import streamlit as st
import functions
import mimetypes




# Header
with st.container():
  st.title("Hard Card Reconciliation")
  st.subheader("...Work in Progress...")
  st.write("So far this app takes in an uploaded Excel file and processes it to a certain point.")
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
st.write("Upload an Excel File to convert to a data frame below")


# Input Serial number and define naming logic
serial_input = st.text_input("Enter Serial Number Here")
serial = serial_input
output_filename = serial + "_clean" + ".xlsx"


# Upload the Sales Order
uploaded_file = st.file_uploader("Choose a file")

df = None
df2 = None
clean_df = None
filename = None
mimetype, _ = None

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, header=4)
    st.write(df)
else: 
  text = "Upload an excel file"
  colored_text = f"<span style='color:blue'>{text}</span>"
  st.write(colored_text, unsafe_allow_html=True)

process = st.button("Process", help="Press this when you've loaded the correct file")

if process:
  df1 = functions.prep_opo(df)  
  df2 =functions.process_opo(df1)
  df2['Part ID'] = df2['Part ID'].astype(int)
  df2 = df2.round(2)
  st.write("Well if you're reading this something happened. Don't hold your breath")
  st.write(df2)
  

  if df2 is not None:
    #clean_df = df2.to_excel(output_filename, index=False)
    
    #st.write("The file has been saved as an excel file with the name " + output_filename)
    clean_df = functions.convert_df(df2)
   
    filename = serial + ".csv"
    mimetype, _ = mimetypes.guess_type(filename)
    st.write("Yay! Good job Kronk!")


if st.download_button(
  label='Download cleaned file',
  data=clean_df, 
  file_name= filename,
  mime=mimetype):  
  st.write('File downloaded!')

