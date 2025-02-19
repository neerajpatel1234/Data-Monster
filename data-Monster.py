import matplotlib.pyplot as plt
import pandas as pd
import pdfplumber
import tkinter as tk
from tkinter import filedialog
import re

def extract_transactions_from_pdf(pdf_path):
    transactions = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    match = re.search(r'(?P<date>\d{2} \w{3})\s+(?P<type>\w+)\s+(?P<description>[\w\s]+)\s+(?P<money_out>\d+\.\d{2})?\s+(?P<money_in>\d+\.\d{2})?', line)
                    if match:
                        category = match.group("description").strip()
                        money_out = float(match.group("money_out")) if match.group("money_out") else 0
                        money_in = float(match.group("money_in")) if match.group("money_in") else 0
                        amount = money_out if money_out > 0 else money_in
                        transactions.append((category, amount))
    
    return pd.DataFrame(transactions, columns=['Category', 'Amount'])

def plot_budget(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['Category'], df['Amount'], color='skyblue')
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.title("Spending Allocation")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
    
    if pdf_path:
        budget_df = extract_transactions_from_pdf(pdf_path)
        
        if not budget_df.empty:
            print("\nBudget Overview:")
            print(budget_df)
            plot_budget(budget_df)
        else:
            print("No budget data found.")
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()