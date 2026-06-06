# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Number of stocks user wants to enter
n = int(input("Enter number of different stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("Stock not found in portfolio!")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment Value: $", total_investment)

# Optional: Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio saved successfully in portfolio.txt")