import model_blackjack
lojtrice = "######################################\n"

def izpis_zmage(igra):

    tekst = lojtrice + 'Zmagali ste. Imate {0} žetonov'.format(model_blackjack.DENAR)
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + 'Izgubili ste. Več sreče prihodnjič!'
    return tekst

def izpis_igre(igra):
    tekst = lojtrice + ('''V roki imate {0} in vsota vrednosti vaših kart je {1} \ndealer ima v roki 
    {2} \n imate še {3}''').format(igra.roka1, igra.doloci_vrednost_roke(igra.roka1), igra.dealer, model_blackjack.DENAR)
    return tekst

def pozeni_vmesnik():
    
    igra = model_blackjack.Igra()
    
    stava = int( input("Koliko stavite?"))
    
    igra.stava(stava)    
    igra.deal()

    while True:
        
        print(izpis_igre(igra))
        igra.dealers_play()
        poteza = input("hit ali stand?: ")
        if poteza == 'hit':
            igra.hit(igra.roka1)
        elif poteza == 'stand':
            pass

        if igra.konec_igre() == model_blackjack.PORAZ:
            print(igra.roka1)
            print(izpis_poraza(igra))
            break
        elif igra.konec_igre() == model_blackjack.ZMAGA:
            print(izpis_zmage(igra))
            break
        else:
            pass

        nova_stava = int(input("Ali povečujete stavo? Vpišite koliko želite staviti, če ne želite, vpišite 0. "))
        if nova_stava == 0:
            pass
        else:
            igra.stava(nova_stava)
    return None


pozeni_vmesnik()
