import matplotlib.pyplot as plt
import pandas as pd
import pdfplumber

def extract_transactions_from_pdf(pdf_path):
    transactions = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    parts = line.split()
                    if len(parts) > 4 and parts[1] in ["BP", "DC"]:  # Filter transactions
                        try:
                            money_out = float(parts[-2]) if parts[-2].replace('.', '', 1).isdigit() else 0
                            money_in = float(parts[-3]) if parts[-3].replace('.', '', 1).isdigit() else 0
                            category = parts[2] if len(parts) > 2 else "Unknown"
                            transactions.append((category, money_out if money_out > 0 else money_in))
                        except ValueError:
                            continue
    
    return pd.DataFrame(transactions, columns=['Category', 'Amount'])

def plot_budget(df):
    plt.figure(figsize=(8, 6))
    plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title("Spending Allocation")
    plt.axis('equal')  # Ensures pie chart is a circle
    plt.show()

def main():
    pdf_path = "1_WP03-0774-0077757-000_20241124_058.pdf"  # Update with actual file path
    budget_df = extract_transactions_from_pdf(pdf_path)
    
    if not budget_df.empty:
        print("\nBudget Overview:")
        print(budget_df)
        plot_budget(budget_df)
    else:
        print("No budget data found.")

if __name__ == "__main__":
    main()
