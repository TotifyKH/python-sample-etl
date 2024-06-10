import pandas as pd

def generate_total_renevue_by_location(df):
    # Clean the column names to remove hidden characters or whitespace
    df.columns = df.columns.str.strip().str.replace("\u200b", "")

    # List of tax columns
    tax_columns = [
        "ពន្ធនាំចូល",
        "អាករពិសេស",
        "អាករលើតម្លៃបន្ថែម",
        "អាករបន្ថែមលើផលិតផលប្រេង",
        "អាករនាំចេញ",
        "ចំណូលផ្សេងៗ",
    ]

    # Clean each column name in tax_columns
    clean_tax_columns = [tax.strip().replace("\u200b", "") for tax in tax_columns]

    # Create a new DataFrame for the required structure
    rows = []
    row_number = 1

    # Aggregate by ministry
    for ministry, ministry_df in df.groupby("នាយកដ្ឋាន"):
        total_revenue = ministry_df[clean_tax_columns].sum().sum()
        rows.append([row_number, ministry, round(total_revenue, 2)])
        row_number += 1

        # Aggregate by branch within each ministry
        for branch, branch_df in ministry_df.groupby("សាខា"):
            total_revenue = branch_df[clean_tax_columns].sum().sum()
            rows.append([row_number, branch, round(total_revenue, 2)])
            row_number += 1

            # Aggregate by department within each branch
            for department, department_df in branch_df.groupby("ការិយាល័យ"):
                total_revenue = department_df[clean_tax_columns].sum().sum()
                rows.append([row_number, department, round(total_revenue, 2)])
                row_number += 1

    # Convert the list of rows to a DataFrame
    result_df = pd.DataFrame(rows, columns=["លេខរៀង", "សូចនាករ", "ចំណូលសរុប"])

    # Save the result to a new CSV file
    result_df.to_csv("./output/renevue_by_location.csv", index=False)
    print("ETL process 2 is completed, generated revenue_by_location.csv")
