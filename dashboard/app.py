import streamlit as st
import plotly.express as px
from queries import (
    get_kpis,
    get_monthly_sales,
    get_top_products,
    get_customer_segments,
    get_shipping_analysis
)

# Page configuration

st.set_page_config(
    page_title="Supply Chain Intelligence",
    layout="wide"
)


st.title("Supply Chain Intelligence Dashboard")
st.sidebar.header("Filters")


selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All", 2015, 2016, 2017, 2018]
)

# Load KPIs

kpi_data = get_kpis()

total_sales = kpi_data["total_sales"][0]
total_profit = kpi_data["total_profit"][0]
total_orders = kpi_data["total_orders"][0]
average_order_value = kpi_data["average_order_value"][0]


# KPI Cards

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Sales",
        f"${total_sales/1_000_000:,.2f}M"
    )


with col2:
    st.metric(
        "Total Profit",
        f"${total_profit/1_000_000:,.2f}M"
    )


with col3:
    st.metric(
        "Total Orders",
        f"{total_orders:,}"
    )


with col4:
    st.metric(
        "Average Order Value",
        f"${average_order_value:,.2f}"
    )

# MONTHLY REVENUE TREND

st.subheader("Monthly Revenue Trend")

if selected_year == "All":
    monthly_sales = get_monthly_sales()
else:
    monthly_sales = get_monthly_sales(selected_year)

monthly_sales["period"] = (
    monthly_sales["year"].astype(str)
    + "-"
    + monthly_sales["month"].astype(str)
)


fig = px.line(
    monthly_sales,
    x="period",
    y="revenue",
    markers=True,
    title="Revenue Over Time"
)

fig.update_yaxes(
    tickformat="$,.0s"
)


st.plotly_chart(
    fig,
    use_container_width=True
)

# PRODUCT + CUSTOMER ANALYSIS

col1, col2 = st.columns(2)


with col1:

    st.subheader("Top 10 Products by Revenue")

    top_products = get_top_products()


    fig = px.bar(
    top_products.sort_values("revenue"),
    x="revenue",
    y="product_name",
    orientation="h",
    title="Top Performing Products"
)
    


    st.plotly_chart(
        fig,
        width="stretch"
    )



with col2:

    st.subheader("Revenue by Customer Segment")

    customer_segments = get_customer_segments()


    fig = px.bar(
        customer_segments,
        x="segment",
        y="revenue",
        title="Revenue Contribution by Segment",
        text="revenue"
    )


    fig.update_traces(
        textposition="outside"
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )

# SHIPPING PERFORMANCE

st.subheader("Shipping Performance")


shipping_analysis = get_shipping_analysis()


fig = px.bar(
    shipping_analysis,
    x="shipping_mode",
    y="late_orders",
    title="Late Deliveries by Shipping Mode",
    text="late_orders"
)


fig.update_traces(
    textposition="outside"
)


st.plotly_chart(
    fig,
    width="stretch"
)