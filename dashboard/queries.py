import pandas as pd

from database import engine

# EXECUTIVE KPIs

def get_kpis():

    query = """
    SELECT
        SUM(sales) AS total_sales,
        SUM(profit) AS total_profit,
        COUNT(order_item_id) AS total_orders,
        ROUND(
            SUM(sales) / COUNT(order_item_id),
            2
        ) AS average_order_value
    FROM fact_orders;
    """

    return pd.read_sql(query, engine)

# MONTHLY SALES TREND

def get_monthly_sales(year=None):

    query = """
    SELECT
        d.year,
        d.month,
        d.month_name,
        SUM(f.sales) AS revenue,
        SUM(f.profit) AS profit

    FROM fact_orders f

    JOIN dim_date d
    ON f.date_id = d.date_id
    """

    if year:
        query += f"""
        WHERE d.year = {year}
        """


    query += """
    GROUP BY
        d.year,
        d.month,
        d.month_name

    ORDER BY
        d.year,
        d.month;
    """


    return pd.read_sql(query, engine)

# TOP PRODUCTS

def get_top_products():

    query = """
    SELECT
        p.product_name,
        SUM(f.sales) AS revenue,
        SUM(f.profit) AS profit

    FROM fact_orders f

    JOIN dim_product p
    ON f.product_id = p.product_id

    GROUP BY
        p.product_name

    ORDER BY
        revenue DESC

    LIMIT 10;
    """

    return pd.read_sql(query, engine)

# CUSTOMER SEGMENTS

def get_customer_segments():

    query = """
    SELECT
        c.segment,
        SUM(f.sales) AS revenue,
        SUM(f.profit) AS profit,
        COUNT(f.order_item_id) AS orders

    FROM fact_orders f

    JOIN dim_customer c
    ON f.customer_id = c.customer_id

    GROUP BY
        c.segment

    ORDER BY
        revenue DESC;
    """

    return pd.read_sql(query, engine)

# SHIPPING PERFORMANCE

def get_shipping_analysis():

    query = """
    SELECT
        s.shipping_mode,
        COUNT(f.order_item_id) AS orders,
        AVG(s.actual_shipping_days) AS avg_shipping_days,
        SUM(s.late_delivery_risk) AS late_orders

    FROM fact_orders f

    JOIN dim_shipping s
    ON f.shipping_id = s.shipping_id

    GROUP BY
        s.shipping_mode

    ORDER BY
        late_orders DESC;
    """

    return pd.read_sql(query, engine)
