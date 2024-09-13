import psycopg2
import pandas as pd
import os

# Establish database connection
connection = psycopg2.connect(
    host="localhost",
    database="bis-erp-migration",
    user="postgres",
    password="postgres",
    port="5433"
)

# Define the SQL query
query = """
SELECT 
    i."Item_Key",
    i."Item_Descr",
    it."ItemTyp_Descr",
    ist."ItemSubTyp_Descr",
    p."Purpose_Name",
    i."Item_Gst",
    STRING_AGG(ispec."ItemSpec_Value", ', ') AS "ItemSpecifications"
FROM 
    public."Item" i
JOIN 
    public."ItemType" it ON i."Item_ItemTyp_Key" = it."ItemTyp_Key"
LEFT JOIN 
    public."ItemSubType" ist ON i."Item_SubType_Key" = ist."ItemSubTyp_Key"
LEFT JOIN 
    public."Purpose" p ON i."Item_Purpose_Key" = p."Purpose_Key"
LEFT JOIN 
    public."ItemSpecification" ispec ON i."Item_Key" = ispec."ItemSpec_Item_key"
GROUP BY 
    i."Item_Key", 
    i."Item_Descr", 
    i."Item_Model_Number", 
    it."ItemTyp_Descr", 
    ist."ItemSubTyp_Descr", 
    p."Purpose_Name",
    i."Item_Gst"
"""

# Execute the query and read data into a DataFrame
df = pd.read_sql_query(query, connection)

# Close the database connection
connection.close()

# Determine the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the output directory, which is one level up from the current directory
output_directory = os.path.join(current_directory, '..', 'output_files', 'new_db_items')
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it does not exist

# Define the output file path
output_file = os.path.join(output_directory, 'item_data.xlsx')

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Data written to {output_file}")
