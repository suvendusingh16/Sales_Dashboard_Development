import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine



# PostgreSQL Connection Config
DB_NAME = "db_sales"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to PostgreSQL using SQLAlchemy
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def fetch_data():
    query = "SELECT * FROM sales;"
    df = pd.read_sql(query, engine)
    return df

# Build Data Analysis and Visualization
def build_dashboard():
    print("Sales Insights Dashboard")
    df = fetch_data()

    print("\nRaw Sales Data:")
    print(df)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Sales Trend Visualization
    print("\nSales Trend Over Time:")
    sales_trend = df.groupby("date")["revenue"].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="date", y="revenue", data=sales_trend)
    plt.xticks(rotation=45)
    plt.title("Sales Trend Over Time")
    plt.show(block=True)

    # Category-wise Sales Breakdown
    print("\nCategory-wise Revenue:")
    category_sales = df.groupby("category")["revenue"].sum().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(x="category", y="revenue", data=category_sales)
    plt.title("Category-wise Revenue")
    plt.show(block=True)

    # Top 5 Best-Selling Products
    print("\nTop 5 Best-Selling Products:")
    top_products = df.groupby("product")["revenue"].sum().reset_index().sort_values(by="revenue", ascending=False).head(5)
    print(top_products)

if __name__ == "__main__":
    build_dashboard()
