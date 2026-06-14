# CodeAlpha Internship: Task 2 - Stock Portfolio Tracker

def display_menu():
    print("\n" + "="*35)
    print("   STOCK PORTFOLIO TRACKER MENU   ")
    print("="*35)
    print("1. View Available Stocks & Prices")
    print("2. Calculate Total Investment")
    print("3. Exit Program")
    print("="*35)

def main():
    # Predefined stock prices as required by the assignment
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOG": 150.0,
        "MSFT": 420.0,
        "AMZN": 175.0
    }
    
    # Dictionary to keep track of what the user buys
    user_portfolio = {}
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\n--- Available Stocks ---")
            for stock, price in stock_prices.items():
                print(f"{stock}: ${price}")
                
        elif choice == "2":
            print("\n--- Calculate Investment ---")
            # Loop to allow adding multiple stocks to the portfolio
            while True:
                stock_name = input("Enter stock symbol (or type 'done' to calculate): ").upper().strip()
                
                if stock_name == "DONE":
                    break
                
                if stock_name in stock_prices:
                    try:
                        quantity = int(input(f"Enter quantity for {stock_name}: "))
                        if quantity <= 0:
                            print("Quantity must be greater than 0.")
                            continue
                        
                        # Add or update the quantity in the user's portfolio
                        if stock_name in user_portfolio:
                            user_portfolio[stock_name] += quantity
                        else:
                            user_portfolio[stock_name] = quantity
                        print(f"Added {quantity} shares of {stock_name} to your session.")
                    except ValueError:
                        print("Invalid input! Please enter a whole number for quantity.")
                else:
                    print("Error: Stock symbol not found in our system. Please try again.")
            
            # Calculate total investment value if portfolio is not empty
            if user_portfolio:
                print("\n" + "*"*40)
                print("         YOUR INVESTMENT REPORT         ")
                print("*"*40)
                
                total_portfolio_value = 0.0
                report_lines = [] # To save into the text file later
                
                for stock, qty in user_portfolio.items():
                    price = stock_prices[stock]
                    cost = qty * price
                    total_portfolio_value += cost
                    line = f"{stock}: {qty} shares x ${price} = ${cost:.2f}"
                    print(line)
                    report_lines.append(line)
                
                print("-"*40)
                total_summary = f"Total Portfolio Value: ${total_portfolio_value:.2f}"
                print(total_summary)
                print("*"*40)
                
                # File Handling: Save the result into a .txt file
                save_choice = input("\nWould you like to save this report to a file? (yes/no): ").lower().strip()
                if save_choice == 'yes' or save_choice == 'y':
                    with open("portfolio_report.txt", "w") as file:
                        file.write("=== CODEALPHA STOCK PORTFOLIO REPORT ===\n\n")
                        for line in report_lines:
                            file.write(line + "\n")
                        file.write("-" * 40 + "\n")
                        file.write(total_summary + "\n")
                    print("Report successfully saved to 'portfolio_report.txt'!")
            else:
                print("\nYour portfolio is empty. No investment to calculate.")
                
        elif choice == "3":
            print("\nThank you for using Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option from the menu.")

if __name__ == "__main__":
    main()