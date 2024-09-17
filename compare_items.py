import pandas as pd
import re

# Function to preprocess the string by removing special characters and splitting into words
def preprocess(text):
    # Remove special characters and extra spaces, and convert to lowercase
    clean_text = re.sub(r'[^a-zA9 ]+', '', text).lower().strip()
    # Split the cleaned text into a lis-Z0-t of words
    words = clean_text.split()
    return words

# Function to progressively reduce the number of words and check for match
def find_best_match(old_item, new_data_list):
    old_words = preprocess(old_item)
    
    # First, look for exact match by processing the entire old_item
    for new_item in new_data_list:
        new_words = preprocess(new_item)
        if old_words == new_words:
            return f"Exact match: '{new_item}'"
    
    # If no exact match, progressively reduce the number of words in old_item
    for i in range(len(old_words), 0, -1):
        subset_old_words = old_words[:i]
        for new_item in new_data_list:
            new_words = preprocess(new_item)
            if all(word in new_words for word in subset_old_words):
                return f"Partial match: '{new_item}' with {i} words match"
    
    return "No match"

# Load the old and new Excel files into pandas DataFrames
old_data_df = pd.read_excel('D:\IGS\Constrogen_data_mIgration_gui\input_files\matched_items_result.xlsx')  # The file with 'ItemName' column
new_data_df = pd.read_excel('D:\IGS\Constrogen_data_mIgration_gui\input_files\item_data.xlsx')  # The file with 'Item' column

# Loop through each value in the old data and find matches in the new data
matches = []
for old_item in old_data_df['ItemName']:
    new_items = new_data_df['Item'].tolist()
    match = find_best_match(old_item, new_items)
    matches.append(match)

# Add the matches as a new column in the old data DataFrame
old_data_df['Match'] = matches

# Save the results to a new Excel file
old_data_df.to_excel('matched_data.xlsx', index=False)

print("Matching process completed. Results saved to 'matched_data.xlsx'.")
