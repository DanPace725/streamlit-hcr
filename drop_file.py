import pandas as pd
import requests
import io

# Fetch the Excel file from GitHub
url = "https://raw.githubusercontent.com/DanPace725/streamlit-hcr/main/files/IDs_To_Delete.csv"

def fetch_and_read_csv(url):
    # Fetch the CSV file from the URL
    response = requests.get(url).content
    
    # Create a file-like object from the response content
    csv_file = io.BytesIO(response)
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    return df

df = fetch_and_read_csv(url)

print(df.head())



