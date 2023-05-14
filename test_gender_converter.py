from unittest import TestCase

from gender_converter import convert_gender


class convert_gender_Test(TestCase):
    def test_convert_gender_when_male(self):
        actual = convert_gender("M")
        expected = "Male"
        self.assertEqual(actual, expected)

    def test_convert_gender_when_female(self):
        actual = convert_gender("F")
        expected = "Female"
        self.assertEqual(actual, expected)

    def test_convert_gender_when_unknown_gender(self):
        actual = convert_gender("hello")
        expected = "Unknown_gender"
        self.assertEqual(actual, expected)


