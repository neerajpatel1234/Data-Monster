import pandas as pd

def excel_to_tables(file_path):
    xls = pd.ExcelFile(file_path)
    tables = {}
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        tables[sheet_name] = df
    
    return tables


# ----------- Variables -----------
file_path = 'example.xlsx'  # Replace with your Excel file path
tables = excel_to_tables(file_path)

tables['Sheet_Title']
