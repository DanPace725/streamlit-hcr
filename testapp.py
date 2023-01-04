#!/Users/daniel.pace/Documents/.python/python-3.11.1-embed-amd64 python

"""
File: testapp.py

Description: This app will clean work documents and return a file with discrepancies. 

Author: Daniel 

"""

import pandas as pd
import streamlit as st
import warnings
from operator import truediv
warnings.filterwarnings('ignore')

# Header
with st.container():
    st.title ("Hard Card Reconciliation")
    st.subheader("...Work in Progress...")
    st.write("This App should allow you to download an excel file that shows a list of option on a Sales Order that doesn't appear on the BOM")


excel_file = st.file_uploader("Upload an Excel file", type="xlsx")
serial = st.text_input('Enter serial number:', '15345')

# Root file path
file_path = 'C:/Users/daniel.pace/OneDrive - Cavco Industries/Documents/Hard Card Rec/'
# This is where you upload files to process
input_fp = 'C:/Users/daniel.pace/OneDrive - Cavco Industries/Documents/Hard Card Rec/Input/'
# This is where the clean file will be uploaded
output_fp = 'C:/Users/daniel.pace/OneDrive - Cavco Industries/Documents/Hard Card Rec/Output/'

ext = ".xlsx"
input_file_name = serial + ext
output_file_name = serial + '_clean' + ext
input_file = input_fp + input_file_name
output_file = output_fp + output_file_name

drop_f = file_path + 'IDs_To_Delete.xlsx'


def process_file():
    # This reads the excel file that contains the Features we want to drop from the table and converts the numbers to integers. 
    drop_df = pd.read_excel(drop_f)
    drop_df = pd.to_numeric(drop_df['Drop_id'],errors='coerce')

    # Read the input file. 
    # This sets the header to row 4 (starting from 0), effectively dropping the data from above
    df = pd.read_excel(input_file, header=4)

    # display first 5 rows
    #df.head()

    # Return only relevant columns
    df = df[['Qty','Option Name','Feat ID#','Option Total']]

    # drop empty values
    df = df.dropna('index')

    # Rename "Feat ID#" to "Part ID"
    df = df.rename(columns={"Feat ID#": "Part ID"})

    mask = ~df['Part ID'].isin(drop_df)

    # Drop the unnecessary Part ID's
    df = df[mask]

    # Sort Option Name A-Z and reset index
    df = df.sort_values('Option Name')
    df = df.reset_index(drop=True)
    return df 
    
df = process_file()


if st.button('Process file'):
    process_file()
    st.write(df)


if st.button('Download cleaned file'):
    st.markdown('File downloaded!')
    df.to_excel(output_file, index=False)

