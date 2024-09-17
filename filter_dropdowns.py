import tkinter as tk


def handle_item_type_selection(event, combobox, sub_type_combobox, key_entry, description_combobox, purpose_combobox, specifications_combobox, df2):
    selected_value = combobox.get()  # Get the selected value from combobox
    print(f"Selected Item Type: {selected_value}")  # Print the selected value

    # Clear the values of the other comboboxes and fields
    sub_type_combobox.set('')  # Clear the selected value in Item Sub Type
    # Clear the selected value in Item Description
    description_combobox.set('')
    purpose_combobox.set('')  # Clear the selected value in Item Purpose
    # Clear the selected value in Item Specifications
    specifications_combobox.set('')

    # Temporarily remove the read-only state of item_key_entry, clear its value, and set it back to read-only
    key_entry.config(state='normal')
    key_entry.delete(0, tk.END)  # Clear the content in the entry widget
    key_entry.config(state='readonly')  # Set it back to read-only

    # Filter the options for Item Sub Type and Item Purpose based on the selected Item Type from df2
    if selected_value != "N/A":  # Check if an actual item type is selected
        filtered_sub_types = df2[df2['Item type'] ==
                                 selected_value]['Item sub type'].unique().tolist()
        filtered_purposes = df2[df2['Item type'] ==
                                selected_value]['Purpose'].unique().tolist()
    else:
        filtered_sub_types = []  # If no valid selection, leave it empty
        filtered_purposes = []  # If no valid selection, leave it empty

    # Set the filtered options in the Item Sub Type combobox
    sub_type_combobox.set_completion_list(filtered_sub_types)
    sub_type_combobox.set('')

    # Set the filtered options in the Item Purpose combobox
    purpose_combobox.set_completion_list(filtered_purposes)
    purpose_combobox.set('')

    # Auto-select Item Purpose if only one option is available
    if len(filtered_purposes) == 1:
        purpose_combobox.set(filtered_purposes[0])
        print(f"Automatically selected Item Purpose: {filtered_purposes[0]}")


def handle_item_purpose_selection(event, item_type_combobox, purpose_combobox, sub_type_combobox, df2):
    selected_item_type = item_type_combobox.get()  # Get selected item type
    selected_purpose = purpose_combobox.get()  # Get selected purpose

    # Print selected values for debugging
    print(
        f"Selected Item Type: {selected_item_type}, Selected Purpose: {selected_purpose}")

    # Filter the Item Sub Type options based on both Item Type and Purpose
    if selected_item_type != "N/A" and selected_purpose != "N/A":
        filtered_sub_types = df2[
            (df2['Item type'] == selected_item_type) &
            (df2['Purpose'] == selected_purpose)
        ]['Item sub type'].unique().tolist()
    else:
        filtered_sub_types = []  # If no valid selection, leave empty

    # Update the Item Sub Type combobox with filtered options
    sub_type_combobox.set_completion_list(filtered_sub_types)
    sub_type_combobox.set('')  # Reset the selection

    # Auto-select Item Sub Type if only one option is available
    if len(filtered_sub_types) == 1:
        sub_type_combobox.set(filtered_sub_types[0])
        print(f"Automatically selected Item Sub Type: {filtered_sub_types[0]}")


