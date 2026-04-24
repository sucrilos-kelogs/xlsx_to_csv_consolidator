# Goal:        Code that consolidates all ".xlsx" files within a folder into a single CSV
# Description: Code built using only Pandas, performing a full consolidation into a single file
# Limitations: Because it does everything without using DuckDB for example, there is no way to
#              detect if a previously processed file has been changed — only the addition of new files is detected

import os                          # Used to navigate the root folder
import pandas as pd                # Used to create the DataFrames
from dotenv import load_dotenv     # Used to load environment variables
load_dotenv()                      # Loads environment variables
SOURCE_FOLDER = os.getenv("SOURCE_FOLDER")  # Folder containing the .xlsx files
OUTPUT_FILE   = os.getenv("OUTPUT_FILE")    # Path of the consolidated CSV


df_list = []  # Empty list used to store all DataFrames that are created

# Loop to create each DataFrame and store it in the list
for (path, folder, files) in os.walk(SOURCE_FOLDER):
    for file_name in files:
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(path, file_name)  # Builds the full path of the file
            df = pd.read_excel(file_path)               # Creates a DataFrame from the found file, if it is an ".xlsx"
            df_list.append(df)                          # Adds the created DataFrame to the list

full = pd.concat(df_list)          # Concatenates all created DataFrames
df_full = pd.DataFrame(full)       # Creates a single DataFrame from all DataFrames
df_full.to_csv(OUTPUT_FILE, index=False)  # Exports the consolidated CSV

print(f'✅ Successfully consolidated! {len(df_list)} file(s) processed.')