# import random loads Python’s random number generator library
import random

def main():
    portfolio = get_portfolio()

    total = calculate_total_value(portfolio)
    print(f"Total Portfolio Value: ${total:.2f}")

    simulate_week(portfolio)


# sample portfolio dictionary (nested dictionary)
def get_portfolio():
    return {
        "AAPL": {"shares": 10, "price": 170},
        "TSLA": {"shares": 4, "price": 250},
        "AMZN": {"shares": 2, "price": 130}
    }


# loops through stocks and adds up shares * price
def calculate_total_value(portfolio):
    total = 0

    for symbol in portfolio:
        shares = portfolio[symbol]["shares"]
        price = portfolio[symbol]["price"]
        total = total + (shares * price)

    return total


# bonus: update prices for 5 days and print total each day
def simulate_week(portfolio):
    print("\nWeekly Simulation (±5% daily price change)")

    for day in range(1, 6):

        for symbol in portfolio:
            change = random.uniform(-0.05, 0.05)
            portfolio[symbol]["price"] = portfolio[symbol]["price"] * (1 + change)

        total = calculate_total_value(portfolio)
        print(f"Day {day} Total: ${total:.2f}")


main()