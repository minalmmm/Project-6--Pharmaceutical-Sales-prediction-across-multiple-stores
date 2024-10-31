import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import load_model
from PIL import Image

# Function to load the model
def load_my_model():
    model_path = r"C:\data science material\project_6\model\model.h5"
    model = load_model(model_path)
    return model

# Load the model
model = load_my_model()

# Display image
image_path = r"C:\data science material\project_6\Notebook\image_rossman.jpg"
image = Image.open(image_path)
st.image(image, caption="Pharmaceutical Sales Forecasting", use_column_width=True)

# Dashboard Title
st.title("Pharmaceutical Sales Prediction Dashboard")

# Sidebar for filters
st.sidebar.header("Filter Options")
store_id = st.sidebar.number_input("Store ID", min_value=1, step=1, value=1)
is_holiday = st.sidebar.selectbox("Is Holiday", ["Yes", "No"])
is_weekend = st.sidebar.selectbox("Is Weekend", ["Yes", "No"])
is_promo = st.sidebar.selectbox("Is Promo", ["Yes", "No"])

# File uploader
uploaded_file = st.file_uploader("Upload CSV file with test data", type=['csv'])

# Load and display data
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:", df.head())

    # Data Preprocessing
    df['IsHoliday'] = df['StateHoliday'].apply(lambda x: 1 if x != '0' else 0)
    df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 1 if x >= 6 else 0)
    df['IsPromo'] = df['Promo']
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter data by store ID
    df_filtered = df[df['Store'] == store_id]

    # Prepare data for prediction
    input_data = df_filtered[['IsHoliday', 'IsWeekend', 'IsPromo']]
    input_data['Day'] = df_filtered['Date'].dt.day
    input_data['Month'] = df_filtered['Date'].dt.month
    input_data['Year'] = df_filtered['Date'].dt.year

    # Convert to NumPy array for prediction
    input_data_np = input_data.values

    # Generate predictions
    predictions = model.predict(input_data_np)

    # Add predictions to dataframe
    df_filtered['Predicted Sales'] = predictions.flatten()

    # Display predictions
    st.write("Predicted Sales Data for Store ID", store_id)
    st.write(df_filtered[['Date', 'Predicted Sales']])

    # User selection for chart type
    st.subheader("Select Chart Type")
    chart_type = st.selectbox("Choose the chart type:", ["Daily", "Monthly", "Yearly"])

    # Daily Sales Prediction Plot
    if chart_type == "Daily":
        st.subheader("Predicted Daily Sales")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=df_filtered, x='Date', y='Predicted Sales', ax=ax)
        ax.set_title(f"Daily Sales Predictions for Store {store_id}")
        st.pyplot(fig)

    # Monthly Sales Prediction Plot
    elif chart_type == "Monthly":
        st.subheader("Predicted Monthly Sales")
        df_filtered['YearMonth'] = df_filtered['Date'].dt.to_period('M')
        monthly_sales = df_filtered.groupby('YearMonth')['Predicted Sales'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=monthly_sales, x='YearMonth', y='Predicted Sales', ax=ax, palette="Blues_d")
        plt.xticks(rotation=45)
        ax.set_title("Monthly Sales Predictions")
        st.pyplot(fig)

    # Yearly Sales Prediction Plot
    elif chart_type == "Yearly":
        st.subheader("Predicted Yearly Sales")
        yearly_sales = df_filtered.groupby(df_filtered['Date'].dt.year)['Predicted Sales'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=yearly_sales, x='Date', y='Predicted Sales', ax=ax, palette="Greens_d")
        ax.set_title("Yearly Sales Predictions")
        st.pyplot(fig)

    # Download Button for Predictions CSV
    st.subheader("Download Predicted Sales Data")
    download_df = df_filtered[['Date', 'Predicted Sales']]
    st.download_button(
        label="Download Predictions as CSV",
        data=download_df.to_csv(index=False),
        file_name="predicted_sales.csv",
        mime="text/csv"
    )
