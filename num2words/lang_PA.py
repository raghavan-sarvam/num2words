# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_PA(Num2Word_EU):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):
        self.low_numwords = [
            "ਨੜਿੱਨਵੇਂ",
            "ਅਠਾਨਵੇਂ",
            "ਸਤਾਨਵੇਂ",
            "ਛਿਆਨਵੇਂ",
            "ਪਚਾਨਵੇਂ",
            "ਚੌਰਾਨਵੇਂ",
            "ਤਿਰਾਨਵੇਂ",
            "ਬਾਨਵੇਂ",
            "ਇੱਕਾਨਵੇਂ",
            "ਨੱਬੇ",
            "ਉਨਾਨਵੇਂ",
            "ਅਠਾਸੀ",
            "ਸਤਾਸੀ",
            "ਛਿਆਸੀ",
            "ਪਚਾਸੀ",
            "ਚੌਰਾਸੀ",
            "ਤਿਰਾਸੀ",
            "ਬਿਆਸੀ",
            "ਇੱਕਾਸੀ",
            "ਅੱਸੀ",
            "ਉਨੱਤਰ",
            "ਅਠੱਤਰ",
            "ਸਤੱਤਰ",
            "ਛਿਹੱਤਰ",
            "ਪਚੱਤਰ",
            "ਚੌਹੱਤਰ",
            "ਤਿਹੱਤਰ",
            "ਬਹੱਤਰ",
            "ਇਕਹੱਤਰ",
            "ਸੱਤਰ",
            "ਉਨਾਹਠ",
            "ਅਠਾਹਠ",
            "ਸਤਾਹਠ",
            "ਛਿਆਹਠ",
            "ਪੈਂਹਠ",
            "ਚੌਂਹਠ",
            "ਤਰੇਹਠ",
            "ਬਾਹਠ",
            "ਇਕਾਹਠ",
            "ਸੱਠ",
            "ਉਨੰਜਾ",
            "ਅਠਵੰਜਾ",
            "ਸਤਵੰਜਾ",
            "ਛਪੰਜਾ",
            "ਪਚਵੰਜਾ",
            "ਚੌਵੰਜਾ",
            "ਤਿਰਵੰਜਾ",
            "ਬਵੰਜਾ",
            "ਇੱਕਵੰਜਾ",
            "ਪੰਜਾਹ",
            "ਉਨੰਜਾ",
            "ਅੜਤਾਲੀ",
            "ਸੈਂਤਾਲੀ",
            "ਛਿਆਲੀ",
            "ਪੈਂਤਾਲੀ",
            "ਚੌਤਾਲੀ",
            "ਤੈਂਤਾਲੀ",
            "ਬਿਆਲੀ",
            "ਇਕਤਾਲੀ",
            "ਚਾਲੀ",
            "ਉਨਤਾਲੀ",
            "ਅਠੱਤੀ",
            "���ੈਂਤੀ",
            "ਛੱਤੀ",
            "ਪੈਂਤੀ",
            "ਚੌਂਤੀ",
            "ਤੇਤੀ",
            "ਬੱਤੀ",
            "ਇਕੱਤੀ",
            "ਤੀਹ",
            "ਉਨੱਤੀ",
            "ਅਠਾਈ",
            "ਸਤਾਈ",
            "ਛੱਬੀ",
            "ਪੱਚੀ",
            "ਚੌਵੀ",
            "ਤੇਈ",
            "ਬਾਈ",
            "ਇੱਕੀ",
            "ਵੀਹ",
            "ਉਨ੍ਨੀ",
            "ਅਠਾਰਾਂ",
            "ਸਤਾਰਾਂ",
            "ਸੋਲਾਂ",
            "ਪੰਦਰਾਂ",
            "ਚੌਦਾਂ",
            "ਤੇਰਾਂ",
            "ਬਾਰਾਂ",
            "ਗਿਆਰਾਂ",
            "ਦਸ",
            "ਨੌਂ",
            "ਅੱਠ",
            "ਸੱਤ",
            "ਛੇ",
            "ਪੰਜ",
            "ਚਾਰ",
            "ਤਿੰਨ",
            "ਦੋ",
            "ਇੱਕ",
            "ਸਿਫ਼ਰ",
        ]

        self.mid_numwords = [(100, "ਸੌ")]

        self.high_numwords = [(7, "ਕਰੋੜ"), (5, "ਲੱਖ"), (3, "ਹਜ਼ਾਰ")]

        self.pointword = "ਦਸ਼ਮਲਵ"

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
        return outword + "ਵਾਂ"

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return str(value) + "ਵਾਂ"
