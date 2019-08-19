import random
DENAR = 100   
STAVA = 0
BARVE = ['Srca', 'Kara', 'Pik', 'Križ']
ZMAGA = 'w'
PORAZ = 'x'

class Karta:
    def __init__(self, barva, stevilo, vrednost):
        self.barva = barva
        self.stevilo = stevilo
        self.vrednost = vrednost
        
 


    def __repr__(self):
        return f'Karta({self.barva}, {self.stevilo}, {self.vrednost})'





class Kup:
    def __init__(self):
        self.kup = None
    
    def zmešaj(self):
        self.kup = [Karta(barva, stevilo, vrednost) for barva in BARVE for stevilo in [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] for vrednost in range(1,10)]
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
    
    #def vrednost(self, seznam):    
    #    if karta.stevilo not in range(2,11):
    #        karta.vrednost = 10
    #    elif karta.stevilo == 'A':
    #        karta.vrednost = 1
    #    else:
    #        karta.vrednost = karta.stevilo
    
    def doloci_vrednost_roke(self, seznam):
        vsota = 0
        for karta in seznam:
            vsota += karta.vrednost

        return vsota
    def __repr__(self):
        return f'{self.roka1}'

m = Igra()
m.deal()
m.vrednost(m.roka1)
print(repr(m))

print(str(m.doloci_vrednost_roke(m.roka1)))