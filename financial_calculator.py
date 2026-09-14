def calculate_timeline(
    starting_balance: float,
    monthly_contribution: float,
    annual_return_rate: float,
    target: float = 100000.0,
):
    """Calculates months and years required to reach a target financial goal."""
    if starting_balance >= target:
        print(f"Goal already achieved! Starting balance of ${starting_balance:,.2f} meets or exceeds target of ${target:,.2f}.")
        return

    monthly_rate = annual_return_rate / 12

    # Prevent infinite loop if balance has zero or negative growth
    if monthly_contribution <= 0 and (starting_balance <= 0 or monthly_rate <= 0):
        print("Error: Target cannot be reached with zero growth and zero/negative monthly contributions.")
        return

    balance = starting_balance
    months = 0

    print(f"--- ${target:,.2f} Milestone Projection ---")
    print(f"Starting Balance: ${starting_balance:,.2f}")
    print(f"Monthly Contribution: ${monthly_contribution:,.2f}")
    print(f"Assumed Annual Return: {annual_return_rate * 100:.2f}%\n")

    while balance < target:
        interest_earned = balance * monthly_rate
        balance += interest_earned + monthly_contribution
        months += 1

    years = months // 12
    remaining_months = months % 12

    print(f"Timeline to Goal: {years} years and {remaining_months} months ({months} total months).")
    print(f"Final Projected Balance: ${balance:,.2f}\n")


# Example usage:
if __name__ == "__main__":
    calculate_timeline(
        starting_balance=2000.0,
        monthly_contribution=800.0,
        annual_return_rate=0.07,
        target=100000.0,
    )
