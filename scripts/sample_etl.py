import pandas as pd


def generate_total_revenue_by_tax_type(df):
    # Clean the column names to remove hidden characters or whitespace
    df.columns = df.columns.str.strip().str.replace("\u200b", "")
    # List of tax types and their corresponding cleaned column names in the original CSV
    tax_columns = [
        "ពន្ធនាំចូល",
        "អាករពិសេស",
        "អាករលើ​តម្លៃ​បន្ថែម",
        "អាករបន្ថែម​លើផលិតផលប្រេង",
        "អាករនាំចេញ",
        "ចំណូលផ្សេងៗ",
    ]
    # Clean each column name in tax_columns
    clean_tax_columns = [tax.strip().replace("\u200b", "") for tax in tax_columns]

    # Create a new DataFrame for the required structure
    data = {
        "លេខរៀង": range(1, len(clean_tax_columns) + 1),
        "ប្រភេទពន្ធ": clean_tax_columns,
        "ចំណូលសរុប": [round(df[col].sum(),2) for col in clean_tax_columns],
    }

    result_df = pd.DataFrame(data)
    # Save the result to a new CSV file
    result_df.to_csv("./output/revenue_by_tax_type.csv", index=False)
    print("ETL process 1 is completed, generated revenue_by_tax_type.csv")
