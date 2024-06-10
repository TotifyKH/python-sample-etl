from scripts.sample_etl import generate_total_revenue_by_tax_type
from scripts.sample_etl_2 import generate_total_renevue_by_location
from scripts.sample_etl_3 import generate_total_revenue
from minio import Minio
from io import BytesIO
import pandas as pd


client = Minio(
    endpoint="localhost:9000",
    access_key="minio",
    secret_key="minio123",
    secure=False
)

def main():
    response = client.get_object('gdce', 'raw-revenue-data/revenue_data_jan_2024.csv')
    df = pd.read_csv(BytesIO(response.data))
    previous_cumulative = 1000000
    generate_total_revenue(df, previous_cumulative)
    generate_total_renevue_by_location(df)
    generate_total_revenue_by_tax_type(df)


if __name__ == "__main__":
    main()
