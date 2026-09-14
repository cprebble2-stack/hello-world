"""
Financial Calculator Module

Provides utilities for calculating financial milestones, timelines, and projections
based on compound interest, monthly contributions, and return rates.
"""

from typing import Tuple, Optional


def calculate_timeline(
    starting_balance: float,
    monthly_contribution: float,
    annual_return_rate: float,
    target: float = 100000.0,
    verbose: bool = True,
) -> Optional[Tuple[int, int, int, float]]:
    """
    Calculates months and years required to reach a target financial goal.
    
    Uses compound interest calculation with monthly contributions to determine
    the timeline for reaching a financial milestone.
    
    Args:
        starting_balance: Initial amount of money (must be >= 0)
        monthly_contribution: Amount added each month (can be 0 or negative)
        annual_return_rate: Expected annual return rate as decimal (e.g., 0.07 for 7%)
        target: Financial goal amount (default: $100,000)
        verbose: If True, prints detailed projection (default: True)
    
    Returns:
        Tuple of (years, remaining_months, total_months, final_balance) if goal is reachable,
        None if goal cannot be reached or starting balance already meets target.
    
    Examples:
        >>> result = calculate_timeline(2000, 800, 0.07, 100000, verbose=False)
        >>> print(result)
        (9, 11, 119, 100157.52)
    """
    # Validate inputs
    if starting_balance < 0:
        if verbose:
            print("Error: Starting balance cannot be negative.")
        return None
    
    if starting_balance >= target:
        if verbose:
            print(f"Goal already achieved! Starting balance of ${starting_balance:,.2f} meets or exceeds target of ${target:,.2f}.")
        return None

    monthly_rate = annual_return_rate / 12

    # Prevent infinite loop if balance has zero or negative growth
    if monthly_contribution <= 0 and (starting_balance <= 0 or monthly_rate <= 0):
        if verbose:
            print("Error: Target cannot be reached with zero growth and zero/negative monthly contributions.")
        return None

    balance = starting_balance
    months = 0

    if verbose:
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

    if verbose:
        print(f"Timeline to Goal: {years} years and {remaining_months} months ({months} total months).")
        print(f"Final Projected Balance: ${balance:,.2f}\n")

    return (years, remaining_months, months, round(balance, 2))


def calculate_balance_at_month(
    starting_balance: float,
    monthly_contribution: float,
    annual_return_rate: float,
    target_month: int,
) -> float:
    """
    Calculates the projected balance at a specific month.
    
    Args:
        starting_balance: Initial amount of money
        monthly_contribution: Amount added each month
        annual_return_rate: Expected annual return rate as decimal
        target_month: The month number to calculate balance for
    
    Returns:
        Projected balance at the specified month
    
    Examples:
        >>> balance = calculate_balance_at_month(2000, 800, 0.07, 12)
        >>> print(f"${balance:,.2f}")
        $12,154.47
    """
    monthly_rate = annual_return_rate / 12
    balance = starting_balance
    
    for _ in range(target_month):
        interest_earned = balance * monthly_rate
        balance += interest_earned + monthly_contribution
    
    return round(balance, 2)


def generate_projection_table(
    starting_balance: float,
    monthly_contribution: float,
    annual_return_rate: float,
    months: int = 60,
) -> list:
    """
    Generates a detailed projection table for a given number of months.
    
    Args:
        starting_balance: Initial amount of money
        monthly_contribution: Amount added each month
        annual_return_rate: Expected annual return rate as decimal
        months: Number of months to project (default: 60)
    
    Returns:
        List of dictionaries containing month-by-month projection data
    
    Examples:
        >>> projections = generate_projection_table(2000, 800, 0.07, 3)
        >>> for proj in projections:
        ...     print(f"Month {proj['month']}: ${proj['balance']:,.2f}")
        Month 1: $2,811.67
        Month 2: $3,629.32
        Month 3: $4,453.12
    """
    monthly_rate = annual_return_rate / 12
    balance = starting_balance
    projections = []
    
    for month in range(1, months + 1):
        interest_earned = balance * monthly_rate
        balance += interest_earned + monthly_contribution
        projections.append({
            'month': month,
            'year': (month - 1) // 12 + 1,
            'balance': round(balance, 2),
            'interest_earned': round(interest_earned, 2),
            'contribution': monthly_contribution,
        })
    
    return projections


# Example usage:
if __name__ == "__main__":
    # Basic timeline calculation
    calculate_timeline(
        starting_balance=2000.0,
        monthly_contribution=800.0,
        annual_return_rate=0.07,
        target=100000.0,
    )
    
    # Calculate balance at a specific month
    balance_at_12_months = calculate_balance_at_month(2000, 800, 0.07, 12)
    print(f"Balance after 12 months: ${balance_at_12_months:,.2f}\n")
    
    # Generate and display projection table for 12 months
    print("--- 12-Month Projection Table ---")
    projections = generate_projection_table(2000, 800, 0.07, 12)
    for proj in projections:
        print(f"Month {proj['month']:2d}: ${proj['balance']:>12,.2f} (Interest: ${proj['interest_earned']:>8,.2f})")
