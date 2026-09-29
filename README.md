# Crop Production Analysis Dashboard

Interactive data analysis of crop yield across Indian states, built to identify what actually drives agricultural yield, nutrient levels, climate, or crop choice.

**Live app:** https://crop-analysis-dashboard.streamlit.app/

## Key Finding

Nutrient levels (N/P/K) show a moderate correlation with yield (0.42, 0.36, 0.36), but this is confounded by crop type. Grouping by crop reveals that high apparent "nutrient-driven" yield is actually explained by a small set of naturally high-biomass crops (banana, tapioca, papaya) that happen to use specific fertilizer dosages, not nutrient dosage causing higher yield. Crop choice and regional growing conditions are the stronger drivers.

## What's in this analysis

- **Data cleaning:** identified and removed 39 outlier rows (yield exceeding physically plausible maximums, likely unit/entry errors) out of 99,849 records
- **Failure analysis:** zero-yield crops (complete crop failures) statistically linked to higher rainfall (p < 0.001), concentrated in perishable vegetable crops, consistent with waterlogging damage
- **Correlation analysis:** nutrient/climate variables vs. yield, with crop-type confounding identified and investigated
- **Regional efficiency vs. volume:** states ranked separately by yield-per-hectare vs. total production, showing these are distinct, sometimes contradictory, metrics (e.g. Uttar Pradesh leads in total production but not in yield efficiency for its top crops)
- **SQL analysis:** window functions, CTEs, conditional aggregation, subqueries, and self-joins run against the cleaned dataset in SQLite
- **Interactive dashboard:** dropdown-driven crop selector for state-wise yield exploration

## Tech stack

Python, pandas, SQLite, seaborn/matplotlib, Streamlit

## Run locally

```bash
git clone https://github.com/Prib15/crop-production-dashboard.git
cd crop-production-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## Dataset

Crop production data (India), sourced from Kaggle, 99,849 records across 33 states and 53 crop types.
