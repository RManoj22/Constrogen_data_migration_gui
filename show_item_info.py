import tkinter as tk
from tkinter import ttk
from button_actions import save_action, search_action, prev_action, next_action
from filter_dropdowns import handle_item_type_selection, handle_item_purpose_selection, handle_item_sub_type_selection, handle_item_description_selection


class AutocompleteCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        """Use this method to set the values for the combobox and make it searchable."""
        # Convert all items to strings, and handle NaN values (floats)
        self._completion_list = sorted(
            [str(item) if item is not None else "N/A" for item in completion_list])
        self['values'] = self._completion_list  # Set combobox values
        # Bind key release event
        self.bind('<KeyRelease>', self._handle_keyrelease)

    def _handle_keyrelease(self, event):
        """Filter the combobox values based on the current text input."""
        if event.keysym in ("BackSpace", "Left", "Right", "Up", "Down", "Shift_L", "Shift_R"):
            return  # Ignore certain keypresses
        value = self.get().lower()  # Get current input text
        if value == "":
            # Reset to full list if empty
            self['values'] = self._completion_list
        else:
            filtered_values = [
                item for item in self._completion_list if value in item.lower()]
            # Update dropdown with filtered list
            self['values'] = filtered_values
        self.event_generate('<Down>')  # Open the dropdown list

    def set_selected_value(self, value):
        """Set the selected value in the combobox."""
        self.set(value)


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
        left_frame.grid(row=0, column=0, padx=10, pady=20)

        # Create a frame for right side fields
        right_frame = tk.Frame(info_frame)
        right_frame.grid(row=0, column=1, padx=150, pady=20, sticky="n")

        # Grid layout for right_frame
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)

        if 0 <= current_row_index < len(df1):
            # Fetch the relevant fields from df1
            s_no_value = df1['SNo'].iloc[current_row_index]
            item_id_value = df1['ItemID'].iloc[current_row_index]
            old_item_name_value = df1['ItemName'].iloc[current_row_index]
            old_item_type_value = df1['ItemTypeName'].iloc[current_row_index]

            item_type_options = ["N/A"] + df2['Item type'].unique().tolist()
            item_sub_type_options = ["N/A"] + \
                df2['Item sub type'].unique().tolist()
            item_purpose_options = ["N/A"] + df2['Purpose'].unique().tolist()
            item_specifications_options = [
                "N/A"] + df2['Item specifications'].unique().tolist()
            item_desc_options = ["N/A"] + df2['Item'].unique().tolist()
            default_item_type = "N/A"
            default_item_sub_type = "N/A"
            default_item_purpose = "N/A"
            default_item_specifications = "N/A"
            default_item_desc = "N/A"

            # Check for matching items in df2
            if 'Item' in df2.columns:
                item_matches = df2[df2['Item'] == old_item_name_value]
                match_count = len(item_matches)  # Count number of matches

                # Display the number of matches
                match_count_label = tk.Label(
                    left_frame, text=f"Matches found in df2: {match_count}", font=("Arial", 12))
                match_count_label.grid(
                    row=5, column=0, columnspan=2, padx=10, pady=20)

                if not item_matches.empty:
                    new_value_found = "Yes"

                    # Handle item description
                    # if len(item_matches) > 1:
                    #     # Multiple matches found, create a dropdown
                    #     item_descriptions = item_matches['Item'].values.tolist(
                    #     )
                    #     selected_item_description = tk.StringVar(root)
                    #     selected_item_description.set(
                    #         item_descriptions[0])  # Set the default value

                    #     tk.Label(right_frame, text="Matches found:").grid(
                    #         row=7, column=0, padx=10, pady=20, sticky="w")
                    #     item_description_dropdown = ttk.Combobox(
                    #         right_frame, textvariable=selected_item_description, values=item_descriptions, width=30)
                    #     item_description_dropdown.grid(
                    #         row=7, column=1, padx=10, pady=20)
                    #     item_description = selected_item_description.get()
                    # else:
                    # Single match found, show as a regular Entry field
                    item_description = item_matches['Item'].values[0]

                    item_key_value = item_matches['Item key'].values[0] if 'Item key' in df2.columns else "N/A"
                    item_type_value = item_matches['Item type'].values[0] if 'Item type' in df2.columns else "N/A"
                    item_sub_type_value = item_matches['Item sub type'].values[
                        0] if 'Item sub type' in df2.columns else "N/A"
                    item_purpose_value = item_matches['Purpose'].values[0] if 'Purpose' in df2.columns else "N/A"
                    item_specifications_value = item_matches['Item specifications'].values[
                        0] if 'Item specifications' in df2.columns else "N/A"

                    # Add the matched item type to options
                    item_type_options.append(item_type_value)
                    item_sub_type_options.append(item_sub_type_value)
                    item_purpose_options.append(item_purpose_value)
                    item_specifications_options.append(
                        item_specifications_value)
                    item_desc_options.append(item_description)
                    default_item_type = item_type_value
                    default_item_sub_type = item_sub_type_value
                    default_item_purpose = item_purpose_value
                    default_item_specifications = item_specifications_value
                    default_item_desc = item_description

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
            tk.Label(left_frame, text="S.No:", font=("Arial", 12)).grid(
                row=0, column=0, padx=10, pady=20, sticky="w")
            s_no_entry = tk.Entry(left_frame, width=30, font=("Arial", 12))
            s_no_entry.grid(row=0, column=1, padx=10, pady=20)
            s_no_entry.insert(0, str(s_no_value))

            tk.Label(left_frame, text="Old ItemName:", font=("Arial", 12)).grid(
                row=2, column=0, padx=10, pady=20, sticky="w")
            item_name_entry = tk.Entry(
                left_frame, width=30, font=("Arial", 12))
            item_name_entry.grid(row=2, column=1, padx=10, pady=20)
            item_name_entry.insert(0, old_item_name_value)
            item_name_entry.config(state="readonly")

            tk.Label(left_frame, text="Old ItemType:", font=("Arial", 12)).grid(
                row=3, column=0, padx=10, pady=20, sticky="w")
            old_item_type_entry = tk.Entry(
                left_frame, width=30, font=("Arial", 12))
            old_item_type_entry.grid(row=3, column=1, padx=10, pady=20)
            old_item_type_entry.insert(0, old_item_type_value)
            old_item_type_entry.config(state="readonly")

            tk.Label(left_frame, text="New Value Found:", font=("Arial", 12)).grid(
                row=4, column=0, padx=10, pady=20, sticky="w")
            new_value_entry = tk.Entry(
                left_frame, width=30, font=("Arial", 12))
            new_value_entry.grid(row=4, column=1, padx=10, pady=20)
            new_value_entry.insert(0, new_value_found)
            new_value_entry.config(state="readonly")

            tk.Label(right_frame, text="Item Type:", font=("Arial", 12)).grid(
                row=0, column=0, padx=10, pady=20, sticky="w")
            item_type_combobox = AutocompleteCombobox(
                right_frame, values=item_type_options, width=30, font=("Arial", 12))
            item_type_combobox.grid(row=0, column=1, padx=10, pady=20)
            item_type_combobox.set_completion_list(
                item_type_options)  # Set autocomplete list
            item_type_combobox.set_selected_value(default_item_type)

            item_type_combobox.bind('<<ComboboxSelected>>', lambda event: handle_item_type_selection(
                event, item_type_combobox, item_sub_type_combobox, item_key_entry,
                item_description_combobox, item_purpose_combobox, item_specifications_combobox, df2))

            tk.Label(right_frame, text="Item Purpose:", font=("Arial", 12)).grid(
                row=1, column=0, padx=10, pady=20, sticky="w")
            item_purpose_combobox = AutocompleteCombobox(
                right_frame, values=item_purpose_options, width=30, font=("Arial", 12))
            item_purpose_combobox.grid(row=1, column=1, padx=10, pady=20)
            item_purpose_combobox.set_completion_list(
                item_purpose_options)  # Set autocomplete list
            item_purpose_combobox.set_selected_value(default_item_purpose)

            item_purpose_combobox.bind('<<ComboboxSelected>>', lambda event: handle_item_purpose_selection(
                event, item_type_combobox, item_purpose_combobox, item_sub_type_combobox, df2))

            tk.Label(right_frame, text="Item Sub Type:", font=("Arial", 12)).grid(
                row=2, column=0, padx=10, pady=20, sticky="w")
            item_sub_type_combobox = AutocompleteCombobox(
                right_frame, values=item_sub_type_options, width=30, font=("Arial", 12))
            item_sub_type_combobox.grid(row=2, column=1, padx=10, pady=20)
            item_sub_type_combobox.set_completion_list(
                item_sub_type_options)  # Set autocomplete list
            item_sub_type_combobox.set_selected_value(default_item_sub_type)

            # In show_item_info.py, inside show_item_info function
            item_sub_type_combobox.bind('<<ComboboxSelected>>', lambda event: handle_item_sub_type_selection(
                event, item_type_combobox, item_purpose_combobox, item_sub_type_combobox, item_description_combobox, item_specifications_combobox, item_key_entry, df2))

            tk.Label(right_frame, text="Item description:", font=("Arial", 12)).grid(
                row=3, column=0, padx=10, pady=20, sticky="w")
            item_description_combobox = AutocompleteCombobox(
                right_frame, width=30, font=("Arial", 12))
            item_description_combobox.grid(row=3, column=1, padx=10, pady=20)
            item_description_combobox.set_completion_list(
                item_desc_options)  # Set autocomplete list
            item_description_combobox.set_selected_value(default_item_desc)

            # In show_item_info.py, inside show_item_info function
            item_description_combobox.bind('<<ComboboxSelected>>', lambda event: handle_item_description_selection(
                event, item_type_combobox, item_purpose_combobox, item_sub_type_combobox, item_description_combobox, item_specifications_combobox, item_key_entry, df2))

            tk.Label(right_frame, text="Item Specifications:", font=("Arial", 12)).grid(
                row=4, column=0, padx=10, pady=20, sticky="w")
            item_specifications_combobox = AutocompleteCombobox(
                right_frame, values=item_specifications_options, width=30, font=("Arial", 12))
            item_specifications_combobox.grid(
                row=4, column=1, padx=10, pady=20)
            item_specifications_combobox.set_completion_list(
                item_specifications_options)  # Set autocomplete list
            item_specifications_combobox.set_selected_value(
                default_item_specifications)

            tk.Label(right_frame, text="Item Key:", font=("Arial", 12)).grid(
                row=5, column=0, padx=10, pady=20, sticky="w")
            item_key_entry = tk.Entry(
                right_frame, width=30, font=("Arial", 12))
            item_key_entry.grid(row=5, column=1, padx=10, pady=20)
            item_key_entry.insert(0, item_key_value)
            item_key_entry.config(state="readonly")

            match_found_var = tk.BooleanVar()
            match_found_checkbox = tk.Checkbutton(
                right_frame, text="Match Not Found", variable=match_found_var, font=("Arial", 12))
            match_found_checkbox.grid(
                row=6, column=0, columnspan=2, padx=10, pady=15, sticky="w")

            button_frame = tk.Frame(root)
            button_frame.pack(pady=10)

            search_button = tk.Button(button_frame, text="Search", font=("Arial", 12), width=12, height=2, command=lambda: update_info(
                *search_action(root, df1, df2, current_row_index, s_no_entry)))
            search_button.grid(row=0, column=0, padx=30)

            prev_button = tk.Button(button_frame, text="Previous",  font=("Arial", 12), width=12, height=2, command=lambda: update_info(
                *prev_action(root, df1, df2, current_row_index)))
            prev_button.grid(row=0, column=1, padx=30)

            next_button = tk.Button(button_frame, text="Next",  font=("Arial", 12), width=12, height=2, command=lambda: update_info(
                *next_action(root, df1, df2, current_row_index)))
            next_button.grid(row=0, column=2, padx=30)

            save_button = tk.Button(root, text="Save",  font=("Arial", 12), width=12, height=2, command=lambda: save_action(
                s_no_value=s_no_entry.get(),
                item_type_combobox=item_type_combobox,
                item_name_entry=item_name_entry,
                new_value_found=new_value_found,  # If applicable
                sub_type_combobox=item_sub_type_combobox,
                item_description_combobox=item_description_combobox,
                old_item_id_value=item_id_value,
                new_item_key=item_key_entry,
                new_item_specifications=item_specifications_combobox,
                match_found=match_found_var.get()  # Get the boolean value
            ))
            save_button.pack(pady=(10, 0))


def update_info(root, df1, df2, new_row_index):
    show_item_info(root, df1, df2, new_row_index)
