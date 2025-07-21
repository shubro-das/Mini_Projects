# weather_analyzer/main.py

import pandas as pd

# Load the weather dataset
df = pd.read_csv("weather.csv")

# Rename columns to simpler names
df.rename(columns={
    'Data.Precipitation': 'Precipitation',
    'Date.Full': 'Date',
    'Date.Month': 'Month',
    'Date.Week of': 'Week',
    'Date.Year': 'Year',
    'Station.City': 'City',
    'Station.Code': 'Code',
    'Station.Location': 'Location',
    'Station.State': 'State',
    'Data.Temperature.Avg Temp': 'AvgTemp',
    'Data.Temperature.Max Temp': 'MaxTemp',
    'Data.Temperature.Min Temp': 'MinTemp',
    'Data.Wind.Direction': 'WindDirection',
    'Data.Wind.Speed': 'WindSpeed'
}, inplace=True)

# Optional: print the cleaned column names
print("\n✅ Renamed Columns:")
print(df.columns.tolist())


# Show the first 5 rows
print("\n🔹 First 5 Rows:")
print(df.head())

# Show column names
print("\n🔹 Columns in the dataset:")
print(df.columns.tolist())

# Basic info: rows, columns, data types
print("\n🔹 Dataset Info:")
print(df.info())

# Basic stats (for numeric columns)
print("\n🔹 Statistical Summary:")
print(df.describe())
