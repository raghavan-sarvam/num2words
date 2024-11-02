# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_GU(Num2Word_EU):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):
        self.low_numwords = [
            "નવ્વાણું",
            "અઠ્ઠાણું",
            "સત્તાણું",
            "છન્નું",
            "પંચાણું",
            "ચોરાણું",
            "ત્રાણું",
            "બાણું",
            "એકાણું",
            "નેવું",
            "નેવ્યાસી",
            "ઇઠ્યાસી",
            "સિત્યાસી",
            "છ્યાસી",
            "પંચ્યાસી",
            "ચોર્યાસી",
            "ત્યાસી",
            "બ્યાસી",
            "એક્યાસી",
            "એંસી",
            "ઓગણાએંસી",
            "સિત્તેર",
            "સિત્તોતેર",
            "છોતેર",
            "પંચોતેર",
            "ચુમ્મોતેર",
            "તોતેર",
            "બોતેર",
            "એકોતેર",
            "સિત્તેર",
            "ઓગણોસિત્તેર",
            "આંઠ્સઠ",
            "સડસઠ",
            "છાસઠ",
            "પાંસઠ",
            "ચોસઠ",
            "ત્રેસઠ",
            "બાસઠ",
            "એકસઠ",
            "સાઇઠ",
            "ઓગણસાઠ",
            "અઠ્ઠાવન",
            "સત્તાવન",
            "છપ્પન",
            "પંચાવન",
            "ચોપન",
            "ત્રેપન",
            "બાવન",
            "એકાવન",
            "પચાસ",
            "ઓગણપચાસ",
            "આડતાલીસ",
            "સુડતાલીસ",
            "છેતાલીસ",
            "પિસ્તાલીસ",
            "ચુમ્માલીસ",
            "ત્રેતાલીસ",
            "બેતાલીસ",
            "એકતાલીસ",
            "ચાલીસ",
            "ઓગણચાલીસ",
            "આડત્રીસ",
            "સાડત્રીસ",
            "છત્રીસ",
            "પાંત્રીસ",
            "ચોત્રીસ",
            "તેત્રીસ",
            "બત્રીસ",
            "એકત્રીસ",
            "ત્રીસ",
            "ઓગણત્રીસ",
            "અઠ્ઠાવીસ",
            "સત્તાવીસ",
            "છવ્વીસ",
            "પચ્ચીસ",
            "ચોવીસ",
            "ત્રેવીસ",
            "બાવીસ",
            "એકવીસ",
            "વીસ",
            "ઓગણીસ",
            "અઢાર",
            "સત્તર",
            "સોળ",
            "પંદર",
            "ચૌદ",
            "તેર",
            "બાર",
            "અગિયાર",
            "દસ",
            "નવ",
            "આઠ",
            "સાત",
            "છ",
            "પાંચ",
            "ચાર",
            "ત્રણ",
            "બે",
            "એક",
            "શૂન્ય",
        ]

        self.mid_numwords = [(100, "સો")]

        self.high_numwords = [(7, "કરોડ"), (5, "લાખ"), (3, "હજાર")]

        self.pointword = "દશાંશ"

        self.cardinal_words = self.low_numwords.copy()

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
        return outword + "મો"

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "મો"
