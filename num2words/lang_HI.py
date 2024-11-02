# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_HI(Num2Word_EU):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):
        self.low_numwords = [
            "निन्यानवे",
            "अट्ठानवे",
            "सत्तानवे",
            "छियानवे",
            "पचानवे",
            "चौरानवे",
            "तिरानवे",
            "बानवे",
            "इक्यानवे",
            "नब्बे",
            "नवासी",
            "अस्सी",
            "उन्यासी",
            "अठहत्तर",
            "सतहत्तर",
            "छिहत्तर",
            "पचहत्तर",
            "चौहत्तर",
            "तिहत्तर",
            "बहत्तर",
            "इकहत्तर",
            "सत्तर",
            "उनहत्तर",
            "अड़सठ",
            "सड़सठ",
            "छियासठ",
            "पैंसठ",
            "चौंसठ",
            "तिरसठ",
            "बासठ",
            "इकसठ",
            "साठ",
            "उनसठ",
            "अट्ठावन",
            "सत्तावन",
            "छप्पन",
            "पचपन",
            "चौवन",
            "तिरेपन",
            "बावन",
            "इक्यावन",
            "पचास",
            "उनचास",
            "अड़तालीस",
            "सैंतालीस",
            "छियालीस",
            "पैंतालीस",
            "चौंतालीस",
            "तैंतालीस",
            "बयालीस",
            "इकतालीस",
            "चालीस",
            "उनतालीस",
            "अड़तीस",
            "सैंतीस",
            "छत्तीस",
            "पैंतीस",
            "चौंतीस",
            "तैंतीस",
            "बत्तीस",
            "इकत्तीस",
            "तीस",
            "उनतीस",
            "अट्ठाईस",
            "सत्ताईस",
            "छब्बीस",
            "पच्चीस",
            "चौबीस",
            "तेईस",
            "बाईस",
            "इक्कीस",
            "बीस",
            "उन्नीस",
            "अठारह",
            "सत्रह",
            "सोलह",
            "पंद्रह",
            "चौदह",
            "तेरह",
            "बारह",
            "ग्यारह",
            "दस",
            "नौ",
            "आठ",
            "सात",
            "छह",
            "पाँच",
            "चार",
            "तीन",
            "दो",
            "एक",
            "शून्य",
        ]

        self.mid_numwords = [(100, "सौ")]

        self.high_numwords = [
            (7, "करोड़"),
            (5, "लाख"),
            (3, "हज़ार"),
        ]

        self.pointword = "दशमलव"

        self.cardinal_words = self.low_numwords.copy()
        self.ordinal_words = [
            "पहला",
            "दूसरा",
            "तीसरा",
            "चौथा",
            "पाँचवाँ",
            "छठा",
            "सातवाँ",
            "आठवाँ",
            "नौवाँ",
            "दसवाँ",
        ]

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
        if value <= 10:
            return self.ordinal_words[value - 1]
        return self.to_cardinal(value) + "वाँ"

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "वाँ"
