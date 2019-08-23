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
    {2} \n imate še {3} žetonov.''').format(igra.roka1, igra.doloci_vrednost_roke(igra.roka1), igra.dealer[:-1], model_blackjack.DENAR)
    return tekst

def izpis_poslovila(igra):
    tekst = 'Hvala da ste igrali pri nas.'
    return tekst

def izpis_poraz_runde(igra):
    tekst = 'Ta krog ste izgubili, na računu imate še {0}.'.format(model_blackjack.DENAR)
    return tekst

def izpis_zmage_runde(igra):
    tekst = 'Čestitamo, ta krog ste zmagali. Na računu imate sedaj {0}.'.format(model_blackjack.DENAR)
    return tekst

def pozeni_vmesnik():
    
    stava = int( input("Koliko stavite?"))
    
    igra.stava(stava)    
    igra.deal()

    while True:
        
        print(izpis_igre(igra))
    
    
        poteza = input("hit ali stand?")
        while poteza == 'hit':
            igra.hit(igra.roka1)
            if igra.konec_igre() == model_blackjack.PORAZ_RUNDE:
                print(izpis_poraz_runde(igra))
                odg = input('Ali želite igrati naprej?')
                if odg.lower() == 'ja' or odg.lower() == 'da':
                    igra.reset()
                    igra.deal()
                    continue
                else:
                    print(izpis_poslovila(igra))
                    break
            print(f'V roki imate {igra.roka1} in vrednost tega je {igra.doloci_vrednost_roke(igra.roka1)}')
            poteza = input("hit ali stand?")

        if poteza == 'stand':
            pass
        

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
                continue
            else:
                print(izpis_poslovila(igra))
                break
        elif igra.konec_igre() == model_blackjack.ZMAGA_RUNDE:
            print(izpis_zmage_runde(igra))
            odg = input('Ali želite igrati naprej?')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
                igra.deal()
                continue
            else:
                print(izpis_poslovila(igra))
                break
        igra.dealers_play()
        print('Delim novo rundo.')
    return None


pozeni_vmesnik()

