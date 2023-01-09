import pandas as pd
import requests
import io
import urls



def fetch_and_read_csv(url):
    # Fetch the CSV file from the URL
    response = requests.get(url).content
    # Create a file-like object from the response content
    csv_file = io.BytesIO(response)
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    return df

def fetch_and_read_excel(url):
    response = requests.get(url).content
    test_file = io.BytesIO(response)
    xl_df = pd.read_excel(test_file)
    return xl_df
  
     
def get_df():
    # Fetch File
    drop_df = fetch_and_read_csv(urls.drop_url)
    # Convert to Numpy array
    drop_df = pd.to_numeric(drop_df['Drop_id'],errors='coerce')

    return drop_df


def prep_opo(df):
     # Return only relevant columns
    df = df[['Qty','Option Name','Feat ID#','Option Total']]

    # drop empty values
    df1 = df.dropna('index')

    # Rename "Feat ID#" to "Part ID"
    df2 = df1.rename(columns={"Feat ID#": "Part ID"})
    
    return df2

def process_opo(df):

    mask = ~df['Part ID'].isin(get_df())

    # Drop the unnecessary Part ID's
    df = df[mask]

    # Sort Option Name A-Z and reset index
    df = df.sort_values('Option Name')
    df = df.reset_index(drop=True)

    return df 




