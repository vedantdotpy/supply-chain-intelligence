import os
import logging
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Configure logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


# Database configuration
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# Create database connection
connection_string = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(connection_string)


logger.info("Database engine created successfully")

# EXTRACT

DATA_PATH = "data/processed/supply_chain_cleaned.csv"

df = pd.read_csv(DATA_PATH)

logger.info("Dataset loaded successfully")
logger.info(f"Rows: {df.shape[0]}")
logger.info(f"Columns: {df.shape[1]}")

# DATA INSPECTION

print(df.head())
print(df.info())
print("Dataset validation completed")

# TRANSFORM CUSTOMER DIMENSION

customer_df = df[
    [
        "Customer Id",
        "Customer City",
        "Customer State",
        "Customer Country",
        "Customer Segment",
        "Customer Zipcode",
        "Latitude",
        "Longitude"
    ]
].copy()


customer_df = customer_df.drop_duplicates()


customer_df.rename(
    columns={
        "Customer Id": "customer_id",
        "Customer City": "city",
        "Customer State": "state",
        "Customer Country": "country",
        "Customer Segment": "segment",
        "Customer Zipcode": "zipcode",
        "Latitude": "latitude",
        "Longitude": "longitude"
    },
    inplace=True
)


logger.info("Customer dimension created")
logger.info(f"Customer rows: {len(customer_df)}")

logger.info(
    f"Customer IDs unique: {customer_df['customer_id'].is_unique}"
)

# TRANSFORM PRODUCT DIMENSION

product_df = df[
    [
        "Product Card Id",
        "Product Name",
        "Category Id",
        "Category Name",
        "Department Name",
        "Product Price"
    ]
].copy()


product_df = product_df.drop_duplicates()


product_df.rename(
    columns={
        "Product Card Id": "product_id",
        "Product Name": "product_name",
        "Category Id": "category_id",
        "Category Name": "category_name",
        "Department Name": "department_name",
        "Product Price": "product_price"
    },
    inplace=True
)


logger.info("Product dimension created")
logger.info(f"Product rows: {len(product_df)}")

logger.info(
    f"Product IDs unique: {product_df['product_id'].is_unique}"
)

# TRANSFORM DATE DIMENSION


date_df = df[
    [
        "order date (DateOrders)"
    ]
].copy()


date_df["full_date"] = pd.to_datetime(
    date_df["order date (DateOrders)"]
).dt.date


date_df = date_df[["full_date"]].drop_duplicates()


date_df["date_id"] = range(1, len(date_df) + 1)


date_df["day"] = pd.to_datetime(
    date_df["full_date"]
).dt.day


date_df["month"] = pd.to_datetime(
    date_df["full_date"]
).dt.month


date_df["month_name"] = pd.to_datetime(
    date_df["full_date"]
).dt.month_name()


date_df["quarter"] = (
    "Q" +
    pd.to_datetime(date_df["full_date"])
    .dt.quarter
    .astype(str)
)


date_df["year"] = pd.to_datetime(
    date_df["full_date"]
).dt.year


date_df = date_df[
    [
        "date_id",
        "full_date",
        "day",
        "month",
        "month_name",
        "quarter",
        "year"
    ]
]


logger.info("Date dimension created")
logger.info(f"Date rows: {len(date_df)}")

# TRANSFORM SHIPPING DIMENSION

shipping_df = df[
    [
        "Shipping Mode",
        "Delivery Status",
        "Days for shipping (real)",
        "Days for shipment (scheduled)",
        "Late_delivery_risk"
    ]
].copy()


shipping_df = shipping_df.drop_duplicates()


shipping_df["shipping_id"] = range(
    1,
    len(shipping_df) + 1
)


shipping_df.rename(
    columns={
        "Shipping Mode": "shipping_mode",
        "Delivery Status": "delivery_status",
        "Days for shipping (real)": "actual_shipping_days",
        "Days for shipment (scheduled)": "scheduled_shipping_days",
        "Late_delivery_risk": "late_delivery_risk"
    },
    inplace=True
)


