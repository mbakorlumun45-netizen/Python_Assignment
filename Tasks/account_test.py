#import unittest

from unittest import TestCase

from account_functions import check_balance

class AccountTest(unittest.TestCase):

    def test_accountBalance_isZero_duringCreation(self):

        balance = 0

        expected_balance = 0

        actual_balance = check_balance
        
        self.assertEqual(actual_balance, expected_balance)i
    
    def test_thatAccount_canBeDepositedInto_afterCreation(self):

    amount = 500.0

    self.assertEqual(0, check_balance())

    deposit(amount)

    self.assertEqual(500.0, check_balance)
