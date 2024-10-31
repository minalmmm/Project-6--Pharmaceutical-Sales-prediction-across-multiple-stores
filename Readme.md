# Pharmaceutical Store Sales Prediction using Time Series

## Overview
This project aims to forecast daily sales across multiple pharmaceutical stores six weeks in advance. Built for Rossmann Pharmaceuticals, this end-to-end solution leverages both machine learning and deep learning techniques, along with a web interface for prediction. It provides store managers with insights to optimize staffing, inventory, and promotional strategies.

## Table of Contents
- [Business Need](#business-need)
- [Data and Features](#data-and-features)
- [Installation and Setup](#installation-and-setup)
- [Modeling Pipeline](#modeling-pipeline)
- [Memory Management and Updates](#memory-management-and-updates)
- [Output and Visualization](#output-and-visualization)
- [Deployment](#deployment)
- [Future Work](#future-work)

## Business Need
The Rossmann Pharmaceuticals finance team requires sales forecasts to streamline operational planning. Predictive insights help managers make informed decisions based on customer patterns influenced by holidays, promotions, competition, and other seasonal factors.

## Data and Features
The dataset includes various features:
- **Id**: Store-Date combination.
- **Store**: Unique store ID.
- **Sales**: Target variable representing daily sales.
- **Customers**: Daily customer count.
- **Open**: Store open indicator.
- **Promo**: Promo on that day (1: active, 0: none).
- **StateHoliday**: Type of holiday affecting sales.
- **SchoolHoliday**: Indicator if public schools were closed.
- Additional engineered features like the number of days to the next holiday, weekend/weekday, competitor distance, and promo interval
## output 
for i in range(1, 7):
    plt.figure(figsize=(10, 6))
    plt.plot(predicted_sales[i], label=f"Week {i} Prediction")  # Replace with actual prediction plotting code
    plt.xlabel("Days")
    plt.ylabel("Sales")
    plt.legend()
    plt.title(f"Sales Prediction for Week {i}")
    plt.savefig(f'image{i}.png')
    plt.show()

"# Project-6--Pharmaceutical-Sales-prediction-across-multiple-stores" 
