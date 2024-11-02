# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class TestMR(TestCase):
    def setup(self):
        self.n2w = num2words
        self.lang = 'mr'

    def test_cardinal_small(self):
        self.assertEqual(num2words(0, lang="mr"), "शून्य")
        self.assertEqual(num2words(1, lang="mr"), "एक")
        self.assertEqual(num2words(5, lang="mr"), "पाच")
        self.assertEqual(num2words(10, lang="mr"), "दहा")
        self.assertEqual(num2words(15, lang="mr"), "पंधरा")
        self.assertEqual(num2words(20, lang="mr"), "वीस")
        self.assertEqual(num2words(25, lang="mr"), "पंचवीस")

    def test_cardinal_medium(self):
        self.assertEqual(num2words(100, lang="mr"), "एक शंभर")
        self.assertEqual(num2words(1000, lang="mr"), "एक हजार")
        self.assertEqual(num2words(100000, lang="mr"), "एक लाख")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="mr", ordinal=True), "एकवा")
        self.assertEqual(num2words(5, lang="mr", ordinal=True), "पाचवा")
        self.assertEqual(num2words(10, lang="mr", ordinal=True), "दहावा")
