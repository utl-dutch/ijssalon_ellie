from helper import som

def presenteer(mijn_dictionary, totaal):
    for k,v in mijn_dictionary.items():
            print (k + " : " + str(v)  + " euro")
    print (25 * "=")
    print (f"totaal = {totaal} euro")
    return
