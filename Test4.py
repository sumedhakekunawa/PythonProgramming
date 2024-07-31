class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1

    def show(self):
        print(self.nr)
        print(f'{self.nr}/{self.dr}')


f1 = Fraction(2, 3)
f1.show()
