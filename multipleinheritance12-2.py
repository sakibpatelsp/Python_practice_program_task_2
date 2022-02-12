"""PROGRAM TO DEMONSTRATE MULTIPLE INHERTANCE"""

class sp:
    def apple(self):
        return "apple"
class om:
    def orange(self):
        return " orange is sweet"
class smartsp(sp, om):
    pass
s1 = smartsp()
print(s1.apple(), "and", s1.orange())