import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/Sample - Superstore.csv",encoding="cp1252")
print(df.head())
print(df.shape)
print(df.columns)
print("\nDataset Information:",df.info())
print("\nStatistical Summary:",df.describe())
print("\nColumn Datatypes:",df.dtypes)
print("\nChecking missing values:",df.isnull().sum())
print("\nChecking for duplicates:",df.duplicated().sum())
print("\nCheck Dataset shape:",df.shape)
# Convert date columns into datetime format
df["Order Date"]=pd.to_datetime(df["Order Date"])
df["Ship Date"]=pd.to_datetime(df["Ship Date"])
# Extract year and month
df["Year"]=df["Order Date"].dt.year
df["Month"]=df["Order Date"].dt.month
df["Month Name"]=df["Order Date"].dt.month_name()
# Calculate shipping days
df["Shipping Days"]=(df["Ship Date"]-df["Order Date"]).dt.days
print(df[["Order Date","Ship Date","Shipping Days"]].head())
print("\nUpdated Dataset Shape:",df.shape)
# Overall Business Performance
Total_Sales= df["Sales"].sum()
Total_Profit= df["Profit"].sum()
Total_Orders= df["Order ID"].nunique()
Total_Customers= df["Customer ID"].nunique()
Total_Quantity = df["Quantity"].sum()
Average_Discount = df["Discount"].mean()
print("============BUISSINESS OVERVIEW============")
print("Total Sales:",round(Total_Sales,2))
print("Total Profit:",round(Total_Profit,2))
print("Total Orders:",Total_Orders)
print("Total Customers:",Total_Customers)
print("Total Quantity Sold:",Total_Quantity)
print("Average Discount:",round(Average_Discount,2))
# Analyze sales by category
category_sales = df.groupby("Category")["Sales"].sum()
print("\n===== SALES BY CATEGORY =====")
print(category_sales.sort_values(ascending=False))
# Analyze profit by region
region_profit = df.groupby("Region")["Profit"].sum()
print("\n===== PROFIT BY REGION =====")
print(region_profit.sort_values(ascending=False))

# First Seaborn visualization 1: Sales by Category

plt.figure(figsize=(8,5))
sns.barplot(data=df,x="Category",y="Sales",estimator=sum,errorbar=None)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.show()

# Visualization 2 – Monthly Sales Trend
# Monthly Sales Analysis
monthly_sales = (df.groupby("Month")["Sales"].sum().reset_index())
print("monthly sales:",monthly_sales)

monthly_sales['Month Name'] = pd.to_datetime(
    monthly_sales['Month'],
    format='%m'
).dt.month_name()

plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales,x="Month Name",y="Sales",marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png")
plt.show()

# visualization 3: Profit by Region
region_profit = df.groupby("Region")["Profit"].sum().reset_index()
print(region_profit.sort_values(by="Profit", ascending=False))

plt.figure(figsize=(8,5))
sns.barplot(data=region_profit,x="Region",y="Profit",estimator=sum,errorbar=None)
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("charts/profit_by_region.png")
plt.show()

# Visualization 4 – Sales by Product Category and Sub-Category
subcategory_sales = (df.groupby(["Category","Sub-Category"])["Sales"].sum().reset_index())
print(subcategory_sales.sort_values(by="Sales", ascending=False))
plt.figure(figsize=(12,6))
sns.barplot(data=subcategory_sales, x="Sub-Category", y="Sales", hue="Category")
plt.title("Sales by Product Category and Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/sales_by_category_subcategory.png")
plt.show()

# Visualization 5 - Profit vs Discount

plt.figure(figsize=(10,6))
sns.scatterplot(data=df,x="Discount",y="Profit",hue="Category",alpha=0.6)
plt.title("Profit vs Discount")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.axhline(y=0,ls="--")
plt.tight_layout()
plt.savefig("charts/profit_vs_discount.png")
plt.show()