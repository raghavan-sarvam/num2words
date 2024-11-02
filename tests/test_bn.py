# -*- coding: utf-8 -*-

from unittest import TestCase

from num2words import num2words


class TestBN(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(100, lang="bn"), "এক শত")
        self.assertEqual(num2words(101, lang="bn"), "এক শত এক")
        self.assertEqual(num2words(1000, lang="bn"), "এক হাজার")
        self.assertEqual(num2words(1001, lang="bn"), "এক হাজার এক")
        self.assertEqual(num2words(10000, lang="bn"), "দশ হাজার")
        self.assertEqual(num2words(100000, lang="bn"), "এক লক্ষ")
        self.assertEqual(num2words(1000000, lang="bn"), "দশ লক্ষ")
        self.assertEqual(num2words(10000000, lang="bn"), "এক কোটি")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="bn", ordinal=True), "একতম")
        self.assertEqual(num2words(10, lang="bn", ordinal=True), "দশতম")
        self.assertEqual(num2words(100, lang="bn", ordinal=True), "এক শততম")
        self.assertEqual(num2words(1000, lang="bn", ordinal=True),
                         "এক হাজারতম")

    def test_ordinal_num(self):
        self.assertEqual(
            num2words(1, lang="bn", ordinal=True, to="ordinal_num"), "একতম"
        )
        self.assertEqual(
            num2words(10, lang="bn", ordinal=True, to="ordinal_num"), "দশতম"
        )
