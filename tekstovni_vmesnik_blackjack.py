import model_blackjack
lojtrice = "######################################\n"



def začetek():
    tekst = lojtrice + 'Pozdravljeni! Začenjate igro blackjacka. Imate 100 žetonov, stava je obvezna, ni pa spodnje meje.\nVsak krog morate staviti. Srečno!\n'
    return tekst


def izpis_zmage(igra):
    tekst = lojtrice + 'Zmagali ste. Imate {0} žetonov'.format(model_blackjack.DENAR)
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + 'Izgubili ste. Dealer je imel v roki {0}, vi pa {1} Več sreče prihodnjič!'.format(igra.dealer, igra.roke)
    return tekst

def izpis_igre(igra):
    tekst = lojtrice + ('''V roki imate {0} in vsota vrednosti vaših kart je {1},\ndealer ima v roki {2}.
    \nImate še {3} žetonov, stavili ste {4}.\n''').format(igra.roke, igra.doloci_vrednost_roke(igra.roke[0]), igra.dealer[:-1], model_blackjack.DENAR, igra.znesek)
    return tekst

def izpis_poslovila(igra):
    tekst = lojtrice + f'Začeli ste s 100 žetoni, sedaj jih imate {model_blackjack.DENAR}. Hvala da ste igrali pri nas.'
    return tekst

def izpis_poraz_runde(igra):
    tekst = lojtrice + 'Ta krog ste izgubili. V roki ste imeli {0},\ndealer pa {1}. Na računu imate še {2}.'.format(igra.roke, igra.dealer, model_blackjack.DENAR)
    tekst += '\n' + lojtrice
    return tekst

def izpis_zmage_runde(igra):
    tekst = lojtrice + 'Čestitamo, ta krog ste zmagali. V roki ste imeli {0},\ndealer pa {1}. Na računu imate sedaj {2}.'.format(igra.roke, igra.dealer, model_blackjack.DENAR)
    tekst += '\n' + lojtrice
    return tekst

def izpis_push(igra):
    tekst = lojtrice + 'Imate enako kot dealer. Denar se vam vrne.'
    return tekst


def trenutno_stanje(igra, roka):
    tekst = lojtrice + f'V roki imate {igra.roke}. Vrednost tega je {igra.doloci_vrednost_roke(roka)}'
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
        stava = input("Koliko stavite? ")
        for znak in stava:
            if znak not in [str(x) for x in range(10)]:
                stava = input("Prosim ponovno vpišite stavo.")
        
        if not igra.stava(int(stava)):
            print('Nimate toliko denarja.')
            stava = int(input("Lahko stavite manj, ali pritisnete enter za izhod. Koliko stavite? "))
        if model_blackjack.DENAR < 0:
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
            i = 0
            if roka != []:
                if i == 1:
                    print('Sedaj igrate še drugo roko.')
                i+= 1
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

        if model_blackjack.DENAR == 0:
            print(izpis_poraza(igra))
            print(izpis_poslovila(igra))
            break
        
        elif igra.preveri_konec() == model_blackjack.PORAZ_RUNDE:
            print(izpis_poraz_runde(igra))
            odg = input('Ali želite igrati naprej? ')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            elif odg.lower() == 'ne':
                print(izpis_poslovila(igra))
                break
            else:
                odg = input('Ali želite igrati naprej? ')
        elif igra.preveri_konec() == model_blackjack.ZMAGA_RUNDE:
            print(izpis_zmage_runde(igra))
            odg = input('Ali želite igrati naprej? ')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            elif odg.lower() == 'ne':
                print(izpis_poslovila(igra))
                break
            else:
                odg = input('Ali želite igrati naprej? ')
        elif igra.preveri_konec() == model_blackjack.PUSH:
            print(izpis_push(igra))
            odg = input('Ali želite igrati naprej? ')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            elif odg.lower() == 'ne':
                print(izpis_poslovila(igra))
                break
            else:
                odg = input('Ali želite igrati naprej? ')
    return None

pozeni_vmesnik()

