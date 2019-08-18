import random
DENAR = 100   
STAVA = 0
BARVE = ['Srca', 'Kara', 'Pik', 'Križ']

class Karta:
    def __init__(self, barva, stevilo):
        self.barva = barva
        self.stevilo = stevilo

    def __repr__(self):
        return f'Karta({self.barva}, {self.stevilo})'
    
    def vredost(self):
        if self.stevilo in range(1,11):
            self.vrednost = self.stevilo
        elif self.stevilo in range(11,14):
            self.vrednost == 10

class Kup:
    def __init__(self):
        self.kup = None
    
    def zmešaj(self):
        self.kup = [Karta(barva, stevilo) for barva in BARVE for stevilo in range(1, 14)]
        random.shuffle(self.kup)
        return self.kup

    def __repr__(self):
        return f'{self.kup}'

class Igralec:
    def __init__(self):
        self.roka = []
    def hit(self):
        self.roka.append(Kup().zmešaj()[1])

    def __str__(self):
        return f'igralec, {self.roka}'
m = Igralec()
m.hit()
print(str(m))