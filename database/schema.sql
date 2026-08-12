CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    segment VARCHAR(50),
    zipcode VARCHAR(20),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6)
);


CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category_id INT,
    category_name VARCHAR(100),
    department_name VARCHAR(100),
    product_price DECIMAL(10,2)
);


CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT,
    month_name VARCHAR(20),
    quarter VARCHAR(10),
    year INT
);


CREATE TABLE dim_shipping (
    shipping_id INT PRIMARY KEY,
    shipping_mode VARCHAR(50),
    delivery_status VARCHAR(100),
    actual_shipping_days INT,
    scheduled_shipping_days INT,
    late_delivery_risk INT
);


CREATE TABLE fact_orders (
    order_item_id INT PRIMARY KEY,

    customer_id INT,
    product_id INT,
    date_id INT,
    shipping_id INT,

    sales DECIMAL(10,2),
    profit DECIMAL(10,2),
    quantity INT,
    discount DECIMAL(10,2),

    FOREIGN KEY (customer_id)
        REFERENCES dim_customer(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES dim_product(product_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id),

    FOREIGN KEY (shipping_id)
        REFERENCES dim_shipping(shipping_id)
);