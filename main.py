# Day 20 — Mini Project #3
# Sales Data Analysis — Part 2
import pandas as pd
import matplotlib.pyplot as plt
# Load Dataset
df = pd.read_csv("sales_data_day20.csv")
print()
print("----- Sales Data Analysis -----")
print()
# Calculate Sales
df["Sales"] = df["Quantity"] * df["Price"]
# Convert Date
df["Date"] = pd.to_datetime(df["Date"])
# Create Month Column
df["Month"] = df["Date"].dt.month
# Product-wise Sales
product_sales = df.groupby("Product")["Sales"].sum()
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()
print("----- Product-wise Sales -----")
print(product_sales)
print()
print("Best Product:", best_product)
print("Best Product Sales:", best_product_sales)
# City-wise Sales
city_sales = df.groupby("City")["Sales"].sum()
best_city = city_sales.idxmax()
best_city_sales = city_sales.max()
print()
print("----- City-wise Sales -----")
print(city_sales)
print()
print("Best City:", best_city)
print("Best City Sales:", best_city_sales)
# Region-wise Sales
region_sales = df.groupby("Region")["Sales"].sum()
best_region = region_sales.idxmax()
best_region_sales = region_sales.max()
print()
print("----- Region-wise Sales -----")
print(region_sales)
print()
print("Best Region:", best_region)
print("Best Region Sales:", best_region_sales)
# Customer-wise Sales
customer_sales = df.groupby("Customer")["Sales"].sum()
best_customer = customer_sales.idxmax()
best_customer_sales = customer_sales.max()
print()
print("----- Customer-wise Sales -----")
print(customer_sales)
print()
print("Best Customer:", best_customer)
print("Best Customer Sales:", best_customer_sales)
# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()
print()
print("----- Monthly Sales -----")
print(monthly_sales)
print()
print("Best Month:", best_month)
print("Best Month Sales:", best_month_sales)
# Chart 1 — Product-wise Sales
plt.bar(product_sales.index, product_sales.values)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product-wise Sales")
plt.savefig("screenshots/product_sales.png")
plt.show()
# Chart 2 — Monthly Sales Trend
plt.plot(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.savefig("screenshots/monthly_sales.png")
plt.show()
# Chart 3 — Region-wise Sales
plt.bar(region_sales.index, region_sales.values)
plt.xlabel("Region")
plt.ylabel("Sales")
plt.title("Region-wise Sales")
plt.savefig("screenshots/region_sales.png")
plt.show()
# Chart 4 — Customer-wise Sales
plt.bar(customer_sales.index, customer_sales.values)
plt.xlabel("Customer")
plt.ylabel("Sales")
plt.title("Customer-wise Sales")
plt.savefig("screenshots/customer_sales.png")
plt.show()
# Business Insights
print()
print("----- Business Insights -----")
print()
print("1. Best-selling Product:", best_product)
print("2. Highest-sales Region:", best_region)
print("3. Highest-sales Month:", best_month)
print()
print("----- Sales Analysis Part 2 Complete! -----")
print()