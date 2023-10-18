import tkinter as tk
from tkinter import filedialog
import pandas as pd
import openpyxl as xl

# ----------- Function Definitions -----------
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

def save_to_csv(dataframe, file_name):
    try:
        dataframe.to_csv(file_name, index=False)
        print(f'Successfully saved to {file_name}')
    except Exception as e:
        print(f'ERROR: {e}')

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def convert_to_csv():
    file_path = entry_path.get()
    tables = excel_to_tables(file_path)
    if tables:
        for sheet_name in tables.keys():
            listbox_sheets.insert(tk.END, sheet_name)

def save_csv():
    global tables
    selected_sheet = listbox_sheets.get(tk.ACTIVE)
    if selected_sheet:
        current_sheet = tables[selected_sheet]
        csv_file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if csv_file_name:
            save_to_csv(current_sheet, csv_file_name)

# ----------- GUI -----------
window = tk.Tk()
window.title("Data Monster")
window.resizable(False, False)

frame = tk.Frame(window)
frame.pack(pady=10)

menu = tk.Menu(window)
window.config(menu=menu)
menu_file = tk.Menu(menu)

filemenu = tk.Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=window.quit) 
helpmenu = tk.Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 


label_path = tk.Label(frame, text="File Path:")
label_path.grid(row=0, column=0)

entry_path = tk.Entry(frame, width=50)
entry_path.grid(row=0, column=1, padx=10)

button_browse = tk.Button(frame, text="Browse Files", command=browse_file)
button_browse.grid(row=0, column=2)

button_convert_csv = tk.Button(frame, text="Convert to CSV", command=convert_to_csv)
button_convert_csv.grid(row=1, columnspan=3, pady=10)

button_convert_excel = tk.Button(frame, text="Convert to Excel")
button_convert_excel.grid(row=2, columnspan=3, pady=10)

listbox_sheets = tk.Listbox(window, selectmode=tk.SINGLE, width=50)
listbox_sheets.pack(pady=10)

button_save = tk.Button(window, text="Save as CSV", command=save_csv)
button_save.pack()

window.mainloop()

