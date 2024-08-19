
import streamlit as st
import pandas as pd
import plotly.express as px
vehicles = pd.read_csv('vehicles_us.csv')
vehicles['price'] = vehicles['price'].astype(float)
vehicles['model_year'] = vehicles['model_year'].astype(float)
vehicles['odometer'] = vehicles['odometer'].astype(float)
vehicles['cylinders'] = vehicles['cylinders'].astype(float)
# converting variables to same type to make calculations easier
# Streamlit app setup
st.title('Vehicle Listings Data Visualization')

# Display dataset preview
st.header('Data Overview')
st.write('Here is a preview of the dataset:')
st.write(vehicles.head())

# Histogram for price distribution
st.header('Histogram of Vehicle Prices')

# Checkbox to show/hide histogram
show_histogram = st.checkbox('Show Histogram', value=True)
if show_histogram:
    if 'price' in vehicles.columns:
        fig_hist = px.histogram(vehicles, x='price', title='Histogram of Vehicle Prices')
        st.plotly_chart(fig_hist)
    else:
        st.write('Price column is not available in the dataset.')

# Scatter plot for price vs. odometer
st.header('Scatter Plot of Price vs. Odometer')

# Checkbox to show/hide scatter plot
show_scatter = st.checkbox('Show Scatter Plot', value=True)
if show_scatter:
    if 'price' in vehicles.columns and 'odometer' in vehicles.columns:
        fig_scatter = px.scatter(vehicles, x='odometer', y='price', title='Scatter Plot of Price vs. Odometer')
        st.plotly_chart(fig_scatter)
    else:
        st.write('Price or Odometer column is not available in the dataset.')