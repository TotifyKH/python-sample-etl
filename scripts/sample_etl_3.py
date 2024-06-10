import pandas as pd

def generate_total_revenue(df, previous_cumulative: int):
    df.columns = df.columns.str.strip().str.replace("\u200b", "")

    # list of tax columns
    tax_columns = [
        "ពន្ធនាំចូល",
        "អាករពិសេស",
        "អាករលើតម្លៃបន្ថែម",
        "អាករបន្ថែមលើផលិតផលប្រេង",
        "អាករនាំចេញ",
        "ចំណូលផ្សេងៗ",
    ]

    clean_tax_columns = [tax.strip().replace("\u200b", "") for tax in tax_columns]
    rows = []

    total_revenue_this_month = round(df[clean_tax_columns].sum().sum(), 2)
    rows.append([1, "ចំណូលសរុបនៃអគ្គនាយកដ្ឋានគយ និងរដ្ឋាករកម្ពុជា", "ប៊ីលានរៀល (ជាទិន្នន័យលំហូ)", total_revenue_this_month])
    rows.append([2, "ចំណូលសរុបនៃអគ្គនាយកដ្ឋានគយ និងរដ្ឋាករកម្ពុជា", "ប៊ីលានរៀល (ជាទិន្នន័យសន្ទិ)", previous_cumulative + total_revenue_this_month])

    result_df = pd.DataFrame(rows, columns=["លេខរៀង", "បរិយាយ", "ឯកតារង្វាស់", "ចំណូលសរុប"])
    result_df.to_csv("./output/total_revenue.csv", index=False)
    print("ETL process 3 is completed, generated total_revenue.csv")