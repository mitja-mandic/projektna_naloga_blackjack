import model_blackjack
lojtrice = "######################################\n"





def izpis_zmage(igra):
    tekst = lojtrice + 'Zmagali ste. Imate {0} žetonov'.format(model_blackjack.DENAR)
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + 'Izgubili ste. Dealer je imel v roki {0}, vi pa {1} Več sreče prihodnjič!'.format(igra.dealer, igra.roke)
    return tekst

def izpis_igre(igra):
    tekst = lojtrice + ('''V roki imate {0} in vsota vrednosti vaših kart je {1} \ndealer ima v roki 
    {2} \n imate še {3} žetonov, stavili ste {4}.''').format(igra.roke, igra.doloci_vrednost_roke(igra.roke[0]), igra.dealer[:-1], model_blackjack.DENAR, igra.znesek)
    return tekst

def izpis_poslovila(igra):
    tekst = lojtrice + 'Hvala da ste igrali pri nas.'
    return tekst

def izpis_poraz_runde(igra):
    tekst =lojtrice + 'Ta krog ste izgubili. V roki ste imeli {0},\ndealer pa {1}. Na računu imate še {2}.'.format(igra.roke, igra.dealer, model_blackjack.DENAR)
    return tekst

def izpis_zmage_runde(igra):
    tekst = lojtrice + 'Čestitamo, ta krog ste zmagali. V roki ste imeli {0},\ndealer pa {1}. Na računu imate sedaj {2}.'.format(igra.roke, igra.dealer, model_blackjack.DENAR)
    return tekst

def trenutno_stanje(igra):
    tekst = lojtrice + f'V roki imate {igra.roke}.'
    return tekst

def pozeni_vmesnik():
    igra = model_blackjack.nova_igra()
    igra.deal(igra.roke[0])
    while True:
        
        stava = int(input("Koliko stavite?"))
        if not igra.stava(stava):
            print('Nimate toliko denarja.')
            break
        if model_blackjack.DENAR < 0:
            print(izpis_poraza(igra))
            break
        
        print(izpis_igre(igra))

        if igra.roka1[0].stevilo == igra.roka1[1].stevilo:
            split = input('split? s tem tudi podvojite svojo stavo.')
            if split == 'ja':
                igra.split()
            else:
                pass
        print(izpis_igre(igra))

        poteza = input("hit ali stand?")
        
        if poteza == 'hit':
            i = 0
            while poteza == 'hit':
                igra.hit(igra.roke[i])
                #print(trenutno_stanje(igra))
                if igra.doloci_vrednost_roke(igra.roke[i]) < 21:
                    print(f'V roki imate {igra.roke} in vrednost tega je {igra.doloci_vrednost_roke(igra.roke[i])}')
                    poteza = input("hit ali stand?")
                if poteza == 'stand':
                    print('sedaj igrate še za drugo roko.')
                    if igra.roke[1] != [] and i < 1:
                        i += 1
                        poteza = input('hit ali stand?')
                    else:
                        break
                elif igra.doloci_vrednost_roke(igra.roke[i]) == 21:
                    break
                elif igra.doloci_vrednost_roke(igra.roke[i]) > 21:
                    break
                
                
                
                
                
            #    if poteza == 'stand':
            #        if igra.roke[1] != []:
            #            i += 1
            #            continue
            #        else:
            #            break
                

        
        
        
        
        
        #for roka in igra.roke:
        #    if roka != []:
        #        while poteza == 'hit':
        #            igra.hit(roka)
        #            if igra.doloci_vrednost_roke(roka) < 21:
        #                print(f'V roki imate {igra.roke} in vrednost tega je {igra.doloci_vrednost_roke(roka)}')
        #                poteza = input("hit ali stand?")
        #            if poteza == 'stand':
        #                break
        #            elif igra.doloci_vrednost_roke(roka) == 21:
        #                break
        #            elif igra.doloci_vrednost_roke(roka) > 21:
        #                break
        #    else:
        #        break

        if poteza == 'stand':
            pass
        print(izpis_igre(igra))
        
        for roka in igra.roke:
            for karta in roka:
                if karta.stevilo == 'A':
                    soft_hand = int(input('V roki imate asa. 1 ali 11>'))
                    if soft_hand == int(11):                            
                        igra.soft_hand(roka)
                        #print(trenutno_stanje(igra))
                        continue
                    else:
                        pass


        igra.dealers_play()



        if model_blackjack.DENAR == 0:
            print(igra.roka1)
            print(izpis_poslovila(igra))
            print(izpis_poraza(igra))
            break
        #elif igra.preveri_konec() == model_blackjack.ZMAGA:
        #    print(izpis_zmage(igra))
        #    print(izpis_poslovila(igra))
        #    break
        
        elif igra.preveri_konec() == model_blackjack.PORAZ_RUNDE:
            print(izpis_poraz_runde(igra))
            odg = input('Ali želite igrati naprej?')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            else:
                print(izpis_poslovila(igra))
                break
        elif igra.preveri_konec() == model_blackjack.ZMAGA_RUNDE:
            print(izpis_zmage_runde(igra))
            odg = input('Ali želite igrati naprej?')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            else:
                print(izpis_poslovila(igra))
                break
        elif igra.preveri_konec() == model_blackjack.PUSH:
            print('Imate enako kot dealer, denar se vam vrne.')
            odg = input('Ali želite igrati naprej?')
            if odg.lower() == 'ja' or odg.lower() == 'da':
                igra.reset()
            else:
                print(izpis_poslovila(igra))
                break
    return None

pozeni_vmesnik()

