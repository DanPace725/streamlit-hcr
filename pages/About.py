import streamlit as st
text_md = """ So far it does the following things:
    - Returns only certain headers
    - Drops blank values
    - Renames "Feat ID#" to "Part ID"
    - Returns Modified Dataframe
    - Processes multiple files
    - Allows for downloading processed files
     """
st.write(text_md)