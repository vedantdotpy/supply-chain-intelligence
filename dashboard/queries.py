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
            (SUM(sales) / COUNT(order_item_id))::numeric,
            2
        ) AS average_order_value,


        ROUND(
            ((SUM(profit) / SUM(sales)) * 100)::numeric,
            2
        ) AS profit_margin,


        ROUND(
            (
                SUM(
                    CASE
                        WHEN s.late_delivery_risk = 1
                        THEN 1
                        ELSE 0
                    END
                )::numeric
                /
                COUNT(f.order_item_id)
            ) * 100,
            2
        ) AS late_delivery_rate,


        ROUND(
            AVG(s.actual_shipping_days)::numeric,
            2
        ) AS average_shipping_days


    FROM fact_orders f


    JOIN dim_shipping s
    ON f.shipping_id = s.shipping_id;

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

# PROFITABILITY BY CATEGORY

def get_profit_by_category():

    query = """
    SELECT
        p.category_name,

        SUM(f.sales) AS revenue,

        SUM(f.profit) AS profit,

        (
            SUM(f.profit)::numeric
            /
            NULLIF(SUM(f.sales)::numeric,0)
            * 100
        )::numeric(10,2) AS profit_margin


    FROM fact_orders f


    JOIN dim_product p
    ON f.product_id = p.product_id


    GROUP BY
        p.category_name


    ORDER BY
        profit_margin DESC


    LIMIT 10;
    """


    return pd.read_sql(query, engine)

def get_discount_analysis():

    query = """

    SELECT

        CASE
            WHEN discount <= 0.10 THEN '0-10%'
            WHEN discount <= 0.20 THEN '10-20%'
            WHEN discount <= 0.30 THEN '20-30%'
            ELSE '30%+'
        END AS discount_range,

        SUM(sales) AS revenue,

        ROUND(
    CAST(
        (
            SUM(profit)::numeric
            /
            NULLIF(SUM(sales)::numeric,0)
        ) * 100
    AS numeric),
    2
) AS profit_margin


    FROM fact_orders


    GROUP BY

        CASE
            WHEN discount <= 0.10 THEN '0-10%'
            WHEN discount <= 0.20 THEN '10-20%'
            WHEN discount <= 0.30 THEN '20-30%'
            ELSE '30%+'
        END


    ORDER BY
        discount_range;

    """


    with engine.raw_connection() as connection:

        df = pd.read_sql_query(
            query,
            connection
        )

    return df