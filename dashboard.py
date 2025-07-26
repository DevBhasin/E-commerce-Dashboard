import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("orders.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Filter Delivered Orders
delivered = df[df['Status'] == 'Delivered']

# Daily Revenue Trend
daily_revenue = delivered.groupby('Date')['Revenue'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_revenue, x='Date', y='Revenue', marker='o')
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("daily_revenue.png")
plt.show()
# Repeat Customer Rate
repeat_buyers = delivered.groupby('User_ID').size().reset_index(name='purchase_count')
repeat_customers = repeat_buyers[repeat_buyers['purchase_count'] > 1]

repeat_rate = len(repeat_customers) / len(repeat_buyers)
print(f"Repeat Customer Rate: {repeat_rate:.2%}")

# Conversion Funnel
funnel = df['Status'].value_counts()
print("\nConversion Funnel:\n", funnel)
