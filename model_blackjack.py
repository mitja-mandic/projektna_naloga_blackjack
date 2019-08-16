import random
DENAR = 100   
STAVA = 0

class Karta:
    FACES = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    
    def __init__(self, barva, vrednost):
        self.barva = barva
        self.vrednost = vrednost
    
    def __str__(self):
        return "{0}, {1}".format(self.barva, self.vrednost)
vrednosti = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
barve = [1,2,3,4]

deck = [Karta(barva, vrednost) for barva in range(1,4) for vrednost in range(1, 14)]
random.shuffle(deck)
for karta in deck: print(str(karta))