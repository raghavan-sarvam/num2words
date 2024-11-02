# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from num2words import num2words


def test_number():
    assert num2words(1, lang="or") == "ଏକ"
    assert num2words(2, lang="or") == "ଦୁଇ"
    assert num2words(3, lang="or") == "ତିନି"
    assert num2words(10, lang="or") == "ଦଶ"
    assert num2words(15, lang="or") == "ପନ୍ଦର"
    assert num2words(20, lang="or") == "କୋଡ଼ିଏ"
    assert num2words(100, lang="or") == "ଶହ"
    assert num2words(1000, lang="or") == "ଏକ ହଜାର"
    assert num2words(100000, lang="or") == "ଏକ ଲକ୍ଷ"
    assert num2words(1000000, lang="or") == "ଦଶ ଲକ୍ଷ"


def test_ordinal():
    assert num2words(1, lang="or", ordinal=True) == "ପ୍ରଥମ"
    assert num2words(2, lang="or", ordinal=True) == "ଦ୍ୱିତୀୟ"
    assert num2words(3, lang="or", ordinal=True) == "ତୃତୀୟ"
    assert num2words(10, lang="or", ordinal=True) == "ଦଶମ"
