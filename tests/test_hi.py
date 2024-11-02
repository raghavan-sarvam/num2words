# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from unittest import TestCase

from num2words import num2words


class Num2WordsHITest(TestCase):
    def test_numbers(self):
        self.assertEqual(num2words(66, lang="hi"), "छियासठ")
        self.assertEqual(num2words(1734, lang="hi"), "एक हज़ार सात सौ चौंतीस")
        self.assertEqual(num2words(134, lang="hi"), "एक सौ चौंतीस")
        self.assertEqual(num2words(54411, lang="hi"),
                         "चौवन हज़ार चार सौ ग्यारह")
        self.assertEqual(num2words(42, lang="hi"), "बयालीस")
        # self.assertEqual(num2words(893, lang="hi"),
        #                 "आठ सौ तिरानवे")
        self.assertEqual(num2words(1729, lang="hi"), "एक हज़ार सात सौ उनतीस")
        self.assertEqual(num2words(123, lang="hi"), "एक सौ तेईस")
        self.assertEqual(num2words(32211, lang="hi"),
                         "बत्तीस हज़ार दो सौ ग्यारह")

    def test_cardinal_for_float_number(self):
        self.assertEqual(
            num2words(1.61803, lang="hi"), "एक दशमलव छह एक आठ शून्य तीन"
        )
        self.assertEqual(num2words(34.876, lang="hi"),
                         "चौंतीस दशमलव आठ सात छह")
        self.assertEqual(num2words(3.14, lang="hi"), "तीन दशमलव एक चार")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="hi", to="ordinal"), "पहला")
        self.assertEqual(num2words(2, lang="hi", to="ordinal"), "दूसरा")
        self.assertEqual(num2words(3, lang="hi", to="ordinal"), "तीसरा")
        self.assertEqual(num2words(12, lang="hi", to="ordinal"), "बारहवाँ")
        self.assertEqual(
            num2words(130, lang="hi", to="ordinal"), "एक सौ तीसवाँ"
        )
        self.assertEqual(
            num2words(1003, lang="hi", to="ordinal"), "एक हज़ार तीनवाँ"
        )
        self.assertEqual(num2words(4, lang="hi", to="ordinal"), "चौथा")

    def test_ordinal_num(self):
        self.assertEqual(num2words(2, lang="hi", to="ordinal_num"), "2वाँ")
        self.assertEqual(num2words(3, lang="hi", to="ordinal_num"), "3वाँ")
        self.assertEqual(num2words(5, lang="hi", to="ordinal_num"), "5वाँ")
        self.assertEqual(num2words(16, lang="hi", to="ordinal_num"), "16वाँ")
        self.assertEqual(num2words(113, lang="hi", to="ordinal_num"), "113वाँ")

    def test_large_numbers(self):
        self.assertEqual(num2words(100000, lang="hi"), "एक लाख")
        self.assertEqual(num2words(1000000, lang="hi"), "दस लाख")
        self.assertEqual(num2words(10000000, lang="hi"), "एक करोड़")
        self.assertEqual(
            num2words(100200300, lang="hi"), "दस करोड़ दो लाख तीन सौ"
        )
