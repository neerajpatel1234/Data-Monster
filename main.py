import pandas as pd 

# ----------- Test Pandas -----------
testData = pd.Series([1,2,3])
print (testData)

# ----------- Function Defs -----------
def excel_to_tables(file_path):
    xls = pd.ExcelFile(file_path)
    tables = {}
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        tables[sheet_name] = df
    
    return tables



# ----------- Ask for file name -----------
file_path = input('Enter file path: ')  
if file_path == '':
    print('ERROR: No file path entered.')
    exit()

tables = excel_to_tables(file_path)

# ----------- Print all sheet names -----------
for sheet_name in tables.keys():
    print(sheet_name)

tables['Sheet_Title']
