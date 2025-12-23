stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "AMAZON": 155,
    "META": 300
}

total_value = 0
portfolio = {}

print("Available Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found! Please choose from the available list.")
        continue

    quantity = int(input(f"Enter quantity of {stock_name}: "))

    # Store in portfolio
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment
for stock, qty in portfolio.items():
    total_value += stock_prices[stock] * qty

print("\n📊 ----- Your Stock Portfolio -----")
for stock, qty in portfolio.items():
    print(f"{stock} | Quantity: {qty} | Value: ${stock_prices[stock] * qty}")

print("-----------------------------------")
print(f"💰 Total Investment Value: ${total_value}")
print("-----------------------------------")

# Optional: Save to file
save_choice = input("Do you want to save your report to a file? (yes/no): ").lower()

if save_choice == "yes":
    filename = "stock_portfolio.txt"
    with open(filename, "w") as file:
        file.write("Your Stock Portfolio:\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} | Quantity: {qty} | Value: ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")

    print(f"📁 Report saved successfully to '{filename}'!")
