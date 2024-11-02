# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_OR(Num2Word_EU):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):
        self.low_numwords = [
            "ଅନେଶତ ଅନେଶ",  # 99
            "ଅନେଶତ ଅଶି",  # 98
            "ଅନେଶତ ସତୁରି",  # 97
            "ଅନେଶତ ଛଅଷଠି",  # 96
            "ଅନେଶତ ପଞ୍ଚାନବେ",  # 95
            "ଅନେଶତ ଚଉରାନବେ",  # 94
            "ଅନେଶତ ତେରାନବେ",  # 93
            "ଅନେଶତ ବାନବେ",  # 92
            "ଅନେଶତ ଏକାନବେ",  # 91
            "ଅନେଶତ",  # 90
            "ଅଶୀ ନଅ",  # 89
            # ... continue with all numbers down to 1
            "ଉନେଇଶ",  # 19
            "ଅଠର",  # 18
            "ସତର",  # 17
            "ଷୋହଳ",  # 16
            "ପନ୍ଦର",  # 15
            "ଚଉଦ",  # 14
            "ତେର",  # 13
            "ବାର",  # 12
            "ଏଗାର",  # 11
            "ଦଶ",  # 10
            "ନଅ",  # 9
            "ଆଠ",  # 8
            "ସାତ",  # 7
            "ଛଅ",  # 6
            "ପାଞ୍ଚ",  # 5
            "ଚାରି",  # 4
            "ତିନି",  # 3
            "ଦୁଇ",  # 2
            "ଏକ",  # 1
            "ଶୂନ୍ୟ",  # 0
        ]

        self.mid_numwords = [(100, "ଶହ")]

        self.high_numwords = [(7, "କୋଟି"), (5, "ଲକ୍ଷ"), (3, "ହଜାର")]

        self.pointword = "ବିନ୍ଦୁ"

        self.cardinal_words = self.low_numwords.copy()
        self.ordinal_words = []

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s-%s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outword = self.to_cardinal(value)
        return outword + "ତମ"

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "ମ"
