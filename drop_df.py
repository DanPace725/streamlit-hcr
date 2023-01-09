
import functions
import variables
import pandas as pd 

# Fetch File
drop_df = functions.fetch_and_read_csv(variables.url)
drop_df = pd.to_numeric(drop_df['Drop_id'],errors='coerce')