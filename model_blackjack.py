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
        self.vrednost = 0

    def __repr__(self):
        return f'Karta({self.barva}, {self.stevilo})'
    
    def vrednost(self):
        if self.stevilo not in range(2,11):
            self.vrednost = 10
        elif self.stevilo == 'A':
            self.vrednost = 1
        else:
            self.vrednost = self.stevilo
class Kup:
    def __init__(self):
        self.kup = None
    
    def zmešaj(self):
        self.kup = [Karta(barva, stevilo) for barva in BARVE for stevilo in [2,3,4,5,6,7,8,9,10,'J','Q','K','A']]
        random.shuffle(self.kup)
        return self.kup
    
    def __repr__(self):
        return f'{self.kup}'


class Igra:
    def __init__(self):
        self.dealer = []
        self.roka1 = []
        self.roka2 = []
        self.kup = Kup().zmešaj()

#    def odstrani_dvojnike(self, seznam):
#        for x in seznam:
#            self.kup.remove(x)
    
    def deal(self):
        že_podeljene = []    
        for karta in self.kup:
            if len(self.roka1) < 2 and karta not in že_podeljene :
                self.roka1.append(karta)
                že_podeljene.append(karta)
            elif karta not in self.roka1 and karta not in že_podeljene and len(self.dealer) < 2:
                self.dealer.append(karta)
                že_podeljene.append(karta)
            else:
                continue
        for karta in že_podeljene:
            self.kup.remove(karta)
    
    def hit(self):
        self.roka1.append(self.kup[0])
        self.kup.remove(self.roka1[-1])
    
    def diler(self):
        vsota = 0
        for karta in self.dealer:
            vsota += karta.vrednost()
            if vsota <= 16:
                self.dealer.append(self.kup[0])
            else:
                pass







    def __repr__(self):
        return f'{self.dealer},{self.roka1}, {len(self.kup)}'
m = Igra()
m.deal()
m.diler()
print(str(m))