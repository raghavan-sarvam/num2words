# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_MR(Num2Word_EU):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):
        self.low_numwords = [
            "नव्व्याण्णव",
            "अठ्ठ्याण्णव",
            "सत्त्याण्णव",
            "शहाण्णव",
            "पंच्याण्णव",
            "चौऱ्याण्णव",
            "त्र्याण्णव",
            "ब्याण्णव",
            "एक्याण्णव",
            "नव्वद",
            "एकोणनव्वद",
            "अठ्ठ्याऐंशी",
            "सत्त्याऐंशी",
            "शहाऐंशी",
            "पंच्याऐंशी",
            "चौऱ्याऐंशी",
            "त्र्याऐंशी",
            "ब्याऐंशी",
            "एक्क्याऐंशी",
            "ऐंशी",
            "एकोणऐंशी",
            "अठ्ठ्याहत्तर",
            "सत्त्याहत्तर",
            "शहात्तर",
            "पंच्याहत्तर",
            "चौऱ्याहत्तर",
            "त्र्याहत्तर",
            "बहात्तर",
            "एकाहत्तर",
            "सत्तर",
            "एकोणसत्तर",
            "अडुसष्ट",
            "सदुसष्ट",
            "सहासष्ट",
            "पासष्ट",
            "चौसष्ट",
            "त्रेसष्ट",
            "बासष्ट",
            "एकसष्ट",
            "साठ",
            "एकोणसाठ",
            "अठ्ठावन्न",
            "सत्तावन्न",
            "छप्पन्न",
            "पंचावन्न",
            "चौपन्न",
            "त्रेपन्न",
            "बावन्न",
            "एक्कावन्न",
            "पन्नास",
            "एकोणपन्नास",
            "अठ्ठेचाळीस",
            "सत्तेचाळीस",
            "सेहेचाळीस",
            "पंचेचाळीस",
            "चव्वेचाळीस",
            "त्रेचाळीस",
            "बेचाळीस",
            "एकेचाळीस",
            "चाळीस",
            "एकोणचाळीस",
            "अडतीस",
            "सदतीस",
            "छत्तीस",
            "पस्तीस",
            "चौतीस",
            "तेहतीस",
            "बत्तीस",
            "एकतीस",
            "तीस",
            "एकोणतीस",
            "अठ्ठावीस",
            "सत्तावीस",
            "सव्वीस",
            "पंचवीस",
            "चोवीस",
            "तेवीस",
            "बावीस",
            "एकवीस",
            "वीस",
            "एकोणीस",
            "अठरा",
            "सतरा",
            "सोळा",
            "पंधरा",
            "चौदा",
            "तेरा",
            "बारा",
            "अकरा",
            "दहा",
            "नऊ",
            "आठ",
            "सात",
            "सहा",
            "पाच",
            "चार",
            "तीन",
            "दोन",
            "एक",
            "शून्य",
        ]

        self.mid_numwords = [(100, "शंभर")]

        self.high_numwords = [(7, "कोटी"), (5, "लाख"), (3, "हजार")]

        self.pointword = "दशांश"

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
        return outword + "वा"

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "वा"
