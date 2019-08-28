import model_blackjack
lojtrice = "######################################\n"

igra = model_blackjack.nova_igra()



def izpis_zmage(igra):
    tekst = lojtrice + 'Zmagali ste. Imate {0} žetonov'.format(model_blackjack.DENAR)
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + 'Izgubili ste. Dealer ima je imel v roki {0}, vi pa {1} Več sreče prihodnjič!'.format(igra.dealer, igra.roka1)
    return tekst

def izpis_igre(igra):
    tekst = lojtrice + ('''V roki imate {0} in vsota vrednosti vaših kart je {1} \ndealer ima v roki 
    {2} \n imate še {3} žetonov, stavili ste {4}.''').format(igra.roka1, igra.doloci_vrednost_roke(igra.roka1), igra.dealer[:-1], model_blackjack.DENAR, igra.znesek)
    return tekst

def izpis_poslovila(igra):
    tekst = lojtrice + 'Hvala da ste igrali pri nas.'
    return tekst

def izpis_poraz_runde(igra):
    tekst =lojtrice + 'Ta krog ste izgubili. V roki ste imeli {0},\ndealer pa {1}. Na računu imate še {2}.'.format(igra.roka1, igra.dealer, model_blackjack.DENAR)
    return tekst

def izpis_zmage_runde(igra):
    tekst = lojtrice + 'Čestitamo, ta krog ste zmagali. V roki ste imeli {0},\ndealer pa {1}. Na računu imate sedaj {2}.'.format(igra.roka1, igra.dealer, model_blackjack.DENAR)
    return tekst

def trenutno_stanje(igra):
    tekst = lojtrice + f'V roki imate {igra.roka1}.'
    return tekst

def pozeni_vmesnik():
    
        
    igra.deal()

    while True:
        stava = int(input("Koliko stavite?"))
    
        if not igra.stava(stava):
            print('Nimate toliko denarja.')
            break
        
        if model_blackjack.DENAR <= 0:
            print(izpis_poraza)
            break
        
        print(izpis_igre(igra))

        for karta in igra.roka1:
                if karta.stevilo == 'A':
                    soft_hand = int(input('1 ali 11?>'))
                    if soft_hand == int(11):
                        igra.soft_hand()
                        print('******soft hand')
                        continue
                    else:
                        pass
        
        print(izpis_igre(igra))

        poteza = input("hit ali stand?")
        if poteza == 'hit':
            while poteza == 'hit':
                igra.hit(igra.roka1)
                i = 3
                #print(trenutno_stanje(igra))
                for karta in igra.roka1[i:]:
                    if karta.stevilo == 'A':
                        soft_hand = int(input('1 ali 11>'))
                        if soft_hand == int(11):                            
                            igra.soft_hand()
                            #print(trenutno_stanje(igra))
                            continue
                        else:
                            pass
                    i+=1
                if igra.doloci_vrednost_roke(igra.roka1) < 21:
                    print(f'V roki imate {igra.roka1} in vrednost tega je {igra.doloci_vrednost_roke(igra.roka1)}')
                    poteza = input("hit ali stand?")
                    if poteza == 'stand':
                        break
                if igra.doloci_vrednost_roke(igra.roka1) == 21:
                    break

                elif igra.doloci_vrednost_roke(igra.roka1) > 21:
                    break

        elif poteza == 'stand':
            pass
        else:
            break
        
        igra.dealers_play()
        
        #print(izpis_igre(igra))
        
        if igra.konec_igre() == model_blackjack.PORAZ:
            print(igra.roka1)
            print(izpis_poslovila(igra))
            print(izpis_poraza(igra))
            break
        
        elif igra.konec_igre() == model_blackjack.ZMAGA:
            print(izpis_zmage(igra))
            print(izpis_poslovila(igra))
            break
        
        elif igra.konec_igre() == model_blackjack.PORAZ_RUNDE:
            print(izpis_poraz_runde(igra))
            odg = input('Ali želite igrati naprej?')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
                igra.deal()
            else:
                print(izpis_poslovila(igra))
                break
        elif igra.konec_igre() == model_blackjack.ZMAGA_RUNDE:
            print(izpis_zmage_runde(igra))
            odg = input('Ali želite igrati naprej?')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
                igra.deal()
            else:
                print(izpis_poslovila(igra))
                break
    return None

pozeni_vmesnik()

