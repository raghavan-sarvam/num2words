# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsTATest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(1, lang="ta"), "ஒன்று")
        self.assertEqual(num2words(10, lang="ta"), "பத்து")
        self.assertEqual(num2words(21, lang="ta"), "இருபத்து ஒன்று")
        self.assertEqual(num2words(100, lang="ta"), "நூறு")
        self.assertEqual(num2words(1000, lang="ta"), "ஆயிரம்")
        self.assertEqual(num2words(100000, lang="ta"), "ஒரு லட்சம்")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="ta", ordinal=True), "ஒன்றுவது")
        self.assertEqual(num2words(10, lang="ta", ordinal=True), "பத்துவது")

    def test_decimal(self):
        self.assertEqual(num2words(1.1, lang="ta"), "ஒன்று புள்ளி ஒன்று")
        self.assertEqual(
            num2words(2.345, lang="ta"), "இரண்டு புள்ளி மூன்று நான்கு ஐந்து"
        )