def handle_item_sub_type_selection(event, item_type_combobox, purpose_combobox, sub_type_combobox, description_combobox, specifications_combobox, key_entry, df2):
    selected_item_type = item_type_combobox.get()  # Get selected Item Type
    selected_purpose = purpose_combobox.get()  # Get selected Purpose
    selected_sub_type = sub_type_combobox.get()  # Get selected Sub Type

    # Print selected values for debugging
    print(
        f"Selected Item Type: {selected_item_type}, Selected Purpose: {selected_purpose}, Selected Sub Type: {selected_sub_type}")

    # Clear the values of the other comboboxes and fields
    # Clear the selected value in Item Description
    description_combobox.set('')
    # Clear the selected value in Item Specifications
    specifications_combobox.set('')

    # Temporarily remove the read-only state of item_key_entry, clear its value, and set it back to read-only
    key_entry.config(state='normal')
    key_entry.delete(0, tk.END)  # Clear the content in the entry widget
    key_entry.config(state='readonly')  # Set it back to read-only

    # Filter the Item Description options based on selected Item Type, Purpose, and Sub Type
    if selected_item_type != "N/A" and selected_purpose != "N/A" and selected_sub_type != "N/A":
        filtered_descriptions = df2[
            (df2['Item type'] == selected_item_type) &
            (df2['Purpose'] == selected_purpose) &
            (df2['Item sub type'] == selected_sub_type)
        ]['Item'].unique().tolist()
    else:
        filtered_descriptions = []  # If no valid selection, leave empty

    # Update the Item Description combobox with filtered options
    description_combobox.set_completion_list(filtered_descriptions)

    if len(filtered_descriptions) == 1:
        # Automatically select the single value
        description_combobox.set(filtered_descriptions[0])
        print(
            f"Automatically selected Item Description: {filtered_descriptions[0]}")
    elif len(filtered_descriptions) > 1:
        # Multiple options available, allow user to select
        description_combobox.set('')  # Clear the selection to allow user input
        print(f"Multiple Item Descriptions available: {filtered_descriptions}")
    else:
        # No descriptions found, reset the combobox
        description_combobox.set('')  # Clear the selection
        print("No matching Item Descriptions found.")


def handle_item_description_selection(event, item_type_combobox, purpose_combobox, sub_type_combobox, description_combobox, specifications_combobox, key_entry, df2):
    # Get the selected values from the comboboxes
    selected_item_type = item_type_combobox.get()  # Get selected Item Type
    selected_purpose = purpose_combobox.get()  # Get selected Purpose
    selected_sub_type = sub_type_combobox.get()  # Get selected Sub Type
    selected_description = description_combobox.get()  # Get selected Item Description

    # Print selected values for debugging
    print(f"Selected Item Type: {selected_item_type}, Selected Purpose: {selected_purpose}, Selected Sub Type: {selected_sub_type}, Selected Description: {selected_description}")

    # Filter the Item Specifications options based on selected values
    if selected_item_type != "N/A" and selected_purpose != "N/A" and selected_sub_type != "N/A" and selected_description != "N/A":
        filtered_specifications = df2[
            (df2['Item type'] == selected_item_type) &
            (df2['Purpose'] == selected_purpose) &
            (df2['Item sub type'] == selected_sub_type) &
            (df2['Item'] == selected_description)
        ]['Item specifications'].unique().tolist()
    else:
        filtered_specifications = []  # If no valid selection, leave it empty

    # Update the Item Specifications combobox with filtered options
    specifications_combobox.set_completion_list(filtered_specifications)

    if len(filtered_specifications) == 1:
        # Automatically select the single value
        specifications_combobox.set(filtered_specifications[0])
        print(
            f"Automatically selected Item Specification: {filtered_specifications[0]}")
    elif len(filtered_specifications) > 1:
        # Multiple options available, allow user to select
        # Clear the selection to allow user input
        specifications_combobox.set('')
        print(
            f"Multiple Item Specifications available: {filtered_specifications}")
    else:
        specifications_combobox.set('')  # Clear the selection
        print("No matching Item Specifications found.")

    # Now handle setting the 'Item key' based on the selected values
    if selected_item_type != "N/A" and selected_purpose != "N/A" and selected_sub_type != "N/A" and selected_description != "N/A":
        # Filter the DataFrame to get the matching Item key
        matching_key = df2[
            (df2['Item type'] == selected_item_type) &
            (df2['Purpose'] == selected_purpose) &
            (df2['Item sub type'] == selected_sub_type) &
            (df2['Item'] == selected_description)
        ]['Item key'].unique().tolist()

        # If we find exactly one matching key, set it as the value of the Item key field
        if len(matching_key) == 1:
            # Temporarily enable the entry field
            key_entry.config(state='normal')
            key_entry.delete(0, tk.END)  # Clear the current value
            key_entry.insert(0, matching_key[0])  # Set the matched key
            # Set the entry back to read-only
            key_entry.config(state='readonly')
            print(f"Automatically set Item Key: {matching_key[0]}")
        elif len(matching_key) > 1:
            print(f"Multiple matching keys found: {matching_key}")
        else:
            print("No matching Item Key found.")
    else:
        print("Incomplete selection for Item Key filtering.")
