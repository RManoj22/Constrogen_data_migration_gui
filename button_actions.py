import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def search_action(root, df1, df2, current_row_index, s_no_entry):
    s_no_value = s_no_entry.get()

    # Check if s_no_value is a valid integer
    if s_no_value.isdigit():
        s_no_value = int(s_no_value)

        # Find the row in df1 where 'SNo' matches s_no_value
        matching_row = df1[df1['SNo'] == s_no_value]

        if not matching_row.empty:
            # Get the index of the first matching row (assuming SNo is unique)
            matching_row_index = matching_row.index[0]

            # Call show_item_info with the found index
            return root, df1, df2, matching_row_index
        else:
            # No matching row found
            tk.messagebox.showerror("Error", "S.No not found in the data.")
    else:
        # Invalid SNo value
        tk.messagebox.showerror("Error", "Invalid S.No value.")


def prev_action(root, df1, df2, current_row_index):
    if df1 is not None and current_row_index > 0:
        current_row_index -= 1
        return root, df1, df2, current_row_index


def save_action(s_no_value, item_type_combobox, item_name_entry, new_value_found, sub_type_combobox, item_description_combobox, old_item_id_value, new_item_key, new_item_specifications, match_found):
    # Retrieve current values from the comboboxes and entry fields
    current_item_type = item_type_combobox.get()  # Get selected item type
    current_item_name = item_name_entry.get()  # Get entered item name
    current_sub_type = sub_type_combobox.get()  # Get selected sub-type
    current_item_description = item_description_combobox.get()  # Get selected description
    current_item_spec_value = new_item_specifications.get()  # Get selected description
    current_item_key_value = new_item_key.get()  # Get selected description

    result = messagebox.askyesno(
        "Save Confirmation", "Are you sure you want to save?")

    if result:
        # Create a dictionary with the collected data
        data = {
            "S.No": [s_no_value],
            "Current Item Type": [current_item_type],
            "Current Item Name": [current_item_name],
            "New Value Found": [new_value_found],
            "Current Sub Type": [current_sub_type],
            "Current Item Description": [current_item_description],
            "Old Item ID": [old_item_id_value],
            "New Item Key": [current_item_key_value],
            "New Item Specifications": [current_item_spec_value],
            "Match not found": [match_found]
        }

        # Create a DataFrame
        df = pd.DataFrame(data)

        # Define the file path
        file_path = 'saved_data.xlsx'

        # Check if the file already exists
        if os.path.isfile(file_path):
            # If it exists, append to it
            with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False,
                            header=False, startrow=writer.sheets['Sheet1'].max_row)
        else:
            # If it does not exist, create it
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)

        print("Data saved:", data)
    else:
        print("Save operation canceled")


def next_action(root, df1, df2, current_row_index):
    if df1 is not None and current_row_index < len(df1) - 1:
        current_row_index += 1
        return root, df1, df2, current_row_index
