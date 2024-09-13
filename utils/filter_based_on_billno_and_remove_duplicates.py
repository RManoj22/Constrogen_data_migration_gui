import pandas as pd
import os

# Load the Excel files
df1 = pd.read_excel(r"D:\IGS\Constrogen_data_mIgration_gui\Data_to_get_unique\Filtered bills of all projects.xlsx")
df2 = pd.read_excel(r"D:\IGS\Constrogen_data_mIgration_gui\Data_to_get_unique\All stock records.xlsx")

# Step 1: Filter the rows in df2 where 'BillNO' matches 'BillNo' from df1
filtered_df = df2[df2['BillNO'].isin(df1['BillNo'])]

# Step 2: Remove duplicates based on 'ItemName' column, keeping the first occurrence
df_unique = filtered_df.drop_duplicates(subset='ItemName', keep='first')

# Step 3: Reset index to add S.No column
df_unique.reset_index(drop=True, inplace=True)
df_unique.index += 1  # Make index start from 1
df_unique.index.name = 'S.No'  # Name the index column as 'S.No'

# Determine the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the output directory, which is one level up from the current directory
output_directory = os.path.join(current_directory, '..', 'output_files')
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it does not exist

# Define the output file path
output_file = os.path.join(output_directory, 'final_unique_filtered_stock_record_data.xlsx')

# Step 5: Save the final result to a single output Excel file
df_unique.to_excel(output_file, index_label='S.No')

print(f"Final filtered and unique stock record data stored into {output_file}")
