import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crop Yield Analysis", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('Crop_production.csv', index_col='ID')
    df = df[df['Yield_ton_per_hec'] <= 100].copy()
    return df

crop_prod_clean = load_data()

st.title("Crop Production Analysis: India")
st.markdown("Analysis of yield drivers across states, crops, and nutrient levels.")

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Records", f"{len(crop_prod_clean):,}")
with col2:
    st.metric("Unique Crops", crop_prod_clean['Crop'].nunique())

st.subheader("Correlation: Nutrients, Climate vs Yield")
numeric_cols = ['N','P','K','pH','rainfall','temperature','Yield_ton_per_hec']
corr_matrix = crop_prod_clean[numeric_cols].corr()
fig1, ax1 = plt.subplots(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax1)
st.pyplot(fig1)

st.subheader("Nitrogen (N) vs Yield")
fig2, ax2 = plt.subplots(figsize=(8,6))
sns.scatterplot(data=crop_prod_clean, x='N', y='Yield_ton_per_hec', alpha=0.15, s=15, ax=ax2)
sns.regplot(data=crop_prod_clean, x='N', y='Yield_ton_per_hec', scatter=False, color='red', ax=ax2)
st.pyplot(fig2)

st.subheader("Yield Distribution by Crop (Top 15 by Median Yield)")
top_crops = crop_prod_clean.groupby('Crop')['Yield_ton_per_hec'].median().sort_values(ascending=False).head(15).index
fig3, ax3 = plt.subplots(figsize=(10,6))
sns.boxplot(data=crop_prod_clean[crop_prod_clean['Crop'].isin(top_crops)], 
            x='Crop', y='Yield_ton_per_hec', order=top_crops, ax=ax3)
ax3.tick_params(axis='x', rotation=45)
st.pyplot(fig3)

st.subheader("Banana Yield by State (Top 10 States)")
banana_data = crop_prod_clean[crop_prod_clean['Crop']=='banana']
top_states = banana_data.groupby('State_Name')['Yield_ton_per_hec'].median().sort_values(ascending=False).head(10).index
fig4, ax4 = plt.subplots(figsize=(10,6))
sns.boxplot(data=banana_data[banana_data['State_Name'].isin(top_states)],
            x='State_Name', y='Yield_ton_per_hec', order=top_states, ax=ax4)
ax4.tick_params(axis='x', rotation=45)
st.pyplot(fig4)

st.subheader("Top 10 States by Total Production")
state_production = crop_prod_clean.groupby('State_Name')['Production_in_tons'].sum().sort_values(ascending=False).head(10)
fig5, ax5 = plt.subplots(figsize=(10,6))
sns.barplot(x=state_production.values, y=state_production.index, orient='h', ax=ax5)
ax5.set_xlabel("Total Production (tons)")
st.pyplot(fig5)

st.subheader("Explore: Yield by State for Any Crop")
crop_list = sorted(crop_prod_clean['Crop'].unique())
selected_crop = st.selectbox("Select a crop", crop_list, index=crop_list.index('banana'))

crop_filtered = crop_prod_clean[crop_prod_clean['Crop'] == selected_crop]
top_states_selected = crop_filtered.groupby('State_Name')['Yield_ton_per_hec'].median().sort_values(ascending=False).head(10).index

fig6, ax6 = plt.subplots(figsize=(10,6))
sns.boxplot(data=crop_filtered[crop_filtered['State_Name'].isin(top_states_selected)],
            x='State_Name', y='Yield_ton_per_hec', order=top_states_selected, ax=ax6)
ax6.tick_params(axis='x', rotation=45)
ax6.set_title(f"{selected_crop.title()} Yield by State (Top 10)")
st.pyplot(fig6)

st.caption(f"Showing {len(crop_filtered)} records for {selected_crop}.")