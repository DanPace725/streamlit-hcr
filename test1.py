import pandas as pd
import streamlit as st
import openpyxl
from drop_file import fetch_and_read_csv


# Header
with st.container():
  st.title("Hard Card Reconciliation")
  st.subheader("...Work in Progress...")
  st.write(
    "This App should allow you to download an excel file that shows a list of option on a Sales Order that doesn't appear on the BOM"
  )

# Read drop file from URL
drop_file_url = 'https://github.com/DanPace725/streamlit-hcr/blob/main/files/IDs_To_Delete.xlsx'
drop_df = pd.read_excel(drop_file_url,
                        engine='openpyxl',
                        converters={'Drop_id': pd.to_numeric})

# Read input file
input_file = st.file_uploader("Upload an Excel file", type="xlsx")
df = pd.read_excel(input_file,
                   header=4,
                   usecols=['Qty', 'Option Name', 'Feat ID#', 'Option Total'])

# Drop empty values
df = df.dropna('index')

# Convert 'Feat ID#' column to numeric
df['Feat ID#'] = pd.to_numeric(df['Feat ID#'], errors='coerce')

# Merge data frames
merged_df = pd.merge(df,
                     drop_df,
                     left_on='Feat ID#',
                     right_on='Drop_id',
                     how='left')

# Drop rows with NaN in 'Drop_id' column
merged_df = merged_df[merged_df['Drop_id'].notna()]

# Group by 'Option Name' and 'Feat ID#'
grouped_df = merged_df.groupby(['Option Name', 'Feat ID#'])

# Calculate sum of 'Option Total' column
summed_df = grouped_df['Option Total'].sum().reset_index()

# Sort by 'Option Name' and 'Feat ID#'
sorted_df = summed_df.sort_values(['Option Name', 'Feat ID#'])

# Get serial number
serial = st.text_input('Enter serial number:', '15345')

# Set file names
input_file_name = serial + '.xlsx'
output_file_name = serial + '_clean' + '.xlsx'

# Write output to Excel file
sorted_df.to_excel(output_file_name, index=False)

# Download output file
st.download(output_file_name)
