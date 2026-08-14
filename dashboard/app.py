import streamlit as st
import plotly.express as px

from queries import (
    get_kpis,
    get_monthly_sales,
    get_top_products,
    get_customer_segments,
    get_shipping_analysis,
    get_profit_by_category,
    get_discount_analysis
)


# PAGE CONFIGURATION

st.set_page_config(
    page_title="Supply Chain Intelligence",
    layout="wide"
)


st.title("🚚 Supply Chain Intelligence Dashboard")

st.sidebar.header("Filters")


selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All", 2015, 2016, 2017, 2018]
)



# LOAD KPIs

kpi_data = get_kpis()


total_sales = kpi_data["total_sales"][0]
total_profit = kpi_data["total_profit"][0]
total_orders = kpi_data["total_orders"][0]
average_order_value = kpi_data["average_order_value"][0]

profit_margin = kpi_data["profit_margin"][0]
late_delivery_rate = kpi_data["late_delivery_rate"][0]
average_shipping_days = kpi_data["average_shipping_days"][0]



# KPI CARDS

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



col5, col6, col7 = st.columns(3)


with col5:
    st.metric(
        "Profit Margin",
        f"{profit_margin}%"
    )


with col6:
    st.metric(
        "Late Delivery Rate",
        f"{late_delivery_rate}%"
    )


with col7:
    st.metric(
        "Avg Shipping Days",
        f"{average_shipping_days} days"
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
    width="stretch"
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



# PROFITABILITY ANALYSIS


st.subheader("Profitability Analysis")


col1, col2 = st.columns(2)



with col1:

    profit_category = get_profit_by_category()


    fig = px.bar(
        profit_category,
        x="category_name",
        y="profit_margin",
        title="Top Categories by Profit Margin %",
        text="profit_margin"
    )


    fig.update_traces(
        textposition="outside"
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )



with col2:

    discount_analysis = get_discount_analysis()


fig = px.bar(
    discount_analysis,
    x="discount_range",
    y="profit_margin",
    text="profit_margin",
    title="Discount Impact on Profit Margin"
)


fig.update_traces(
    textposition="outside"
)


st.plotly_chart(
    fig,
    width="stretch"
)

# BUSINESS INSIGHTS

st.subheader("Business Insights")


profit_category = get_profit_by_category()


best_category = (
    profit_category
    .sort_values(
        "profit_margin",
        ascending=False
    )
    .iloc[0]
)


discount_data = get_discount_analysis()


best_discount = (
    discount_data
    .sort_values(
        "profit_margin",
        ascending=False
    )
    .iloc[0]
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Most Profitable Category",
        best_category["category_name"]
    )


with col2:

    st.metric(
        "Highest Profit Margin",
        f"{best_category['profit_margin']}%"
    )


with col3:

    st.metric(
        "Best Discount Range",
        best_discount["discount_range"]
    )