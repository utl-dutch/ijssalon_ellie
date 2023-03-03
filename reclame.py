from algemene_functies import mijn_functie_2

# Les 8 - Opdracht 5
def aanbieding_1(smaak, prijs, korting):
    global text_1
    kortingbedrag = prijs * korting
    tebetalenbedrag = prijs - kortingbedrag
    text_1 = f"Vandaag in de aanbieding: emmertje ijs ( 1 liter) in de smaak {smaak},\
van {prijs} euro voor {tebetalenbedrag:.2f} euro."
    return text_1

# Les 8 - Opdracht 7
def inkomsten_totaal(inkomsten, btw):
   global totaal
   totaal = sum(inkomsten)
   global btwbedrag
   btwbedrag = totaal * btw
   return totaal, btwbedrag

# Les 8 - Opdracht 8
def laag_en_hoog(mijn_lijst):
    global hoogste
    hoogste = max(mijn_lijst)
    global laagste
    laagste = min(mijn_lijst)
    global gevonden
    gevonden = []
    gevonden.append(hoogste)
    gevonden.append(laagste)
    return gevonden

# Les 8 - Opdracht 10
def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal2 = 0
    for i in mijn_lijst:
        totaal2 += i
    global gemiddeld
    gemiddeld = str(int(totaal2/aantal))
    return gemiddeld
    
# Les 8 - Opdracht 11
def meervoudig(invoer_lijst):
    laag_en_hoog(invoer_lijst)
    return gevonden

# Les 8 - Opdracht 12
def combinatie(invoer_lijst_2):
    meervoudig(invoer_lijst_2)
    korte_lijst = gevonden
    mijn_functie_2(korte_lijst)

getallen = [10,5,3,2,1,2,9]
combinatie(getallen)