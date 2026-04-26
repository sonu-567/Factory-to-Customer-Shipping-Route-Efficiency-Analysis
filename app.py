
import pandas as pd
import matplotlib.pyplot as plt


data = [
    ["CA-1001", "2024-01-01", "2024-01-05", "Standard", "East", "NY", 200],
    ["CA-1002", "2024-01-02", "2024-01-06", "Express", "Central", "IL", 150],
    ["CA-1003", "2024-01-03", "2024-01-10", "Standard", "West", "CA", 300],
    ["CA-1004", "2024-01-04", "2024-01-08", "Express", "East", "NJ", 180],
    ["CA-1005", "2024-01-05", "2024-01-12", "Standard", "West", "TX", 220],
    ["CA-1006", "2024-01-06", "2024-01-09", "Express", "Central", "TX", 250],
    ["CA-1007", "2024-01-07", "2024-01-15", "Standard", "East", "FL", 270],
]

df = pd.DataFrame(data, columns=[
    "Order ID", "Order Date", "Ship Date", "Ship Mode",
    "Region", "State", "Sales"
])

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days
df = df[df["Lead Time"] >= 0]


region = df.groupby("Region")["Lead Time"].mean()

plt.figure()
plt.bar(region.index, region.values)
plt.title("Average Lead Time by Region")
plt.xlabel("Region")
plt.ylabel("Days")
plt.show()


mode = df.groupby("Ship Mode")["Lead Time"].mean()

plt.figure()
plt.bar(mode.index, mode.values)
plt.title("Lead Time by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Days")
plt.show()


plt.figure()
df.boxplot(column="Lead Time", by="Region")
plt.title("Lead Time Distribution by Region")
plt.suptitle("")
plt.xlabel("Region")
plt.ylabel("Days")
plt.show()


plt.figure()
plt.scatter(df["Sales"], df["Lead Time"])
plt.title("Sales vs Lead Time")
plt.xlabel("Sales")
plt.ylabel("Lead Time")
plt.show()


trend = df.sort_values("Order Date")

plt.figure()
plt.plot(trend["Order Date"], trend["Lead Time"])
plt.title("Lead Time Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Lead Time")
plt.xticks(rotation=45)
plt.show()

# =========================
# 6. Top & Bottom Routes
# =========================
sorted_df = df.sort_values("Lead Time")

top = sorted_df.head(3)
bottom = sorted_df.tail(3)

plt.figure()
plt.bar(top["State"], top["Lead Time"])
plt.title("Top Fastest Routes")
plt.xlabel("State")
plt.ylabel("Days")
plt.show()

plt.figure()
plt.bar(bottom["State"], bottom["Lead Time"])
plt.title("Slowest Routes")
plt.xlabel("State")
plt.ylabel("Days")
plt.show()


df["Delayed"] = df["Lead Time"] > 5

delay_counts = df["Delayed"].value_counts()

plt.figure()
plt.bar(["On Time", "Delayed"], delay_counts.values)
plt.title("Delay Frequency")
plt.ylabel("Count")
plt.show()