shipping_df = shipping_df[
    [
        "shipping_id",
        "shipping_mode",
        "delivery_status",
        "actual_shipping_days",
        "scheduled_shipping_days",
        "late_delivery_risk"
    ]
]


logger.info("Shipping dimension created")
logger.info(f"Shipping rows: {len(shipping_df)}")

# TRANSFORM FACT TABLE

fact_df = df[
    [
        "Order Item Id",
        "Customer Id",
        "Product Card Id",
        "order date (DateOrders)",
        "Shipping Mode",
        "Delivery Status",
        "Days for shipping (real)",
        "Days for shipment (scheduled)",
        "Late_delivery_risk",
        "Sales",
        "Order Profit Per Order",
        "Order Item Quantity",
        "Order Item Discount"
    ]
].copy()


# Rename columns

fact_df.rename(
    columns={
        "Order Item Id": "order_item_id",
        "Customer Id": "customer_id",
        "Product Card Id": "product_id",
        "Sales": "sales",
        "Order Profit Per Order": "profit",
        "Order Item Quantity": "quantity",
        "Order Item Discount": "discount"
    },
    inplace=True
)


logger.info("Fact table base created")
logger.info(f"Fact table rows: {len(fact_df)}")

# ADD DATE KEY

fact_df["order_date"] = pd.to_datetime(
    df["order date (DateOrders)"]
).dt.date


fact_df = fact_df.merge(
    date_df[
        [
            "date_id",
            "full_date"
        ]
    ],
    left_on="order_date",
    right_on="full_date",
    how="left"
)


fact_df.drop(
    columns=[
        "order_date",
        "full_date"
    ],
    inplace=True
)


print("Date key added")
print(fact_df.head())

# ADD SHIPPING KEY

fact_df = fact_df.merge(
    shipping_df,
    left_on=[
        "Shipping Mode",
        "Delivery Status",
        "Days for shipping (real)",
        "Days for shipment (scheduled)",
        "Late_delivery_risk"
    ],
    right_on=[
        "shipping_mode",
        "delivery_status",
        "actual_shipping_days",
        "scheduled_shipping_days",
        "late_delivery_risk"
    ],
    how="left"
)


fact_df.drop(
    columns=[
        "Shipping Mode",
        "Delivery Status",
        "Days for shipping (real)",
        "Days for shipment (scheduled)",
        "Late_delivery_risk",
        "shipping_mode",
        "delivery_status",
        "actual_shipping_days",
        "scheduled_shipping_days",
        "late_delivery_risk"
    ],
    inplace=True
)


print("Shipping key added")
print(fact_df.head())
print(fact_df.columns.tolist())
print("Rows:", len(fact_df))
print(
    "Missing date keys:",
    fact_df["date_id"].isna().sum()
)

print(
    "Missing shipping keys:",
    fact_df["shipping_id"].isna().sum()
)

# CLEAN FINAL FACT TABLE

fact_df.drop(
    columns=[
        "order date (DateOrders)"
    ],
    inplace=True
)


print("Final fact table cleaned")
print(fact_df.columns.tolist())
print(fact_df.isnull().sum())

logger.info("Starting database loading...")

# CLEAR EXISTING DATA

with engine.begin() as connection:

    connection.execute(
        text(
            """
            TRUNCATE TABLE
            fact_orders,
            dim_customer,
            dim_product,
            dim_date,
            dim_shipping
            CASCADE;
            """
        )
    )

logger.info("Existing database tables cleared")

# LOAD DATA INTO POSTGRESQL

customer_df.to_sql(
    "dim_customer",
    engine,
    if_exists="append",
    index=False
)

logger.info("Loaded dim_customer")


product_df.to_sql(
    "dim_product",
    engine,
    if_exists="append",
    index=False
)

logger.info("Loaded dim_product")


date_df.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)

logger.info("Loaded dim_date")


shipping_df.to_sql(
    "dim_shipping",
    engine,
    if_exists="append",
    index=False
)

logger.info("Loaded dim_shipping")


fact_df.to_sql(
    "fact_orders",
    engine,
    if_exists="append",
    index=False
)

logger.info("Loaded fact_orders")


logger.info("Database loading completed successfully")