import model_blackjack
lojtrice = "######################################\n"



def začetek():
    tekst = lojtrice + 'Pozdravljeni! Začenjate igro blackjacka. Imate 100 žetonov, stava je obvezna, spodnja meja je 1.\nVsak krog morate staviti. Srečno!\n'
    return tekst


def izpis_zmage(igra):
    tekst = lojtrice + 'Zmagali ste. Imate {0} žetonov'.format(igra.denar)
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + 'Izgubili ste.'
    return tekst

def izpis_igre(igra):
    tekst = lojtrice + ('''V roki imate {0} in vsota vrednosti vaših kart je {1},\ndealer ima v roki {2}.
    \nImate še {3} žetonov, stavili ste {4}.\n''').format(igra.roke, igra.doloci_vrednost_roke(igra.roke[0]), igra.dealer[:-1], igra.denar, igra.znesek)
    return tekst

def izpis_poslovila(igra):
    tekst = lojtrice + f'Začeli ste s 100 žetoni, sedaj jih imate {igra.denar}. Hvala da ste igrali pri nas.'
    return tekst

def izpis_poraz_runde(igra):
    tekst = lojtrice + 'Ta krog ste izgubili. V roki ste imeli {0},\ndealer pa {1}. Na računu imate še {2}.'.format(igra.roke, igra.dealer, igra.denar)
    tekst += '\n' + lojtrice
    return tekst

def izpis_zmage_runde(igra):
    tekst = lojtrice + 'Čestitamo, ta krog ste zmagali. V roki ste imeli {0},\ndealer pa {1}. Na računu imate sedaj {2}.'.format(igra.roke, igra.dealer, igra.denar)
    tekst += '\n' + lojtrice
    return tekst

def izpis_push(igra):
    tekst = lojtrice + 'Imate enako kot dealer. Denar se vam vrne.'
    return tekst


def trenutno_stanje(igra, roka):
    tekst = f'V roki imate {igra.roke}. Vrednost tega je {igra.doloci_vrednost_roke(roka)}\n' + '=' * len(lojtrice)
    return tekst

def igra_hit(igra, roka):
    vprasanje = input('Hit ali stand? ')
    while True:

        if vprasanje.lower() == 'stand':   

            break
        elif vprasanje.lower() == 'hit':
            igra.hit(roka)
            print(trenutno_stanje(igra, roka))
            if igra.doloci_vrednost_roke(roka) < 21:

                vprasanje = input('Hit ali stand? ')
            else:
                break
        else:
            vprasanje = input('Hit ali stand? ')


def pozeni_vmesnik():
    print(začetek())
    igra = model_blackjack.nova_igra()
    igra.deal(igra.roke[0])
    
    while True:  
        if igra.denar == 0:
            print(izpis_poraza(igra))
            print(izpis_poslovila(igra))
            break
        
        stava = input("Koliko stavite? ")
        for znak in stava:
            if znak not in [str(x) for x in range(10)]:
                stava = input("Prosim ponovno vpišite stavo.")
        
        if not igra.stava(int(stava)):
            stava = int(input("Lahko stavite manj, ali pritisnete enter za izhod. Koliko stavite? "))
        if igra.denar < 0:
            print(izpis_poraza(igra))
            break
        
        print(izpis_igre(igra))

        if igra.roka1[0].stevilo == igra.roka1[1].stevilo:
            split = input('Split? s tem tudi podvojite svojo stavo. ')
            if split.lower() == 'ja' or split.lower() == 'da':
                igra.split()
                print(izpis_igre(igra))
            else:
                pass
    
        for roka in igra.roke:
            if roka != []:
                print(f'Igrate roko {igra.roke.index(roka) + 1}')
                igra_hit(igra, roka)
            else:
                break
                
        print(izpis_igre(igra))
        
        for roka in igra.roke:
            if igra.doloci_vrednost_roke(roka) > 21:
                break
            for karta in roka:
                if karta.stevilo == 'A':
                    soft_hand = int(input('V roki imate asa. 1 ali 11>'))
                    if soft_hand == int(11):                            
                        igra.soft_hand(roka)
                        continue
                    else:
                        pass


        igra.dealers_play()
        igra.uredi_denar()
        konec = igra.preveri_konec()
        if konec == model_blackjack.PORAZ_RUNDE:
            print(izpis_poraz_runde(igra))
            if igra.denar == 0:
                print(izpis_poraza(igra))
                print(izpis_poslovila(igra))
                break
            odg = input('Ali želite igrati naprej? ')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            elif odg.lower() == 'ne':
                print(izpis_poslovila(igra))
                break
            else:
                odg = input('Ali želite igrati naprej? ')
                igra.reset()
        elif konec == model_blackjack.ZMAGA_RUNDE:
            print(izpis_zmage_runde(igra))
            odg = input('Ali želite igrati naprej? ')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            elif odg.lower() == 'ne':
                print(izpis_poslovila(igra))
                break
            else:
                odg = input('Ali želite igrati naprej? ')
                igra.reset()
        elif konec == model_blackjack.PUSH:
            print(izpis_push(igra))
            odg = input('Ali želite igrati naprej? ')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            elif odg.lower() == 'ne':
                print(izpis_poslovila(igra))
                break
            else:
                odg = input('Ali želite igrati naprej? ')
                igra.reset()
 
    return None

pozeni_vmesnik()

