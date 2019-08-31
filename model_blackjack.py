import random
DENAR = 100   
BARVE = ['Srca', 'Kara', 'Pik', 'Križ']
ZMAGA = 'wW'
PORAZ = 'xx'
ZMAGA_RUNDE = 'w'
PORAZ_RUNDE = 'x'
PUSH = 'p'
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
        self.roke = [self.roka1, self.roka2]
        self.znesek = 0
        self.vrednost_roke = 0
        self.kup = Kup().zmešaj()
    
    def stava(self, znesek):
        global DENAR
        if znesek <= DENAR and znesek != 0:
            DENAR -= znesek
            self.znesek += znesek
            return True
        else:
            return False 

    def deal(self, roka):
        že_podeljene = []    
        #if self.stava:
        for karta in self.kup:
            if len(roka) < 2 and karta not in že_podeljene :
                roka.append(karta)
                že_podeljene.append(karta)
            elif karta not in roka and karta not in že_podeljene and len(self.dealer) < 2:
                self.dealer.append(karta)
                že_podeljene.append(karta)
            else:
                continue
        
        for karta in že_podeljene:
            self.kup.remove(karta)
        
    def hit(self, igralec):
        if self.stava:    
            igralec.append(self.kup[0])
            self.kup.remove(igralec[-1])

    def doloci_vrednost_roke(self, igralec):    
        self.vrednost_roke = 0
        for karta in igralec:
            if karta.stevilo not in range(2,12) and karta.stevilo != 'A':
                self.vrednost_roke += 10
            elif karta.stevilo == 'A':
                self.vrednost_roke += 1
            else:
                self.vrednost_roke += karta.stevilo
        return self.vrednost_roke

    def soft_hand(self, roka):
        for i, s in enumerate(roka):
            if s.stevilo == 'A':
                roka[i] = Karta(barva=s.barva,stevilo = 11)
                return roka

    def dealers_play(self):
        while self.doloci_vrednost_roke(self.dealer) <= 17:
            self.dealer.append(self.kup[0])
            self.kup.remove(self.dealer[-1])

    def split(self):
        if self.roka1[0].stevilo == self.roka1[1].stevilo:
            self.roka2.append(self.roka1[1])
            self.roka1.pop()
            self.znesek *= 2
            for roka in self.roke:
                self.deal(roka)
            return True
        else:
            return False

    def konec_igre(self, roka):
        global DENAR
        if DENAR <= 0:
            return PORAZ
        elif DENAR == 300:
            return ZMAGA
        elif (self.doloci_vrednost_roke(self.dealer) < 21) and (self.doloci_vrednost_roke(roka) < 21) and self.doloci_vrednost_roke(roka) == self.doloci_vrednost_roke(self.dealer):
            self.znesek = 0
            return PUSH
        elif self.doloci_vrednost_roke(roka) > 21:
            DENAR -= self.znesek
            self.znesek = 0
            return PORAZ_RUNDE
        elif self.doloci_vrednost_roke(roka) == 21:
            DENAR += self.znesek
            self.znesek = 0
            return ZMAGA_RUNDE
        elif self.doloci_vrednost_roke(self.dealer) == 21:
            DENAR -= self.znesek
            self.znesek = 0
            return PORAZ_RUNDE
        elif self.doloci_vrednost_roke(self.dealer) > 21: 
            DENAR += self.znesek
            self.znesek = 0
            return ZMAGA_RUNDE
        elif (self.doloci_vrednost_roke(self.dealer) < 21) and (self.doloci_vrednost_roke(roka) < 21) and (self.doloci_vrednost_roke(roka) < self.doloci_vrednost_roke(self.dealer)):
            DENAR -= self.znesek
            self.znesek = 0
            return PORAZ_RUNDE
        elif (self.doloci_vrednost_roke(self.dealer) < 21) and (self.doloci_vrednost_roke(roka) < 21) and (self.doloci_vrednost_roke(roka) > self.doloci_vrednost_roke(self.dealer)):
            DENAR += self.znesek
            self.znesek = 0
            return ZMAGA_RUNDE
        
    def reset(self):
        self.dealer = []
        self.roka1 = []
        self.roka2 = []
        self.roke = [self.roka1, self.roka2]
        self.kup = Kup().zmešaj()
        self.deal(self.roka1)
    
    def preveri_konec(self):
        rezultati = []
        for roka in self.roke:
            if roka != []:
                if self.konec_igre(roka) == ZMAGA_RUNDE:
                    rezultati.append(1)
                elif self.konec_igre(roka) == PORAZ_RUNDE:
                    rezultati.append(-2)
                elif self.konec_igre(roka) == PUSH:
                    rezultati.append(0)
        if sum(rezultati) == 0:
            return PUSH
        elif sum(rezultati) < 0:
            return PORAZ_RUNDE
        else:
            return ZMAGA_RUNDE
    
    
    
    def __repr__(self):
        return f'{self.roka1},{self.roka2},{self.roke}'
    #return f'{self.roka1},{self.dealer},{self.doloci_vrednost_roke(self.roka1)},{self.doloci_vrednost_roke(self.dealer)}'

#m = Igra()
#m.deal(m.roka1)
#print(repr(m))
#m.split()
#print(repr(m))



def nova_igra():
    return Igra()