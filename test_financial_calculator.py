"""
Unit tests for financial_calculator.py

Tests all functions with various scenarios and edge cases.
"""

import unittest
from financial_calculator import (
    calculate_timeline,
    calculate_compound_interest,
    calculate_loan_payment,
    calculate_retirement_fund,
    calculate_roi,
)


class TestCalculateTimeline(unittest.TestCase):
    """Test cases for calculate_timeline function"""

    def test_goal_already_achieved(self):
        """Test when starting balance already meets goal"""
        result = calculate_timeline(
            starting_balance=150000.0,
            monthly_contribution=0,
            annual_return_rate=0.05,
            target=100000.0,
        )
        self.assertIsNone(result)

    def test_basic_timeline(self):
        """Test basic timeline calculation"""
        # Should not raise an error
        calculate_timeline(
            starting_balance=2000.0,
            monthly_contribution=800.0,
            annual_return_rate=0.07,
            target=50000.0,
        )

    def test_zero_contribution_with_growth(self):
        """Test timeline with no contributions but investment returns"""
        calculate_timeline(
            starting_balance=10000.0,
            monthly_contribution=0,
            annual_return_rate=0.10,
            target=50000.0,
        )


class TestCompoundInterest(unittest.TestCase):
    """Test cases for calculate_compound_interest function"""

    def test_basic_compound_interest(self):
        """Test basic compound interest calculation"""
        result = calculate_compound_interest(
            principal=1000.0,
            annual_rate=0.05,
            years=1,
            compounding_periods=1,
        )
        self.assertAlmostEqual(result["final_amount"], 1050.0, places=2)
        self.assertAlmostEqual(result["interest_earned"], 50.0, places=2)

    def test_monthly_compounding(self):
        """Test monthly compounding"""
        result = calculate_compound_interest(
            principal=1000.0,
            annual_rate=0.12,
            years=1,
            compounding_periods=12,
        )
        # Should be slightly more than simple interest due to compounding
        self.assertGreater(result["final_amount"], 1120.0)

    def test_zero_rate(self):
        """Test with 0% interest rate"""
        result = calculate_compound_interest(
            principal=5000.0,
            annual_rate=0.0,
            years=5,
        )
        self.assertEqual(result["final_amount"], 5000.0)
        self.assertEqual(result["interest_earned"], 0.0)

    def test_negative_principal(self):
        """Test with negative principal (should fail)"""
        result = calculate_compound_interest(
            principal=-1000.0,
            annual_rate=0.05,
            years=5,
        )
        self.assertIsNone(result)


class TestLoanPayment(unittest.TestCase):
    """Test cases for calculate_loan_payment function"""

    def test_basic_loan(self):
        """Test basic loan payment calculation"""
        result = calculate_loan_payment(
            principal=100000.0,
            annual_rate=0.05,
            years=5,
        )
        self.assertIsNotNone(result)
        self.assertGreater(result["monthly_payment"], 0)
        self.assertGreater(result["total_interest"], 0)

    def test_zero_interest_loan(self):
        """Test loan with 0% interest"""
        result = calculate_loan_payment(
            principal=12000.0,
            annual_rate=0.0,
            years=1,
        )
        self.assertAlmostEqual(result["monthly_payment"], 1000.0, places=2)
        self.assertEqual(result["total_interest"], 0.0)

    def test_30_year_mortgage(self):
        """Test standard 30-year mortgage"""
        result = calculate_loan_payment(
            principal=300000.0,
            annual_rate=0.04,
            years=30,
        )
        self.assertGreater(result["monthly_payment"], 0)
        self.assertGreater(result["total_paid"], result["principal"])

    def test_invalid_loan(self):
        """Test with invalid inputs"""
        result = calculate_loan_payment(
            principal=-100000.0,
            annual_rate=0.05,
            years=5,
        )
        self.assertIsNone(result)


class TestRetirementFund(unittest.TestCase):
    """Test cases for calculate_retirement_fund function"""

    def test_basic_retirement(self):
        """Test basic retirement calculation"""
        result = calculate_retirement_fund(
            current_age=30,
            retirement_age=65,
            current_savings=50000.0,
            monthly_contribution=1000.0,
            annual_return_rate=0.07,
            annual_expenses=60000.0,
        )
        self.assertIsNotNone(result)
        self.assertGreater(result["retirement_balance"], 0)

    def test_retirement_age_error(self):
        """Test when current age >= retirement age"""
        result = calculate_retirement_fund(
            current_age=70,
            retirement_age=65,
            current_savings=100000.0,
            monthly_contribution=0,
            annual_return_rate=0.05,
            annual_expenses=50000.0,
        )
        self.assertIsNone(result)

    def test_early_retirement(self):
        """Test early retirement scenario"""
        result = calculate_retirement_fund(
            current_age=40,
            retirement_age=50,
            current_savings=300000.0,
            monthly_contribution=2000.0,
            annual_return_rate=0.08,
            annual_expenses=80000.0,
            life_expectancy=85,
        )
        self.assertIsNotNone(result)


class TestROI(unittest.TestCase):
    """Test cases for calculate_roi function"""

    def test_positive_roi(self):
        """Test positive return on investment"""
        result = calculate_roi(
            initial_investment=10000.0,
            final_value=15000.0,
            years=1,
        )
        self.assertAlmostEqual(result["total_roi_percentage"], 50.0, places=2)
        self.assertEqual(result["profit"], 5000.0)

    def test_negative_roi(self):
        """Test negative return on investment"""
        result = calculate_roi(
            initial_investment=10000.0,
            final_value=8000.0,
            years=1,
        )
        self.assertAlmostEqual(result["total_roi_percentage"], -20.0, places=2)
        self.assertEqual(result["profit"], -2000.0)

    def test_break_even(self):
        """Test break-even scenario"""
        result = calculate_roi(
            initial_investment=10000.0,
            final_value=10000.0,
            years=1,
        )
        self.assertEqual(result["total_roi_percentage"], 0.0)
        self.assertEqual(result["profit"], 0.0)

    def test_annualized_roi(self):
        """Test annualized ROI calculation"""
        result = calculate_roi(
            initial_investment=10000.0,
            final_value=20000.0,
            years=2,
        )
        # 100% total return over 2 years = ~41.42% annualized
        self.assertGreater(result["annualized_roi_percentage"], 0)
        self.assertLess(result["annualized_roi_percentage"], 50.0)


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple functions"""

    def test_full_financial_plan(self):
        """Test a complete financial planning scenario"""
        # Calculate savings goal
        calculate_timeline(
            starting_balance=5000.0,
            monthly_contribution=500.0,
            annual_return_rate=0.06,
            target=50000.0,
        )

        # Calculate compound interest on savings
        savings = calculate_compound_interest(
            principal=50000.0,
            annual_rate=0.05,
            years=10,
        )
        self.assertIsNotNone(savings)

        # Calculate retirement needs
        retirement = calculate_retirement_fund(
            current_age=35,
            retirement_age=65,
            current_savings=50000.0,
            monthly_contribution=1500.0,
            annual_return_rate=0.07,
            annual_expenses=75000.0,
        )
        self.assertIsNotNone(retirement)


if __name__ == "__main__":
    unittest.main()
