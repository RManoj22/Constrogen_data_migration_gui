import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def show_item_info(root, df1, df2, current_row_index, s_no_value=None):
    global s_no_entry

    if df1 is not None and df2 is not None:
        # Clear previous window contents
        for widget in root.winfo_children():
            widget.destroy()

        # Adjust window size for the detailed view
        root.geometry("800x500")

        # Create a frame for the information
        info_frame = tk.Frame(root)
        info_frame.pack(pady=20)

        # Create a frame for left side fields
        left_frame = tk.Frame(info_frame)
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        # Create a frame for right side fields
        right_frame = tk.Frame(info_frame)
        right_frame.grid(row=0, column=1, padx=10, pady=5, sticky="n")

        # Use grid layout for right_frame to align labels and fields horizontally
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_rowconfigure(1, weight=1)
        right_frame.grid_rowconfigure(2, weight=1)
        right_frame.grid_rowconfigure(3, weight=1)
        right_frame.grid_rowconfigure(4, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_columnconfigure(1, weight=2)

        if 0 <= current_row_index < len(df1):
            # Fetch the SNo, ItemName, and ItemID values from df1
            s_no_value = df1['SNo'].iloc[current_row_index]  # Fetch SNo value
            item_id_value = df1['ItemID'].iloc[current_row_index]
            item_name_value = df1['ItemName'].iloc[current_row_index]
            old_item_type_value = df1['ItemTypeName'].iloc[current_row_index]

            # Check for matching items in df2
            if 'Item' in df2.columns:
                item_matches = df2[df2['Item'] == item_name_value]
                if not item_matches.empty:
                    new_value_found = "Yes"
                    item_description = item_matches['Item'].values[0]
                    item_key_value = item_matches['Item key'].values[0] if 'Item key' in df2.columns else "N/A"
                    item_type_value = item_matches['Item type'].values[0] if 'Item type' in df2.columns else "N/A"
                    item_sub_type_value = item_matches['Item sub type'].values[
                        0] if 'Item sub type' in df2.columns else "N/A"
                    item_purpose_value = item_matches['Purpose'].values[0] if 'Purpose' in df2.columns else "N/A"
                    item_specifications_value = item_matches['Item specifications'].values[
                        0] if 'Item specifications' in df2.columns else "N/A"
                else:
                    new_value_found = "No"
                    item_description = "Not Found"
                    item_key_value = "N/A"
                    item_type_value = "N/A"
                    item_sub_type_value = "N/A"
                    item_purpose_value = "N/A"
                    item_specifications_value = "N/A"
            else:
                new_value_found = "Item column not found in second file"
                item_description = "N/A"
                item_key_value = "N/A"
                item_type_value = "N/A"
                item_sub_type_value = "N/A"
                item_purpose_value = "N/A"
                item_specifications_value = "N/A"

            tk.Label(left_frame, text="S.No:").grid(
                row=0, column=0, padx=10, pady=5, sticky="w")
            s_no_entry = tk.Entry(left_frame, width=30)
            s_no_entry.grid(row=0, column=1, padx=10, pady=5)
            s_no_entry.insert(0, str(s_no_value))

            tk.Label(left_frame, text="ItemID:").grid(
                row=1, column=0, padx=10, pady=5, sticky="w")
            item_id_entry = tk.Entry(left_frame, width=30)
            item_id_entry.grid(row=1, column=1, padx=10, pady=5)
            item_id_entry.insert(0, item_id_value)
            item_id_entry.config(state="readonly")

            tk.Label(left_frame, text="ItemName:").grid(
                row=2, column=0, padx=10, pady=5, sticky="w")
            item_name_entry = tk.Entry(left_frame, width=30)
            item_name_entry.grid(row=2, column=1, padx=10, pady=5)
            item_name_entry.insert(0, item_name_value)
            item_name_entry.config(state="readonly")

            tk.Label(left_frame, text="ItemType:").grid(
                row=3, column=0, padx=10, pady=5, sticky="w")
            old_item_type_entry = tk.Entry(left_frame, width=30)
            old_item_type_entry.grid(row=3, column=1, padx=10, pady=5)
            old_item_type_entry.insert(0, old_item_type_value)
            old_item_type_entry.config(state="readonly")

            tk.Label(left_frame, text="New Value Found:").grid(
                row=4, column=0, padx=10, pady=5, sticky="w")
            new_value_entry = tk.Entry(left_frame, width=30)
            new_value_entry.grid(row=4, column=1, padx=10, pady=5)
            new_value_entry.insert(0, new_value_found)
            new_value_entry.config(state="readonly")

            tk.Label(right_frame, text="Item description:").grid(
                row=0, column=0, padx=10, pady=5, sticky="w")
            item_description_entry = tk.Entry(right_frame, width=30)
            item_description_entry.grid(row=0, column=1, padx=10, pady=5)
            item_description_entry.insert(0, item_description)
            item_description_entry.config(state="readonly")

            tk.Label(right_frame, text="Item Key:").grid(
                row=1, column=0, padx=10, pady=5, sticky="w")
            item_key_entry = tk.Entry(right_frame, width=30)
            item_key_entry.grid(row=1, column=1, padx=10, pady=5)
            item_key_entry.insert(0, item_key_value)
            item_key_entry.config(state="readonly")

            tk.Label(right_frame, text="Item Type:").grid(
                row=2, column=0, padx=10, pady=5, sticky="w")
            item_type_entry = tk.Entry(right_frame, width=30)
            item_type_entry.grid(row=2, column=1, padx=10, pady=5)
            item_type_entry.insert(0, item_type_value)
            item_type_entry.config(state="readonly")

            tk.Label(right_frame, text="Item Sub Type:").grid(
                row=3, column=0, padx=10, pady=5, sticky="w")
            item_sub_type_entry = tk.Entry(right_frame, width=30)
            item_sub_type_entry.grid(row=3, column=1, padx=10, pady=5)
            item_sub_type_entry.insert(0, item_sub_type_value)
            item_sub_type_entry.config(state="readonly")

            tk.Label(right_frame, text="Item Purpose:").grid(
                row=4, column=0, padx=10, pady=5, sticky="w")
            item_purpose_entry = tk.Entry(right_frame, width=30)
            item_purpose_entry.grid(row=4, column=1, padx=10, pady=5)
            item_purpose_entry.insert(0, item_purpose_value)
            item_purpose_entry.config(state="readonly")

            tk.Label(right_frame, text="Item Specifications:").grid(
                row=5, column=0, padx=10, pady=5, sticky="w")
            item_specifications_entry = tk.Entry(right_frame, width=30)
            item_specifications_entry.grid(row=5, column=1, padx=10, pady=5)
            item_specifications_entry.insert(0, item_specifications_value)
            item_specifications_entry.config(state="readonly")

            button_frame = tk.Frame(root)
            button_frame.pack(pady=10)

            search_button = tk.Button(
                button_frame, text="Search", command=lambda: search_action(root, df1, df2, current_row_index, s_no_entry))
            search_button.grid(row=0, column=0, padx=5)

            prev_button = tk.Button(button_frame, text="Prev", command=lambda: prev_action(
                root, df1, df2, current_row_index))
            prev_button.grid(row=0, column=1, padx=5)

            save_button = tk.Button(
                button_frame, text="Save", command=lambda: save_action(s_no_value, item_type_value, item_name_value, new_value_found, item_sub_type_value, item_description, item_id_value, item_key_value, item_specifications_value))
            save_button.grid(row=0, column=2, padx=5)

            next_button = tk.Button(button_frame, text="Next", command=lambda: next_action(
                root, df1, df2, current_row_index))
            next_button.grid(row=0, column=3, padx=5)

            close_button = tk.Button(root, text="Close", command=root.quit)
            close_button.pack(pady=10)

        else:
            tk.Label(root, text="Index out of range").pack()


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
            show_item_info(root, df1, df2, matching_row_index)
        else:
            # No matching row found
            tk.messagebox.showerror("Error", "S.No not found in the data.")
    else:
        # Invalid SNo value
        tk.messagebox.showerror("Error", "Invalid S.No value.")


def prev_action(root, df1, df2, current_row_index):
    if df1 is not None and current_row_index > 0:
        current_row_index -= 1
        show_item_info(root, df1, df2, current_row_index)




def save_action(s_no_value, old_item_type_value, old_item_name_value, new_value_found, new_item_sub_type_value, new_item_description, old_item_id_value, new_item_key_value, new_item_specifications_value):
    result = messagebox.askyesno(
        "Save Confirmation", "Are you sure you want to save?")
    
    if result:
        # Create a dictionary with the data
        data = {
            "S.No": [s_no_value],
            "Old Item Type": [old_item_type_value],
            "Old Item Name": [old_item_name_value],
            "New Value Found": [new_value_found],
            "New Item Sub Type": [new_item_sub_type_value],
            "New Item Description": [new_item_description],
            "Old Item ID": [old_item_id_value],
            "New Item Key": [new_item_key_value],
            "New Item Specifications": [new_item_specifications_value]
        }
        
        # Create a DataFrame
        df = pd.DataFrame(data)
        
        # Define the file path
        file_path = 'saved_data.xlsx'
        
        # Check if the file already exists
        if os.path.isfile(file_path):
            # If it exists, append to it
            with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
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
        show_item_info(root, df1, df2, current_row_index)
