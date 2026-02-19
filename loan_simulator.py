def main():
    loan = get_amount("Loan amount: ")
    rate = get_amount("Annual interest rate (%): ") / 100 / 12
    payment = get_amount("Monthly payment: ")

    months = simulate_loan(loan, rate, payment)

    print(f"Loan paid off in {months} months")


# gets numeric input
def get_amount(text):
    return float(input(text))


# month-by-month payoff loop
def simulate_loan(balance, monthly_rate, payment):
    months = 0

    # prevents infinite loop if payment too small
    if payment <= balance * monthly_rate:
        print("Payment too low — balance will never decrease.")
        return 0

    while balance > 0:
        interest = balance * monthly_rate
        balance = balance + interest - payment
        months += 1

    return months


main()