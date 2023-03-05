def decoreer(tekst=""):
    tekst = "header"
    lengte = len(tekst) + 4
    print ()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def onderstreep(tekst = ""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=") 
    return uit

def som(mijn_dictionary):
    totaal = sum(mijn_dictionary.values())
    return totaal

