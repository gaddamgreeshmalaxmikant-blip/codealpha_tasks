# Simplified Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 135, "MSFT": 330}

print("Simple Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

portfolio = {}
total_value = 0

# Get user input
while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate and display results
print("\n--- PORTFOLIO SUMMARY ---")
for stock, quantity in portfolio.items():
    value = quantity * stock_prices[stock]
    total_value += value
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTOTAL INVESTMENT: ${total_value}")

# Save to file
with open("simple_portfolio.txt", "w") as f:
    f.write("Stock Portfolio\n")
    f.write("===============\n")
    for stock, quantity in portfolio.items():
        f.write(f"{stock}: {quantity} shares\n")
    f.write(f"Total Value: ${total_value}\n")

print("Results saved to 'simple_portfolio.txt'")