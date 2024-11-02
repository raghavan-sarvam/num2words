# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsGUTest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(100, lang="gu"), "એક સો")
        self.assertEqual(num2words(101, lang="gu"), "એક સો એક")
        self.assertEqual(num2words(1000, lang="gu"), "એક હજાર")
        self.assertEqual(num2words(12000, lang="gu"), "બાર હજાર")
        self.assertEqual(num2words(100000, lang="gu"), "એક લાખ")
        self.assertEqual(num2words(1000000, lang="gu"), "દસ લાખ")
        self.assertEqual(num2words(10000000, lang="gu"), "એક કરોડ")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="gu", ordinal=True), "એકમો")
        self.assertEqual(num2words(10, lang="gu", ordinal=True), "દસમો")
        self.assertEqual(num2words(100, lang="gu", ordinal=True), "એક સોમો")
        self.assertEqual(num2words(1000, lang="gu", ordinal=True), "એક હજારમો")
