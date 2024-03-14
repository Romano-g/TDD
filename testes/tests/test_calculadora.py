try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../calculadora'
            )
        )
    )
except BaseException:
    raise


from calculadora import my_sum
from unittest import TestCase, main


class TestCalculadora(TestCase):
    def test_sum_five_plus_five_return_ten(self):
        self.assertEqual(my_sum(5, 5), 10)

    def test_sum_minus_five_plus_five_return_zero(self):
        self.assertEqual(my_sum(-5, 5), 0)

    def test_multiple_sums(self):
        x_y_returns = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3),
            (-5, -5, -10),
            (1, 1, 2),
        )

        for x_y_returns in x_y_returns:
            with self.subTest(x_y_returns=x_y_returns):
                x, y, returns = x_y_returns
                self.assertEqual(my_sum(x, y), returns)

    def test_sum_x_are_not_int_or_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            my_sum('11', 10)

    def test_sum_y_are_not_int_or_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            my_sum(11, '10')


if __name__ == '__main__':
    main()
