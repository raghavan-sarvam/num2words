# -*- coding: utf-8 -*-

from unittest import TestCase

from num2words import num2words


class TestPA(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(100, lang="pa"), "ਇੱਕ ਸੌ")
        self.assertEqual(num2words(101, lang="pa"), "ਇੱਕ ਸੌ ਇੱਕ")
        self.assertEqual(num2words(1000, lang="pa"), "ਇੱਕ ਹਜ਼ਾਰ")
        self.assertEqual(num2words(12000, lang="pa"), "ਬਾਰਾਂ ਹਜ਼ਾਰ")
        self.assertEqual(num2words(100000, lang="pa"), "ਇੱਕ ਲੱਖ")
        self.assertEqual(num2words(1000000, lang="pa"), "ਦਸ ਲੱਖ")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="pa", ordinal=True), "ਇੱਕਵਾਂ")
        self.assertEqual(num2words(10, lang="pa", ordinal=True), "ਦਸਵਾਂ")
        self.assertEqual(num2words(100, lang="pa", ordinal=True), "ਇੱਕ ਸੌਵਾਂ")
