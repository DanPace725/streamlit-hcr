from functions import fetch_and_read_csv, process_opo
import pandas as pd

# csv file stored in Github repo

url = "https://raw.githubusercontent.com/DanPace725/streamlit-hcr/main/files/IDs_To_Delete.csv"

# Fetch File
drop_df = fetch_and_read_csv(url)
drop_df = pd.to_numeric(drop_df['Drop_id'],errors='coerce')

