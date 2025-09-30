import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("gdp_data.csv")

# Pick a country
country = "United States"

# Filter for that country
gdp_row = df[df["Country Name"] == country]
#####################################################
# Reshape data: years as rows, GDP as values
gdp = gdp_row.loc[:, "1960":"2024"].T.reset_index()
gdp.columns = ["Year", "GDP"]

# Convert Year to int and GDP to numeric
gdp["Year"] = gdp["Year"].astype(int)
gdp["GDP"] = pd.to_numeric(gdp["GDP"], errors="coerce")

# Drop missing values
gdp = gdp.dropna()

# Calculate growth rate as %
gdp["GrowthRate"] = gdp["GDP"].pct_change() * 100

#GDP over time
plt.figure(figsize=(10, 5))
plt.plot(gdp["Year"], gdp["GDP"], color="blue", label="GDP")
plt.title(f"GDP of {country} Over Time")
plt.xlabel("Year")
plt.ylabel("GDP (in Tens of Trillions US$)")
plt.legend()
plt.show()

#Plot growth in percentage
plt.figure(figsize=(10, 5))
plt.plot(gdp["Year"], gdp["GrowthRate"], color="green", label="Growth Rate")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.title(f"GDP Growth Rate of {country}")
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")
plt.legend()
plt.show()
