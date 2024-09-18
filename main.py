import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from show_item_info import show_item_info

# Define font and button sizes
FONT_SIZE = 12
BUTTON_WIDTH = 20
BUTTON_HEIGHT = 2

current_path = os.getcwd()
# Initialize file paths and current row index
# Default path for old data
file_path_1 = f"{current_path}/input_files/matched_items_result.xlsx"
# Default path for new data
file_path_2 = f"{current_path}/input_files/item_data.xlsx"
current_row_index = 0
df1 = None
df2 = None

def select_file_1():
    global file_path_1, df1
    file_path_1 = filedialog.askopenfilename(
        title="Select Old Data Excel File",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if file_path_1:
        file_label_1.config(text=f"Selected: {file_path_1.split('/')[-1]}")
    check_files_selected()

def select_file_2():
    global file_path_2, df2
    file_path_2 = filedialog.askopenfilename(
        title="Select New Data Excel File",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if file_path_2:
        file_label_2.config(text=f"Selected: {file_path_2.split('/')[-1]}")
    check_files_selected()

def check_files_selected():
    if file_path_1 and file_path_2:
        load_button.grid(row=3, column=0, columnspan=2, pady=20)

def load_files():
    global df1, df2, current_row_index
    df1 = pd.read_excel(file_path_1)
    df2 = pd.read_excel(file_path_2)
    current_row_index = 0  # Reset row index to 0
    show_item_info(root, df1, df2, current_row_index)

root = tk.Tk()
root.title("Excel File Loader")
root.geometry("750x300")
root.option_add('*TCombobox*Listbox.font', ('Arial', 12))

# Set the window to maximize by default
root.state('zoomed')

# Define styles with the font and button sizes
label_style = {"font": ("Arial", FONT_SIZE)}
button_style = {"font": ("Arial", FONT_SIZE), "width": BUTTON_WIDTH, "height": BUTTON_HEIGHT}

file_label_1 = tk.Label(root, text=f"Selected: {file_path_1.split('/')[-1]}", **label_style)
file_label_1.grid(row=0, column=0, padx=300, pady=(250, 10), sticky="w")

select_button_1 = tk.Button(root, text="Browse File", command=select_file_1, **button_style)
select_button_1.grid(row=0, column=1, padx=50, pady=(250, 10))

file_label_2 = tk.Label(root, text=f"Selected: {file_path_2.split('/')[-1]}", **label_style)
file_label_2.grid(row=1, column=0, padx=300, pady=(50, 30), sticky="w")

select_button_2 = tk.Button(root, text="Browse File", command=select_file_2, **button_style)
select_button_2.grid(row=1, column=1, padx=50, pady=(50, 30))

load_button = tk.Button(root, text="Load Files", command=load_files, **button_style)
load_button.grid(row=3, column=0, columnspan=2, padx=700, pady=20)

root.mainloop()
