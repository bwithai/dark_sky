import os
import time
import pandas as pd
import re
from tqdm import tqdm
from utils import get_person_data_from_dataframe

# Define ANSI escape codes for colors
GREEN = '\033[92m'
END = '\033[0m'

data_directory = 'data'

for filename in os.listdir(data_directory):
    if filename.endswith('.xlsx'):
        print(filename, " is in progress.....")

        # Read the Excel file into a DataFrame
        start = time.time()
        df = pd.read_excel(os.path.join(data_directory, filename))

        # Now, you can work with the DataFrame 'df'

        total_rows = len(df)  # Get the total number of rows
        batch = []  # Initialize an empty batch list

        # Use tqdm to create a colorful progress bar with percentage
        for index, row in tqdm(df.iterrows(), desc=f"{GREEN}Inserting rows{END}", total=total_rows, ncols=100):
            # You can access the data from the DataFrame 'row' variable

            person_data = get_person_data_from_dataframe(row)  # Implement this function
            if person_data:
                print(person_data)
                break
            else:
                print("_______")
                continue


        #     batch.append(person_data.as_dict())  # Add the person to the batch
        #
        #     if len(batch) >= batch_size:
        #         # Insert the batch into the collection
        #         result = collection.insert_many(batch)
        #         batch = []  # Clear the batch after insertion
        #
        # # Insert any remaining rows in the batch
        # if batch:
        #     result = collection.insert_many(batch)

        end = time.time()
        print(f"Processing time for {filename}: {end - start} seconds")
