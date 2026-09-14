"""
Test suite for financial_calculator module.

Tests the financial calculation functions with various scenarios including
edge cases, validation, and correctness checks.
"""

import unittest
from financial_calculator import (
    calculate_timeline,
    calculate_balance_at_month,
    generate_projection_table,
)


class TestCalculateTimeline(unittest.TestCase):
    """Test cases for calculate_timeline function."""
    
    def test_basic_calculation(self):
        """Test basic timeline calculation."""
        result = calculate_timeline(2000, 800, 0.07, 100000, verbose=False)
        self.assertIsNotNone(result)
        years, remaining_months, total_months, final_balance = result
        self.assertEqual(years, 9)
        self.assertEqual(remaining_months, 11)
        self.assertEqual(total_months, 119)
        self.assertAlmostEqual(final_balance, 100157.52, places=2)
    
    def test_goal_already_achieved(self):
        """Test when starting balance meets or exceeds target."""
        result = calculate_timeline(150000, 0, 0.07, 100000, verbose=False)
        self.assertIsNone(result)
    
    def test_zero_contribution_zero_growth(self):
        """Test error case with zero contribution and zero growth."""
        result = calculate_timeline(100, 0, 0.0, 1000, verbose=False)
        self.assertIsNone(result)
    
    def test_negative_starting_balance(self):
        """Test validation of negative starting balance."""
        result = calculate_timeline(-1000, 800, 0.07, 100000, verbose=False)
        self.assertIsNone(result)
    
    def test_zero_starting_balance(self):
        """Test calculation with zero starting balance."""
        result = calculate_timeline(0, 100, 0.05, 10000, verbose=False)
        self.assertIsNotNone(result)
        self.assertGreater(result[2], 0)  # Should have positive months
    
    def test_high_return_rate(self):
        """Test with high return rate."""
        result = calculate_timeline(1000, 100, 0.20, 50000, verbose=False)
        self.assertIsNotNone(result)
        # Should reach goal faster with high return
        self.assertLess(result[2], 100)  # Should be less than 100 months
    
    def test_return_values(self):
        """Test that return tuple has correct structure."""
        result = calculate_timeline(5000, 500, 0.08, 50000, verbose=False)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        years, months, total, balance = result
        self.assertIsInstance(years, int)
        self.assertIsInstance(months, int)
        self.assertIsInstance(total, int)
        self.assertIsInstance(balance, float)


class TestCalculateBalanceAtMonth(unittest.TestCase):
    """Test cases for calculate_balance_at_month function."""
    
    def test_balance_at_month_1(self):
        """Test balance calculation after 1 month."""
        balance = calculate_balance_at_month(2000, 800, 0.07, 1)
        # 2000 * (1 + 0.07/12) + 800 = 2000 * 1.005833... + 800
        expected = 2000 * (1 + 0.07/12) + 800
        self.assertAlmostEqual(balance, expected, places=2)
    
    def test_balance_at_month_0(self):
        """Test balance at month 0 (should equal starting balance)."""
        balance = calculate_balance_at_month(2000, 800, 0.07, 0)
        self.assertEqual(balance, 2000)
    
    def test_balance_growth(self):
        """Test that balance grows over time."""
        balance_1 = calculate_balance_at_month(2000, 800, 0.07, 1)
        balance_12 = calculate_balance_at_month(2000, 800, 0.07, 12)
        self.assertGreater(balance_12, balance_1)
    
    def test_zero_contribution(self):
        """Test balance growth with no contributions."""
        balance = calculate_balance_at_month(1000, 0, 0.07, 12)
        # Should only grow via interest
        self.assertGreater(balance, 1000)
        self.assertLess(balance, 1100)  # But not by much


class TestGenerateProjectionTable(unittest.TestCase):
    """Test cases for generate_projection_table function."""
    
    def test_table_length(self):
        """Test that projection table has correct length."""
        projections = generate_projection_table(2000, 800, 0.07, 12)
        self.assertEqual(len(projections), 12)
    
    def test_table_structure(self):
        """Test that each row has required fields."""
        projections = generate_projection_table(2000, 800, 0.07, 3)
        required_fields = {'month', 'year', 'balance', 'interest_earned', 'contribution'}
        for proj in projections:
            self.assertTrue(required_fields.issubset(proj.keys()))
    
    def test_month_progression(self):
        """Test that months are sequential."""
        projections = generate_projection_table(2000, 800, 0.07, 5)
        for i, proj in enumerate(projections, 1):
            self.assertEqual(proj['month'], i)
    
    def test_year_calculation(self):
        """Test that year is calculated correctly."""
        projections = generate_projection_table(2000, 800, 0.07, 24)
        # Months 1-12 should be year 1
        for proj in projections[:12]:
            self.assertEqual(proj['year'], 1)
        # Months 13-24 should be year 2
        for proj in projections[12:]:
            self.assertEqual(proj['year'], 2)
    
    def test_balance_increases(self):
        """Test that balance consistently increases."""
        projections = generate_projection_table(2000, 800, 0.07, 12)
        for i in range(1, len(projections)):
            self.assertGreater(projections[i]['balance'], projections[i-1]['balance'])
    
    def test_contribution_consistency(self):
        """Test that contribution is consistent across all rows."""
        contribution = 500
        projections = generate_projection_table(2000, contribution, 0.07, 10)
        for proj in projections:
            self.assertEqual(proj['contribution'], contribution)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def test_very_large_monthly_contribution(self):
        """Test with very large monthly contribution."""
        result = calculate_timeline(0, 50000, 0.01, 100000, verbose=False)
        self.assertIsNotNone(result)
        self.assertLess(result[2], 5)  # Should reach goal in less than 5 months
    
    def test_very_small_target(self):
        """Test with very small target already exceeded."""
        result = calculate_timeline(1000, 0, 0.07, 100, verbose=False)
        self.assertIsNone(result)
    
    def test_precision(self):
        """Test that calculations maintain precision."""
        balance = calculate_balance_at_month(0.01, 0.01, 0.07, 100)
        self.assertIsInstance(balance, float)
        self.assertGreaterEqual(balance, 0)


if __name__ == '__main__':
    unittest.main()
