import tkinter as tk
from tkinter import ttk
from button_actions import save_action, search_action, prev_action, next_action

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

        # Grid layout for right_frame
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)

        if 0 <= current_row_index < len(df1):
            # Fetch the relevant fields from df1
            s_no_value = df1['SNo'].iloc[current_row_index]
            item_id_value = df1['ItemID'].iloc[current_row_index]
            old_item_name_value = df1['ItemName'].iloc[current_row_index]
            old_item_type_value = df1['ItemTypeName'].iloc[current_row_index]

            # Check for matching items in df2
            if 'Item' in df2.columns:
                item_matches = df2[df2['Item'] == old_item_name_value]
                match_count = len(item_matches)  # Count number of matches

                # Display the number of matches
                match_count_label = tk.Label(left_frame, text=f"Matches found in df2: {match_count}")
                match_count_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

                if not item_matches.empty:
                    new_value_found = "Yes"

                    # Handle item description
                    if len(item_matches) > 1:
                        # Multiple matches found, create a dropdown
                        item_descriptions = item_matches['Item'].values.tolist()
                        selected_item_description = tk.StringVar(root)
                        selected_item_description.set(item_descriptions[0])  # Set the default value

                        tk.Label(right_frame, text="Matches found:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
                        item_description_dropdown = ttk.Combobox(right_frame, textvariable=selected_item_description, values=item_descriptions, width=30)
                        item_description_dropdown.grid(row=7, column=1, padx=10, pady=5)
                        item_description = selected_item_description.get()
                    else:
                        # Single match found, show as a regular Entry field
                        item_description = item_matches['Item'].values[0]

                    item_key_value = item_matches['Item key'].values[0] if 'Item key' in df2.columns else "N/A"
                    item_type_value = item_matches['Item type'].values[0] if 'Item type' in df2.columns else "N/A"
                    item_sub_type_value = item_matches['Item sub type'].values[0] if 'Item sub type' in df2.columns else "N/A"
                    item_purpose_value = item_matches['Purpose'].values[0] if 'Purpose' in df2.columns else "N/A"
                    item_specifications_value = item_matches['Item specifications'].values[0] if 'Item specifications' in df2.columns else "N/A"
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

            # Display SNo and other details
            tk.Label(left_frame, text="S.No:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
            s_no_entry = tk.Entry(left_frame, width=30)
            s_no_entry.grid(row=0, column=1, padx=10, pady=5)
            s_no_entry.insert(0, str(s_no_value))

            tk.Label(left_frame, text="Old ItemName:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
            item_name_entry = tk.Entry(left_frame, width=30)
            item_name_entry.grid(row=2, column=1, padx=10, pady=5)
            item_name_entry.insert(0, old_item_name_value)
            item_name_entry.config(state="readonly")

            tk.Label(left_frame, text="Old ItemType:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
            old_item_type_entry = tk.Entry(left_frame, width=30)
            old_item_type_entry.grid(row=3, column=1, padx=10, pady=5)
            old_item_type_entry.insert(0, old_item_type_value)
            old_item_type_entry.config(state="readonly")

            tk.Label(left_frame, text="New Value Found:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
            new_value_entry = tk.Entry(left_frame, width=30)
            new_value_entry.grid(row=4, column=1, padx=10, pady=5)
            new_value_entry.insert(0, new_value_found)
            new_value_entry.config(state="readonly")

            tk.Label(right_frame, text="Item Key:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
            item_key_entry = tk.Entry(right_frame, width=30)
            item_key_entry.grid(row=1, column=1, padx=10, pady=5)
            item_key_entry.insert(0, item_key_value)
            item_key_entry.config(state="readonly")

            tk.Label(right_frame, text="Item description:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
            item_description_entry = tk.Entry(right_frame, width=30)
            item_description_entry.grid(row=0, column=1, padx=10, pady=5)
            item_description_entry.insert(0, item_description)

            tk.Label(right_frame, text="Item Type:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
            item_type_entry = tk.Entry(right_frame, width=30)
            item_type_entry.grid(row=2, column=1, padx=10, pady=5)
            item_type_entry.insert(0, item_type_value)

            tk.Label(right_frame, text="Item Sub Type:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
            item_sub_type_entry = tk.Entry(right_frame, width=30)
            item_sub_type_entry.grid(row=3, column=1, padx=10, pady=5)
            item_sub_type_entry.insert(0, item_sub_type_value)

            tk.Label(right_frame, text="Item Purpose:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
            item_purpose_entry = tk.Entry(right_frame, width=30)
            item_purpose_entry.grid(row=4, column=1, padx=10, pady=5)
            item_purpose_entry.insert(0, item_purpose_value)

            tk.Label(right_frame, text="Item Specifications:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
            item_specifications_entry = tk.Entry(right_frame, width=30)
            item_specifications_entry.grid(row=5, column=1, padx=10, pady=5)
            item_specifications_entry.insert(0, item_specifications_value)

            button_frame = tk.Frame(root)
            button_frame.pack(pady=10)

            search_button = tk.Button(button_frame, text="Search", command=lambda: update_info(*search_action(root, df1, df2, current_row_index, s_no_entry)))
            search_button.grid(row=0, column=0, padx=5)

            prev_button = tk.Button(button_frame, text="Previous", command=lambda: update_info(*prev_action(root, df1, df2, current_row_index)))
            prev_button.grid(row=0, column=1, padx=5)

            next_button = tk.Button(button_frame, text="Next", command=lambda: update_info(*next_action(root, df1, df2, current_row_index)))
            next_button.grid(row=0, column=2, padx=5)

            save_button = tk.Button(button_frame, text="Save", command=lambda: save_action(
                s_no_value,
                old_item_type_value,
                old_item_name_value,
                new_value_found,
                item_sub_type_value,
                item_description,
                item_id_value,
                item_key_value,
                item_specifications_value
            ))
            save_button.grid(row=0, column=3, padx=5)

def update_info(root, df1, df2, new_row_index):
    show_item_info(root, df1, df2, new_row_index)
