def addiere(a=1, b=2):
    return a+b

def addiere(a, b):
    return a + b




ergebnis = addiere(1, 2)
print("Ergebnis:", ergebnis)

ergebnis_2 = addiere (a=2, b=3)
print("Ergebnis2:", ergebnis_2)

def verkette(str1, str2):
    verkettet = str1 + str2
    return verkettet

verketteter_string = verkette ("Hallo ", "Welt!")
print(verketteter_string)

## Exxkurs: Exception-Handling
dozent = verkette("Dozent#", 1)
print(dozent)

try:
    print("Wird immer ausgeführt, bis an Stelle, wo fehler auftritt")
    dozent = verkette("Dozent#", 1)
    print(dozent)
except Exception as e:
    print("Wird ausgeführt, wenn Fehler auftritt!")
    print("Fehler", e)
else:
    print("Wird nach 'try' ausgeführt, wenn kein Fehler aufgetreten ist!")
finally:
    print("Wird immer zusätzlich am Ende ausgeführt - egal ob Fehler oder nicht!")