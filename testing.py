import zipfile
import pandas as pd

# Create a new zip file
zip_filename = "processed_files.zip"
zip_file = zipfile.ZipFile(zip_filename, "w")

for i, uploaded_file in enumerate(uploaded_files):
    filename = uploaded_file.name
    df = pd.read_excel(uploaded_file, header=4)
    df = functions.prep_opo(df)  
    df = functions.process_opo(df)
    df['Part ID'] = df['Part ID'].astype(int)
    df = df.round(2)
    st.write("File Cleaned")

    if not df.empty:
        clean_df = functions.convert_df(df)
        new_filename = f"{filename.split('.')[0]}_clean.csv"

        # Write the cleaned file to a temporary file
        temp_file = NamedTemporaryFile(mode="w", suffix=".csv", delete=False)
        clean_df.to_csv(temp_file.name, index=False)
        temp_file.close()

        # Add the temporary file to the zip file
        zip_file.write(temp_file.name, arcname=new_filename)

# Close the zip file
zip_file.close()

if st.download_button(
  label='Download Zip File',
  file_path=zip_filename,
  mime='application/zip'):  
  st.write('Zip file downloaded!')
