import pandas as pd
import requests
import io
from main import drop_df

def fetch_and_read_csv(url):
    # Fetch the CSV file from the URL
    response = requests.get(url).content
    
    # Create a file-like object from the response content
    csv_file = io.BytesIO(response)
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    return df

def process_opo(df):
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




