import pandas as pd
import os

# Function to match ItemNames from the first file with ItemTypeNAME_x from the second file
def match_item_names(file1, file2):
    # Read the Excel files
    df1 = pd.read_excel(file1)  # First file containing ItemName and ItemID
    df2 = pd.read_excel(file2)  # Second file containing ItemName and ItemTypeNAME_x

    # Initialize a list to store the results
    results = []

    # Loop through each row in the first file
    for index, row in df1.iterrows():
        item_name = row['ItemName']
        item_id = row['ItemID']

        # Search for the ItemName in the second file
        matching_row = df2[df2['ItemNAME'] == item_name]
        if not matching_row.empty:
            # Get the value of ItemTypeNAME_x for the matching row
            item_type_name = matching_row['ItemTypeNAME_x'].values[0]
            results.append({'SNo': index + 1, 'ItemID': item_id,
                           'ItemName': item_name, 'ItemTypeName': item_type_name})

    # Convert the results list to a DataFrame
    result_df = pd.DataFrame(results)

    # Determine the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the output directory, which is one level up from the current directory
    output_directory = os.path.join(current_directory, '..', 'output_files')
    os.makedirs(output_directory, exist_ok=True)  # Create the directory if it does not exist

    # Define the output file path
    output_file = os.path.join(output_directory, 'matched_items_result.xlsx')

    # Write the result to a new Excel file
    result_df.to_excel(output_file, index=False)

    print(f"Matching ItemID, ItemName, and ItemTypeNAME_x values have been written to '{output_file}'.")

# Usage
# First file containing ItemName
file1 = r'D:\IGS\Constrogen_data_mIgration_gui\output_files\final_unique_filtered_stock_record_data.xlsx'
# Second file containing ItemName and ItemTypeNAME_x
file2 = r'D:\IGS\Constrogen_data_mIgration_gui\output_files\old_items_with_item_type\output_with_item_type.xlsx'

match_item_names(file1, file2)
