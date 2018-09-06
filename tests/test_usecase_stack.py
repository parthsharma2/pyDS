from pyDS.usecase.stack import bracketBalanced, decimalBaseConvert
import unittest


class TestUsecaseBracketBalanced(unittest.TestCase):

    def test_empty_expression(self):
        self.assertTrue(bracketBalanced(""))

    def test_balanced_expression(self):
        self.assertTrue(bracketBalanced("({[]})"))

    def test_unbalanced_expression(self):
        self.assertFalse(bracketBalanced("(([)))"))

    def test_real_life_balanced_expression(self):
        self.assertTrue(bracketBalanced("a + ( b * c )"))

    def test_real_life_unbalanced_expression(self):
        self.assertFalse(bracketBalanced("a + ( b * c"))


class TestUsecaseDecimalBaseConvert(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimalBaseConvert(12,2), "1100")

    def test_decimal_to_octal(self):
        self.assertEqual(decimalBaseConvert(21, 8), "25")

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(decimalBaseConvert(15, 16), "F")

    def test_base_higher_than_16(self):
        with self.assertRaises(ValueError):
            decimalBaseConvert(45, 17)

    def test_base_lower_than_2(self):
        with self.assertRaises(ValueError):
            decimalBaseConvert(165, -2)

    def test_number_zero(self):
        self.assertEqual(decimalBaseConvert(0, 8), "0")
