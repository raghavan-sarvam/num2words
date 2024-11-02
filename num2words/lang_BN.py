# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_BN(Num2Word_EU):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):
        self.low_numwords = [
            "নিরানব্বই",
            "আটানব্বই",
            "সাতানব্বই",
            "ছিয়ানব্বই",
            "পঁচানব্বই",
            "চুরানব্বই",
            "তিরানব্বই",
            "বিরানব্বই",
            "একানব্বই",
            "নব্বই",
            "উননব্বই",
            "আটাশি",
            "সাতাশি",
            "ছিয়াশি",
            "পঁচাশি",
            "চুরাশি",
            "তিরাশি",
            "বিরাশি",
            "একাশি",
            "আশি",
            "ঊনআশি",
            "আটাত্তর",
            "সাতাত্তর",
            "ছিয়াত্তর",
            "পঁচাত্তর",
            "চুয়াত্তর",
            "তিয়াত্তর",
            "বাহাত্তর",
            "একাত্তর",
            "সত্তর",
            "ঊনসত্তর",
            "আটষট্টি",
            "সাতষট্টি",
            "ছেষট্টি",
            "পঁয়ষট্টি",
            "চৌষট্টি",
            "তেষট্টি",
            "বাষট্টি",
            "একষট্টি",
            "ষাট",
            "ঊনষাট",
            "আটান্ন",
            "সাতান্ন",
            "ছাপ্পান্ন",
            "পঞ্চান্ন",
            "চুয়ান্ন",
            "তিপ্পান্ন",
            "বায়ান্ন",
            "একান্ন",
            "পঞ্চাশ",
            "ঊনপঞ্চাশ",
            "আটচল্লিশ",
            "সাতচল্লিশ",
            "ছেচল্লিশ",
            "পঁয়তাল্লিশ",
            "চুয়াল্লিশ",
            "তেতাল্লিশ",
            "বিয়াল্লিশ",
            "একচল্লিশ",
            "চল্লিশ",
            "ঊনচল্লিশ",
            "আটত্রিশ",
            "সাঁইত্রিশ",
            "ছত্রিশ",
            "পঁয়ত্রিশ",
            "চৌত্রিশ",
            "তেত্রিশ",
            "বত্রিশ",
            "একত্রিশ",
            "ত্রিশ",
            "ঊনত্রিশ",
            "আটাশ",
            "সাতাশ",
            "ছাব্বিশ",
            "পঁচিশ",
            "চব্বিশ",
            "তেইশ",
            "বাইশ",
            "একুশ",
            "কুড়ি",
            "উনিশ",
            "আঠারো",
            "সতেরো",
            "ষোলো",
            "পনেরো",
            "চৌদ্দ",
            "তেরো",
            "বারো",
            "এগারো",
            "দশ",
            "নয়",
            "আট",
            "সা��",
            "ছয়",
            "পাঁচ",
            "চার",
            "তিন",
            "দুই",
            "এক",
            "শূন্য",
        ]

        self.mid_numwords = [(100, "শত")]

        self.high_numwords = [(7, "কোটি"), (5, "লক্ষ"), (3, "হাজার")]

        self.pointword = "দশমিক"

        self.cardinal_words = self.low_numwords.copy()

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outword = self.to_cardinal(value)
        return outword + "তম"

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "তম"
