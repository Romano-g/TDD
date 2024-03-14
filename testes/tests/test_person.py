try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../pessoa'
            )
        )
    )
except BaseException:
    raise


import unittest

from person import Person
from unittest.mock import patch


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Person('Caio', 'Romano')
        self.p2 = Person('Tutu', 'Galeffi')
        return super().setUp()

    def test_person_attr_name_value(self):
        self.assertEqual(self.p1.name, 'Caio')
        self.assertEqual(self.p2.name, 'Tutu')

    def test_person_attr_name_value_is_str(self):
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p2.name, str)

    def test_person_attr_surname_value(self):
        self.assertEqual(self.p1.surname, 'Romano')
        self.assertEqual(self.p2.surname, 'Galeffi')

    def test_person_attr_surname_value_is_str(self):
        self.assertIsInstance(self.p1.surname, str)
        self.assertIsInstance(self.p2.surname, str)

    def test_person_attr_data_obtained_starts_false(self):
        self.assertFalse(self.p1.obtained_data)
        self.assertFalse(self.p2.obtained_data)

    def test_get_all_data_succes_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'OK')
            self.assertTrue(self.p1.obtained_data)

            self.assertEqual(self.p2.get_all_data(), 'OK')
            self.assertTrue(self.p2.obtained_data)

    def test_get_all_data_failure_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERRO 404')
            self.assertFalse(self.p1.obtained_data)

            self.assertEqual(self.p2.get_all_data(), 'ERRO 404')
            self.assertFalse(self.p2.obtained_data)

    def test_get_all_data_success_and_failure_sequential(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'OK')
            self.assertTrue(self.p1.obtained_data)

            self.assertEqual(self.p2.get_all_data(), 'OK')
            self.assertTrue(self.p2.obtained_data)
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERRO 404')
            self.assertFalse(self.p1.obtained_data)

            self.assertEqual(self.p2.get_all_data(), 'ERRO 404')
            self.assertFalse(self.p2.obtained_data)


if __name__ == '__main__':
    unittest.main()
