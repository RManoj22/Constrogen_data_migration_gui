import pandas as pd
import os

# Load the first Excel file with ItemName and ItemTypeID
item_file = 'D:\\IGS\\Constrogen_data_mIgration_gui\\Old_Items_data\\Item Details.xlsx'  # Replace with your first Excel file path
df_items = pd.read_excel(item_file)

# Load the second Excel file with ItemTypeID and ItemType
item_type_file = 'D:\\IGS\\Constrogen_data_mIgration_gui\\Old_Items_data\\Item Type.xlsx'  # Replace with your second Excel file path
df_item_types = pd.read_excel(item_type_file)

# Merge the two DataFrames on ItemTypeID
df_merged = pd.merge(df_items, df_item_types, on='ItemTypeID', how='left')

# Determine the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the output directory, which is one level up from the current directory
output_directory = os.path.join(current_directory, '..', 'output_files', 'old_items_with_item_type')
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it does not exist

# Define the output file path
output_file = os.path.join(output_directory, 'output_with_item_type.xlsx')

# Save the updated DataFrame to a new Excel file
df_merged.to_excel(output_file, index=False)

print(f"Item data with types have been written to {output_file}")
