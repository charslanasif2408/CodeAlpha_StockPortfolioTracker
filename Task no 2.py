#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 330,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("📈 Welcome to the Stock Portfolio Tracker!\n")
print("Available stocks:", ', '.join(stock_prices.keys()))

# Input loop
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("❌ Invalid stock symbol. Please choose from:", ', '.join(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock} shares: "))
        if quantity < 0:
            raise ValueError
    except ValueError:
        print("❌ Please enter a valid positive integer for quantity.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save this report? (yes/no): ").lower()
if save == 'yes':
    filename = "portfolio_report.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("=======================\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(f"✅ Report saved to '{filename}'")


# In[ ]:




