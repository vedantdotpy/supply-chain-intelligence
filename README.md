# Supply Chain Intelligence Analytics Dashboard

A complete end-to-end data analytics project focused on analyzing supply chain performance, sales trends, customer behavior, product profitability, and delivery operations.

The project transforms raw transactional supply chain data into clean analytical datasets and business insights that can support data-driven decision making.

---

# Business Problem

Companies operating in large-scale supply chains need visibility into:

- Overall sales and profitability performance
- Product contribution and profitability
- Customer segment behavior
- Geographic sales distribution
- Delivery efficiency
- Discount impact on profitability

This project analyzes historical supply chain data to identify key business drivers, operational issues, and optimization opportunities.

---

# Project Objectives

The main objectives of this project are:

- Build a reliable data cleaning pipeline
- Perform exploratory data analysis
- Identify important business KPIs
- Analyze product and customer performance
- Evaluate shipping and delivery efficiency
- Understand discount and profitability relationships
- Prepare analytics datasets for dashboard development

---

# Dataset Overview

The dataset contains transactional supply chain records including:

- Orders
- Customers
- Products
- Sales
- Profit
- Discounts
- Shipping details
- Delivery information
- Geographic attributes

Dataset size after cleaning:

- Rows: 180,519
- Columns: 53

Analysis period:

```
January 2015 - January 2018
```

---

# Project Architecture

```
Raw Data
    |
    |
    v
Data Cleaning Pipeline
(02_data_cleaning.ipynb)
    |
    |
    v
Clean Dataset
    |
    |
    v
Exploratory Data Analysis
(03_exploratory_data_analysis.ipynb)
    |
    |
    v
Analytics Layer
    |
    |
    v
Dashboard Development
(Power BI / Streamlit)
```

---

# Repository Structure

```
Supply-Chain-Intelligence

│
├── data
│   │
│   ├── raw
│   │
│   ├── processed
│   │
│   └── analytics
│       ├── monthly_performance.csv
│       ├── product_performance.csv
│       ├── customer_segment_analysis.csv
│       ├── country_analysis.csv
│       ├── shipping_analysis.csv
│       └── discount_analysis.csv
│
├── notebooks
│   │
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_exploratory_data_analysis.ipynb
│
└── README.md
```

---

# Technologies Used

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn

## Development Environment

- Jupyter Notebook
- VS Code

## Version Control

- Git
- GitHub

---

# Key Business KPIs

The following KPIs were calculated:

| KPI | Value |
|---|---:|
| Gross Sales | $36.78M |
| Net Sales | $33.05M |
| Total Profit | $3.96M |
| Profit Margin | 12% |
| Orders | 65,752 |
| Customers | 20,652 |
| Units Sold | 384,079 |
| Average Order Value | $502.71 |

---

# Key Insights

## Product Performance

- A small number of products contribute a majority of revenue.
- Top 10 products contribute approximately 90% of total revenue.
- Three products were identified with negative profitability.

---

## Customer Segment Analysis

Customer contribution:

| Segment | Revenue |
|---|---:|
| Consumer | $19.09M |
| Corporate | $11.16M |
| Home Office | $6.52M |

The Consumer segment is the largest revenue contributor.

---

## Delivery Performance

Delivery analysis revealed:

- Late deliveries represent a significant operational challenge.
- Approximately 54.83% of orders have late delivery risk.
- Shipping mode performance varies significantly.

---

## Discount Analysis

Analysis showed:

- Increasing discounts do not necessarily increase profitability.
- Higher discount levels generally reduce profit contribution.
- Discount strategies should be optimized carefully.

---

# Analytics Datasets Generated

The project produces reusable analytical datasets:

### Monthly Performance

Tracks:

- Revenue trends
- Profit trends
- Orders
- Units sold


### Product Performance

Tracks:

- Revenue contribution
- Profitability
- Units sold
- Product ranking


### Customer Analysis

Tracks:

- Customer segments
- Revenue contribution
- Profit contribution


### Geographic Analysis

Tracks:

- Country-level performance
- Revenue
- Profit
- Orders


### Shipping Analysis

Tracks:

- Delivery performance
- Shipping mode efficiency
- Late delivery risk


### Discount Analysis

Tracks:

- Discount levels
- Revenue impact
- Profit impact

---

# Future Improvements

Future development includes:

- Power BI executive dashboard
- Interactive Streamlit dashboard
- Sales forecasting model
- Customer segmentation using machine learning
- Delivery delay prediction model

---

# Author

Vedant Mishra

B.Tech - Industrial Internet of Things

Data Analytics | Python | SQL | Business Intelligence

GitHub:
https://github.com/vedantdotpy