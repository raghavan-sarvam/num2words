# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_TA(Num2Word_EU):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):
        self.low_numwords = [
            "தொண்ணூற்று ஒன்பது",
            "தொண்ணூற்று எட்டு",
            "தொண்ணூற்று ஏழு",
            "தொண்ணூற்று ஆறு",
            "தொண்ணூற்று ஐந்து",
            "தொண்ணூற்று நான்கு",
            "தொண்ணூற்று மூன்று",
            "தொண்ணூற்று இரண்டு",
            "தொண்ணூற்று ஒன்று",
            "தொண்ணூறு",
            "எண்பத்து ஒன்பது",
            "எண்பத்து எட்டு",
            "எண்பத்து ஏழு",
            "எண்பத்து ஆறு",
            "எண்பத்து ஐந்து",
            "எண்பத்து நான்கு",
            "எண்பத்து மூன்று",
            "எண்பத்து இரண்டு",
            "எண்பத்து ஒன்று",
            "எண்பது",
            "எழுபத்து ஒன்பது",
            "எழுபத்து எட்டு",
            "எழுபத்து ஏழு",
            "எழுபத்து ஆறு",
            "எழுபத்து ஐந்து",
            "எழுபத்து நான்கு",
            "எழுபத்து மூன்று",
            "எழுபத்து இரண்டு",
            "எழுபத்து ஒன்று",
            "எழுபது",
            "அறுபத்து ஒன்பது",
            "அறுபத்து எட்டு",
            "அறுபத்து ஏழு",
            "அறுபத்து ஆறு",
            "அறுபத்து ஐந்து",
            "அறுபத்து நான்கு",
            "அறுபத்து மூன்று",
            "அறுபத்து இரண்டு",
            "அறுபத்து ஒன்று",
            "அறுபது",
            "ஐம்பத்து ஒன்பது",
            "ஐம்பத்து எட்டு",
            "ஐம்பத்து ஏழு",
            "ஐம்பத்து ஆறு",
            "ஐம்பத்து ஐந்து",
            "ஐம்பத்து நான்கு",
            "ஐம்பத்து மூன்று",
            "ஐம்பத்து இரண்டு",
            "ஐம்பத்து ஒன்று",
            "ஐம்பது",
            "நாற்பத்து ஒன்பது",
            "நாற்பத்து எட்டு",
            "நாற்பத்து ஏழு",
            "நாற்பத்து ஆறு",
            "நாற்பத்து ஐந்து",
            "நாற்பத்து நான்கு",
            "நாற்பத்து மூன்று",
            "நாற்பத்து இரண்டு",
            "நாற்பத்து ஒன்று",
            "நாற்பது",
            "முப்பத்து ஒன்பது",
            "முப்பத்து எட்டு",
            "முப்பத்து ஏழு",
            "முப்பத்து ஆறு",
            "முப்பத்து ஐந்து",
            "முப்பத்து நான்கு",
            "முப்பத்து மூன்று",
            "முப்பத்து இரண்டு",
            "முப்பத்து ஒன்று",
            "முப்பது",
            "இருபத்து ஒன்பது",
            "இருபத்து எட்டு",
            "இருபத்து ஏழு",
            "இருபத்து ஆறு",
            "இருபத்து ஐந்து",
            "இருபத்து நான்கு",
            "இருபத்து மூன்று",
            "இருபத்து இரண்டு",
            "இருபத்து ஒன்று",
            "இருபது",
            "பத்தொன்பது",
            "பதினெட்டு",
            "பதினேழு",
            "பதினாறு",
            "பதினைந்து",
            "பதினான்கு",
            "பதிமூன்று",
            "பன்னிரண்டு",
            "பதினொன்று",
            "பத்து",
            "ஒன்பது",
            "எட்டு",
            "ஏழு",
            "ஆறு",
            "ஐந்து",
            "நான்கு",
            "மூன்று",
            "இரண்டு",
            "ஒன்று",
            "பூஜ்யம்",
        ]

        self.mid_numwords = [(100, "நூறு")]

        self.high_numwords = [(7, "கோடி"), (5, "லட்சம்"), (3, "ஆயிரம்")]

        self.pointword = "புள்ளி"

        self.modifiers = []  # Tamil doesn't need modifiers like Telugu

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        # Special case for lakh and crore when left number is 1
        if lnum == 1 and rtext in ["லட்சம்", "கோடி"]:
            return ("ஒரு " + rtext, rnum)
        # Special case for 100, 1000, etc. when left number is 1
        elif lnum == 1 and rnum in [100, 1000]:  # 100, 1000
            return (rtext, rnum)
        elif lnum == 1 and rnum < 100:
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
        outwords = self.to_cardinal(value)
        ordinal_num = outwords + "வது"
        return ordinal_num

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, "வது")
