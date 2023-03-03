# Les 8 - Opdracht 2
def mijn_functie_1(key):
    mijn_dictionary = {
        2 : 4,
        4 : 16,
        10 : 100,
        12 : 144
    }
    value = mijn_dictionary[key]
    return value

# Les 8 - Opdracht 3
def mijn_functie_2(key1, key2):
        global value1
        global value2
        global value3
        global value4       
        value1 = (key1 + key2)
        value2 = (key1 - key2)
        value3 = (key1 * key2)
        value4 = int((key1/key2))
        return [value1, value2, value3, value4]





    


