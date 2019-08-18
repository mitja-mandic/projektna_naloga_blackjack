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
ZMEŠAN_KUP = Kup().zmešaj()
class Igralec:
    def __init__(self, ime):
        self.roka = []
        self.ime = ime
    
    def __repr__(self):
        return f'{self.ime}, {self.roka}'


    def deal(self):
        že_podeljene = []
        for karta in ZMEŠAN_KUP:
            if len(self.roka) < 2 and karta not in že_podeljene :
                self.roka.append(karta)
                že_podeljene.append(karta)
            else:
                continue
        for karta in že_podeljene:
            ZMEŠAN_KUP.remove(karta)
        return ZMEŠAN_KUP
        return self.roka
