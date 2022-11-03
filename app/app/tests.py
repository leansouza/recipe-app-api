"""Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Teste the calc module

    Args:
        SimpleTestCase (_type_): _description_
    """

    def test_add_numbers(self):
        """ Test adding numbers together."""

        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Test subtracting numbers together."""

        res = calc.subtract(10,15)

        self.assertEqual(res, 5)