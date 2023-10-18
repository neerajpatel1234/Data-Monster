import pandas as pd

# ----------- Test Pandas -----------
testData = pd.Series([1,2,3])
print(testData)

# ----------- Function Defs -----------
def excel_to_tables(file_path):
    try:
        xls = pd.ExcelFile(file_path)
    except Exception as e:
        print(f'ERROR: {e}')
        return None

    tables = {}
    
    if not xls.sheet_names:
        print('ERROR: No sheets found in file.')
        return None
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        tables[sheet_name] = df
    
    return tables

# ----------- Ask for file name -----------
file_path = input('Enter file path: ')  
if not file_path:
    print('ERROR: No file path entered.')
    exit()
    
# ----------- Read Excel file -----------
tables = excel_to_tables(file_path)

if tables:
    # ----------- Print all sheet names -----------
    for sheet_name in tables.keys():
        print(sheet_name)
        
    # ----------- Access a specific sheet -----------
    sheet_name = input('Enter sheet name: ')
    current_sheet = tables.get(sheet_name)

    if current_sheet is not None:
        print(current_sheet)
    else:
        print(f'ERROR: Sheet "{sheet_name}" not found.')
