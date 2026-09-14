# Financial Calculator Documentation

## Overview
The Financial Calculator is a comprehensive Python module designed to help with financial planning, investment analysis, and loan calculations. It provides multiple functions for different financial scenarios.

## Installation
Simply import the module:
```python
from financial_calculator import (
    calculate_timeline,
    calculate_compound_interest,
    calculate_loan_payment,
    calculate_retirement_fund,
    calculate_roi,
)
```

## Functions

### 1. `calculate_timeline()`
Calculates how long it takes to reach a financial goal.

**Parameters:**
- `starting_balance` (float): Initial amount in account
- `monthly_contribution` (float): Regular monthly contribution
- `annual_return_rate` (float): Expected annual return (0.07 = 7%)
- `target` (float): Goal amount (default: $100,000)

**Example:**
```python
calculate_timeline(
    starting_balance=2000.0,
    monthly_contribution=800.0,
    annual_return_rate=0.07,
    target=100000.0,
)
```

**Output:**
```
--- $100,000.00 Milestone Projection ---
Starting Balance: $2,000.00
Monthly Contribution: $800.00
Assumed Annual Return: 7.00%

Timeline to Goal: 11 years and 10 months (142 total months).
Final Projected Balance: $101,447.90
```

---

### 2. `calculate_compound_interest()`
Calculates the final amount with compound interest using the formula: A = P(1 + r/n)^(nt)

**Parameters:**
- `principal` (float): Initial investment amount
- `annual_rate` (float): Annual interest rate (0.05 = 5%)
- `years` (float): Time period in years
- `compounding_periods` (int): Compounding frequency per year (default: 12 for monthly)

**Example:**
```python
result = calculate_compound_interest(
    principal=5000.0,
    annual_rate=0.05,
    years=10,
    compounding_periods=12,
)
```

**Returns:**
```python
{
    "principal": 5000.0,
    "interest_earned": 1633.58,
    "final_amount": 6633.58,
}
```

---

### 3. `calculate_loan_payment()`
Calculates monthly loan payment using amortization formula.

**Parameters:**
- `principal` (float): Loan amount
- `annual_rate` (float): Annual interest rate (0.045 = 4.5%)
- `years` (int): Loan term in years

**Example:**
```python
result = calculate_loan_payment(
    principal=200000.0,
    annual_rate=0.045,
    years=30,
)
```

**Returns:**
```python
{
    "monthly_payment": 1013.37,
    "total_paid": 364814.40,
    "total_interest": 164814.40,
}
```

---

### 4. `calculate_retirement_fund()`
Projects retirement savings and determines if you're on track.

**Parameters:**
- `current_age` (int): Your current age
- `retirement_age` (int): Planned retirement age
- `current_savings` (float): Current retirement savings
- `monthly_contribution` (float): Monthly retirement contribution
- `annual_return_rate` (float): Expected annual return rate
- `annual_expenses` (float): Expected annual retirement expenses
- `life_expectancy` (int): Expected life expectancy (default: 95)

**Example:**
```python
result = calculate_retirement_fund(
    current_age=30,
    retirement_age=65,
    current_savings=50000.0,
    monthly_contribution=1000.0,
    annual_return_rate=0.07,
    annual_expenses=60000.0,
)
```

**Returns:**
```python
{
    "retirement_balance": 1875432.18,
    "total_needed": 1800000.0,
    "surplus_or_shortfall": 75432.18,
}
```

---

### 5. `calculate_roi()`
Calculates Return on Investment (ROI) percentage.

**Parameters:**
- `initial_investment` (float): Initial investment amount
- `final_value` (float): Current or final value
- `years` (float): Time period (optional, for annualized ROI)

**Example:**
```python
result = calculate_roi(
    initial_investment=10000.0,
    final_value=15000.0,
    years=3,
)
```

**Returns:**
```python
{
    "total_roi_percentage": 50.0,
    "annualized_roi_percentage": 14.47,
    "profit": 5000.0,
}
```

---

## Error Handling

All functions include validation to prevent invalid inputs:
- Negative or zero amounts where required
- Invalid time periods
- Age inconsistencies

Example error handling:
```python
result = calculate_compound_interest(
    principal=-1000,  # Invalid
    annual_rate=0.05,
    years=10,
)
# Output: Error: Principal, rate, and years must be non-negative.
```

---

## Usage Tips

1. **Rate Format:** Always provide rates as decimals (0.07 for 7%, not 7)
2. **Currency:** All amounts are in dollars ($)
3. **Time Periods:** Times should be in years unless specified otherwise
4. **Return Values:** Most functions return dictionaries for programmatic use
5. **Print Output:** Functions print formatted results to console

---

## Common Scenarios

### Scenario 1: Save for a Car ($30,000 in 3 years)
```python
calculate_timeline(
    starting_balance=5000.0,
    monthly_contribution=700.0,
    annual_return_rate=0.03,
    target=30000.0,
)
```

### Scenario 2: Mortgage Analysis
```python
calculate_loan_payment(
    principal=350000.0,
    annual_rate=0.06,
    years=30,
)
```

### Scenario 3: College Savings Fund
```python
calculate_retirement_fund(
    current_age=5,
    retirement_age=18,
    current_savings=10000.0,
    monthly_contribution=500.0,
    annual_return_rate=0.06,
    annual_expenses=25000.0,
    life_expectancy=18,
)
```

---

## License
Free to use for personal and educational purposes.
