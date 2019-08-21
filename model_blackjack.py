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
        self.znesek = 0
        self.kup = Kup().zmešaj()
    
    def stava(self, znesek):
        global DENAR
        if znesek <= DENAR and znesek != 0:
            DENAR -= znesek
            self.znesek += znesek
            return True
        else:
            return False 

    def deal(self):
        že_podeljene = []    
        
        if self.stava:
            for karta in self.kup:
                if len(self.roka1) < 2 and karta not in že_podeljene :
                    self.roka1.append(karta)
                    že_podeljene.append(karta)
                elif karta not in self.roka1 and karta not in že_podeljene and len(self.dealer) < 2:
                    self.dealer.append(karta)
                    že_podeljene.append(karta)
                else:
                    continue
        else:
            print('stavi')
        for karta in že_podeljene:
            self.kup.remove(karta)
        
    def hit(self, igralec):
        if self.stava:
            igralec.append(self.kup[0])
            self.kup.remove(igralec[-1])

    def doloci_vrednost_roke(self, igralec):    
        vrednost = 0
        for karta in igralec:
            if karta.stevilo not in range(2,11) and karta.stevilo != 'A':
                vrednost += 10
            elif karta.stevilo == 'A':
                vrednost += 1
            else:
                vrednost += karta.stevilo
        return vrednost

    def dealers_play(self):
        if self.doloci_vrednost_roke(self.dealer) <= 16:
            self.dealer.append(self.kup[0])
            self.kup.remove(self.dealer[-1])
        else:
            pass
        
    def konec_igre(self):
        global DENAR
        if self.doloci_vrednost_roke(self.roka1) > 21 or self.doloci_vrednost_roke(self.dealer) == 21:
            return PORAZ
        elif self.doloci_vrednost_roke(self.dealer) > 21 or self.doloci_vrednost_roke(self.roka1) == 21:
            DENAR += self.znesek
            return ZMAGA
        elif DENAR == 0:
            return PORAZ

    def __repr__(self):
        return f'{self.roka1},{self.dealer},{self.znesek},{DENAR}'

def nova_igra():
    return Igra()