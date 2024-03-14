"""
TDD - Test Driven Development (Desenvolvimento Dirigido a Testes)

Red
1 - Criar o teste e ver falhar (antes de criar o programa)

Green
2 - Criar o código e ver o teste passar

Refactor
3 - Melhorar o código
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../bacon'
            )
        )
    )

except BaseException:
    raise

import unittest
from bacon_with_eggs import bacon_with_eggs


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_with_eggs_must_raise_assertionerror_if_not_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('0')

    def test_bacon_with_eggs_must_return_bacon_with_eggs_if_int_multiple_of_3_and_5(
            self):
        entrys = (15, 30, 45, 60)
        returns = 'Bacon with eggs'

        for entry in entrys:
            with self.subTest(entry=entry, returns=returns):
                self.assertEqual(bacon_with_eggs(entry), returns)

    def test_bacon_with_eggs_return_starve_if_int_not_multiple_of_3_and_5(self):
        entrys = (1, 2, 4, 7, 8)
        returns = 'Starve'

        for entry in entrys:
            with self.subTest(entry=entry, returns=returns):
                self.assertEqual(bacon_with_eggs(entry), returns)

    def test_bacon_with_eggs_return_bacon_if_int_is_multiple_of_3(self):
        entrys = (3, 6, 9, 12, 18, 21, 24, 27)
        returns = 'Bacon'

        for entry in entrys:
            with self.subTest(entry=entry, returns=returns):
                self.assertEqual(bacon_with_eggs(entry), returns)

    def test_bacon_with_eggs_returns_eggs_if_int_is_multiple_of_5(self):
        entrys = (5, 10, 20, 25, 35, 40, 50, 55)
        returns = 'Eggs'

        for entry in entrys:
            with self.subTest(entry=entry, returns=returns):
                self.assertEqual(bacon_with_eggs(entry), returns)


if __name__ == '__main__':
    unittest.main()
