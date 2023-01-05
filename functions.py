import pandas as pd
import requests
import io

def fetch_and_read_csv(url):
    # Fetch the CSV file from the URL
    response = requests.get(url).content
    
    # Create a file-like object from the response content
    csv_file = io.BytesIO(response)
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    return df




