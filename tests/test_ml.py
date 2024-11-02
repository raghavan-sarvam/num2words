# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from num2words import num2words
from num2words.lang_ML import Num2Word_ML


class TestML(unittest.TestCase):
    def setUp(self):
        self.n2w = Num2Word_ML()

    def test_number(self):
        # self.assertEqual(num2words(1, lang='ml'), 'ഒന്ന് നൂറ്')
        self.assertEqual(num2words(12, lang="ml"), "പന്ത്രണ്ട്")
        self.assertEqual(num2words(100, lang="ml"), "ഒന്ന് നൂറ്")
        self.assertEqual(num2words(1000, lang="ml"), "ഒന്ന് ആയിരം")
        self.assertEqual(num2words(10000, lang="ml"), "പത്ത് ആയിരം")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="ml", ordinal=True), "ഒന്ന്ആമത്")
        self.assertEqual(num2words(5, lang="ml", ordinal=True), "അഞ്ച്ആമത്")
