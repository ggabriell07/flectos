import unittest

from examples.router import extract_brl_amount, route_message


class RouterTests(unittest.TestCase):
    def test_purchase_decision(self):
        result = route_message("Será que devo comprar um tênis de R$ 300?")
        self.assertEqual(result.flow, "purchase_decision")

    def test_expense(self):
        result = route_message("Paguei R$ 45 no almoço")
        self.assertEqual(result.flow, "expense_registration")

    def test_income(self):
        result = route_message("Recebi R$ 4500 de salário")
        self.assertEqual(result.flow, "income_registration")

    def test_state_precedence(self):
        result = route_message("preciso", {"current_flow": "purchase_decision"})
        self.assertEqual(result.source, "conversation_state")

    def test_brl_parsing(self):
        self.assertEqual(extract_brl_amount("R$ 1.200,50"), 1200.50)


if __name__ == "__main__":
    unittest.main()
