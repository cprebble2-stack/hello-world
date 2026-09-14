"""
Visualization module for financial calculator projections.

Generates plots and visual representations of financial growth projections
using matplotlib for better understanding of investment timelines.
"""

import matplotlib.pyplot as plt
from financial_calculator import generate_projection_table


def plot_balance_growth(
    starting_balance: float,
    monthly_contribution: float,
    annual_return_rate: float,
    months: int = 120,
    title: str = "Financial Growth Projection",
    save_path: str = None,
):
    """
    Plots balance growth over time.
    
    Args:
        starting_balance: Initial amount of money
        monthly_contribution: Amount added each month
        annual_return_rate: Expected annual return rate as decimal
        months: Number of months to project (default: 120)
        title: Title for the plot
        save_path: Optional path to save the plot image
    """
    projections = generate_projection_table(
        starting_balance, monthly_contribution, annual_return_rate, months
    )
    
    month_list = [p['month'] for p in projections]
    balance_list = [p['balance'] for p in projections]
    
    plt.figure(figsize=(12, 6))
    plt.plot(month_list, balance_list, linewidth=2, color='#2E86AB', marker='o', markersize=4)
    plt.xlabel('Months', fontsize=12)
    plt.ylabel('Balance ($)', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.tight_layout()
    plt.show()


def plot_contribution_vs_interest(
    starting_balance: float,
    monthly_contribution: float,
    annual_return_rate: float,
    months: int = 120,
    title: str = "Contribution vs Interest Breakdown",
    save_path: str = None,
):
    """
    Plots breakdown of contributions vs interest earned over time.
    
    Args:
        starting_balance: Initial amount of money
        monthly_contribution: Amount added each month
        annual_return_rate: Expected annual return rate as decimal
        months: Number of months to project (default: 120)
        title: Title for the plot
        save_path: Optional path to save the plot image
    """
    projections = generate_projection_table(
        starting_balance, monthly_contribution, annual_return_rate, months
    )
    
    month_list = [p['month'] for p in projections]
    interest_list = [p['interest_earned'] for p in projections]
    contribution_list = [p['contribution'] for p in projections]
    
    plt.figure(figsize=(12, 6))
    
    x = range(len(month_list))
    width = 0.35
    
    plt.bar([i - width/2 for i in x], contribution_list, width, label='Monthly Contribution', color='#A23B72')
    plt.bar([i + width/2 for i in x], interest_list, width, label='Interest Earned', color='#F18F01')
    
    plt.xlabel('Months', fontsize=12)
    plt.ylabel('Amount ($)', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.tight_layout()
    plt.show()


def plot_comparison(
    scenarios: list,
    months: int = 120,
    title: str = "Financial Scenario Comparison",
    save_path: str = None,
):
    """
    Compares multiple financial scenarios on the same plot.
    
    Args:
        scenarios: List of dictionaries with keys:
                  'name', 'starting_balance', 'monthly_contribution', 'annual_return_rate'
        months: Number of months to project (default: 120)
        title: Title for the plot
        save_path: Optional path to save the plot image
    
    Example:
        >>> scenarios = [
        ...     {'name': 'Conservative', 'starting_balance': 2000, 'monthly_contribution': 500, 'annual_return_rate': 0.03},
        ...     {'name': 'Moderate', 'starting_balance': 2000, 'monthly_contribution': 800, 'annual_return_rate': 0.07},
        ...     {'name': 'Aggressive', 'starting_balance': 2000, 'monthly_contribution': 1200, 'annual_return_rate': 0.10},
        ... ]
        >>> plot_comparison(scenarios)
    """
    plt.figure(figsize=(14, 7))
    
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
    
    for idx, scenario in enumerate(scenarios):
        projections = generate_projection_table(
            scenario['starting_balance'],
            scenario['monthly_contribution'],
            scenario['annual_return_rate'],
            months,
        )
        
        month_list = [p['month'] for p in projections]
        balance_list = [p['balance'] for p in projections]
        
        plt.plot(
            month_list,
            balance_list,
            linewidth=2.5,
            marker='o',
            markersize=4,
            label=scenario['name'],
            color=colors[idx % len(colors)],
        )
    
    plt.xlabel('Months', fontsize=12)
    plt.ylabel('Balance ($)', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.tight_layout()
    plt.show()


# Example usage:
if __name__ == "__main__":
    # Plot single scenario
    plot_balance_growth(2000, 800, 0.07, 120, title="$100k Goal Projection")
    
    # Plot contribution vs interest
    plot_contribution_vs_interest(2000, 800, 0.07, 120)
    
    # Compare multiple scenarios
    scenarios = [
        {'name': 'Conservative', 'starting_balance': 2000, 'monthly_contribution': 500, 'annual_return_rate': 0.03},
        {'name': 'Moderate', 'starting_balance': 2000, 'monthly_contribution': 800, 'annual_return_rate': 0.07},
        {'name': 'Aggressive', 'starting_balance': 2000, 'monthly_contribution': 1200, 'annual_return_rate': 0.10},
    ]
    plot_comparison(scenarios, months=120)
