import random
DENAR = 100   
STAVA = 0
BARVE = ['Srca', 'Kara', 'Pik', 'Križ']
ZMAGA = 'w'
PORAZ = 'x'

class Karta:
    def __init__(self, barva, stevilo):
        self.barva = barva
        self.stevilo = stevilo

    def __repr__(self):
        return f'Karta({self.barva}, {self.stevilo})'
    
    def vrednost(self):
        if self.stevilo not in range(2,11):
            self.vrednost = 10
            return self.vrednost
        elif self.stevilo == 'A':
            self.vrednost == 1
            return int(self.vrednost)
        else:
            return int(self.stevilo)
class Kup:
    def __init__(self):
        self.kup = None
    
    def zmešaj(self):
        self.kup = [Karta(barva, stevilo) for barva in BARVE for stevilo in [2,3,4,5,6,7,8,9,10,'J','Q','K','A']]
        random.shuffle(self.kup)
        return self.kup


class Igra:
    def __init__(self):
        self.dealer = []
        self.roka1 = []
        self.roka2 = []
        self.kup = Kup().zmešaj()

    def odstrani_dvojnike(self):
        for karta in self.roka1:
            self.kup.remove(karta)
        return self.kup
    
    def deal(self):
        že_podeljene = []
        for karta in self.kup:
            if len(self.dealer) < 2 and karta not in že_podeljene :
                self.dealer.append(karta)
                že_podeljene.append(karta)
            else:
                continue      
        self.kup.odstrani_dvojnike()
        for karta in self.kup:
            if len(self.roka1) < 2 and karta not in že_podeljene :
                self.roka1.append(karta)
                že_podeljene.append(karta)
            else:
                continue
        return self.roka1
        if sum(karta.vrednost() for karta in self.roka1) == 21:
            return ZMAGA
    
    
    def hit(self):
        self.roka1.append(self.kup[0])
        return self.roka1
    def __repr__(self):
        return f'{self.dealer},{self.roka}'
m = Igra()
m.deal()
print(repr(m))
    
    
