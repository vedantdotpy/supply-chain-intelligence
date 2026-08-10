# Supply Chain & Demand Intelligence Platform

An end-to-end analytics and decision-support project that analyzes supply chain operations, customer demand, logistics performance, and profitability — then converts those findings into forecasts, decision models, and business recommendations.

## Business Problem

A large company is facing rising supply chain costs and recurring operational problems. Management needs answers to four questions:

1. What is happening?
2. Why is it happening?
3. What is likely to happen next?
4. What decisions should we make about it?

This project works through those four questions using a real-world supply chain dataset, moving from raw data to executive-level recommendations.

## Objectives

1. Understand and validate the dataset (structure, grain, quality)
2. Build a reproducible data cleaning pipeline
3. Perform exploratory data analysis (EDA)
4. Develop business KPIs
5. Analyze sales, profit, customers, products, geography, and shipping performance
6. Identify inefficiencies and root causes
7. Analyze demand trends and seasonality
8. Forecast future demand
9. Build decision-support and scenario models
10. Communicate findings through an executive dashboard
11. Produce clear, evidence-based recommendations

## Key Business Questions

### Revenue & Profitability

- Which products and categories generate the most revenue?
- Which products generate the highest profit margins?
- Which markets and regions contribute most to profitability?
- Are high-revenue products necessarily high-profit products?

### Customer & Demand

- Which customer segments generate the most value?
- How does demand vary across products, regions, and time?
- Which products exhibit stable versus volatile demand?
- Are there identifiable seasonal demand patterns?

### Logistics & Delivery

- Which shipping modes perform best?
- Which regions experience the highest delivery risk?
- What factors are associated with late deliveries?
- Where should operational improvements be prioritized?

### Decision Support

- Where should management prioritize intervention?
- What trade-offs exist between cost, service performance, and demand?
- How could demand forecasting improve operational planning?
- Which decisions could provide the greatest potential business impact?

## Project Architecture

```
Raw Data
   │
   ▼
Python / Pandas — validation & cleaning
   │
   ▼
Feature Engineering
   │
   ├──► Exploratory Analysis
   └──► Statistical Analysis
   │
   ▼
SQL Analytics
   │
   ▼
Demand Analysis
   │
   ▼
Forecasting
   │
   ▼
Decision Modeling
   │
   ▼
Power BI Dashboard
   │
   ▼
Business Recommendations
```

## Technology Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Data manipulation | Pandas, NumPy |
| Statistics | SciPy, Statsmodels *(planned)* |
| Machine learning / forecasting | Scikit-learn, Statsmodels *(planned)* |
| Database | PostgreSQL *(planned)* |
| BI / Visualization | Power BI *(planned)* |
| Version control | Git, GitHub |

Python, Pandas, NumPy, Git, and GitHub are currently in active use. Other tools will be introduced — and added to `requirements.txt` — as the project reaches the phase that needs them.

## Dataset

**DataCo Smart Supply Chain for Big Data Analysis**

- Source: [Mendeley Data](https://data.mendeley.com/datasets/8gx2fvg2k6/5)
- DOI: `10.17632/8gx2fvg2k6.5`
- Contributors: Fabian Constante, Fernando Silva, António Pereira
- License: CC BY 4.0

The dataset contains structured supply chain data (provisioning, production, sales, and commercial distribution) alongside a clickstream/access-log file capturing online customer behavior.

Raw data files are **not included in this repository** due to their size (~187 MB combined). The dataset is available under the CC BY 4.0 license from the official Mendeley Data repository.

1. Download the dataset from the Mendeley link above
2. Place the files in `data/raw/`:
   - `DataCoSupplyChainDataset.csv`
   - `DescriptionDataCoSupplyChain.csv`
   - `tokenized_access_logs.csv`

> **Note:** Not every variable initially expected (e.g. warehouse stock levels, reorder points) is guaranteed to exist in this dataset. Any analysis relying on data not present in the source will be clearly labeled as a documented assumption or simulation, distinct from actual source data.

## Repository Structure

```
supply-chain-intelligence/
│
├── data/
│   ├── raw/                 # Original datasets (not tracked)
│   └── processed/           # Cleaned datasets (not tracked)
│
├── notebooks/               # Exploratory and analytical notebooks
│
├── src/
│   ├── data/                # Data loading and cleaning scripts
│   ├── analysis/            # Analytical functions
│   └── models/              # Forecasting and decision models
│
├── sql/                     # SQL schema and analysis queries
│
├── dashboard/                # Power BI dashboard files
│
├── reports/                  # Executive reports
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Analytical Techniques

- Data quality assessment and validation
- Exploratory data analysis (univariate, bivariate, multivariate)
- KPI development (revenue, profit margin, AOV, delivery performance)
- Customer and geographic segmentation
- Hypothesis testing and statistical inference
- SQL-based analytics (joins, window functions, CTEs)
- Time series demand forecasting
- Decision and scenario modeling (cost/service trade-offs, sensitivity analysis)

## Key Deliverables

- Reproducible Python data-cleaning pipeline
- Data-quality assessment
- Exploratory data analysis
- Business KPI framework
- Customer, product, and geographic analysis
- Logistics and delivery analysis
- SQL analytical layer
- Demand and time-series analysis
- Demand forecasting models
- Decision and scenario models
- Executive Power BI dashboard
- Executive business report
- Evidence-based business recommendations

## Project Status

**Current phase: Project setup**

- [x] Dataset selected and downloaded
- [x] Project repository initialized
- [x] Git repository created and connected to GitHub
- [x] `.gitignore` configured to exclude raw data
- [ ] Dataset investigation (grain, entities, data quality)
- [ ] Data cleaning pipeline
- [ ] Exploratory data analysis
- [ ] Statistical analysis
- [ ] SQL layer
- [ ] Demand forecasting
- [ ] Decision models
- [ ] Power BI dashboard
- [ ] Final executive report

This README will be updated as each phase is completed.

## Reproducibility

```bash
git clone https://github.com/vedantdotpy/supply-chain-intelligence.git
cd supply-chain-intelligence
pip install -r requirements.txt
```

Then download the dataset as described above and place it in `data/raw/`.

## Author

**Vedant Mishra**
B.Tech, Industrial Internet of Things (IIoT) — University School of Automation and Robotics, GGSIPU, New Delhi
GitHub: [@vedantdotpy](https://github.com/vedantdotpy)

## Project Philosophy

> **Good analytics does not end with a chart. It ends with a better decision.**

The goal of this project is to demonstrate the complete journey from raw data to actionable business intelligence — combining technical analysis, statistical reasoning, forecasting, decision-making, and clear business communication.