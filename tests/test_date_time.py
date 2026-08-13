import unittest
import sys
from datetime import date
sys.path.insert(0, '..')

from brliant_calc import date_time


class TestDateAndTimeOperations(unittest.TestCase):

    def test_add_days(self):
        self.assertEqual(str(date_time.add_days("2024-01-15", "30")), "2024-02-14")
        self.assertEqual(str(date_time.add_days("2024-01-01", "0")), "2024-01-01")
        self.assertEqual(str(date_time.add_days("2024-03-01", "-1")), "2024-02-29")

    def test_add_months(self):
        self.assertEqual(str(date_time.add_months("2024-01-15", "1")), "2024-02-15")
        self.assertEqual(str(date_time.add_months("2024-01-31", "1")), "2024-02-29")
        self.assertEqual(str(date_time.add_months("2024-01-31", "13")), "2025-02-28")
        self.assertEqual(str(date_time.add_months("2024-03-31", "-1")), "2024-02-29")

    def test_diff_days(self):
        self.assertEqual(date_time.diff_days("2024-01-01", "2024-12-31"), 365)
        self.assertEqual(date_time.diff_days("2024-01-01", "2024-01-01"), 0)
        self.assertEqual(date_time.diff_days("2024-12-31", "2024-01-01"), -365)

    def test_day_of_week(self):
        self.assertEqual(date_time.day_of_week("2024-07-04"), "Thursday")
        self.assertEqual(date_time.day_of_week("2024-01-01"), "Monday")

    def test_age(self):
        today = date.today()
        expected = today.year - 2000
        if (today.month, today.day) < (1, 1):
            expected -= 1
        self.assertEqual(date_time.age("2000-01-01"), expected)
        self.assertGreaterEqual(date_time.age("2024-01-01"), 0)

    def test_julian_day(self):
        self.assertEqual(date_time.julian_day("2000-01-01"), 2451545)
        self.assertEqual(date_time.julian_day("1970-01-01"), 2440588)
        self.assertEqual(date_time.julian_day("2024-01-01"), 2460311)

    def test_is_leap_year(self):
        self.assertTrue(date_time.is_leap_year("2024"))
        self.assertTrue(date_time.is_leap_year("2000"))
        self.assertFalse(date_time.is_leap_year("2023"))
        self.assertFalse(date_time.is_leap_year("1900"))

    def test_week_number(self):
        self.assertEqual(date_time.week_number("2024-01-01"), 1)
        self.assertEqual(date_time.week_number("2024-12-31"), 1)

    def test_date_format_variants(self):
        self.assertEqual(str(date_time.add_days("2024/01/15", "1")), "2024-01-16")
        self.assertEqual(str(date_time.add_days("15-01-2024", "1")), "2024-01-16")
        self.assertEqual(str(date_time.add_days("15/01/2024", "1")), "2024-01-16")
        self.assertEqual(str(date_time.add_days("01/15/2024", "1")), "2024-01-16")

    def test_invalid_date_raises(self):
        with self.assertRaises(ValueError):
            date_time.add_days("not-a-date", "1")
        with self.assertRaises(ValueError):
            date_time.julian_day("2024-13-45")

    def test_invalid_number_raises(self):
        with self.assertRaises(ValueError):
            date_time.add_days("2024-01-01", "abc")


if __name__ == '__main__':
    unittest.main()
