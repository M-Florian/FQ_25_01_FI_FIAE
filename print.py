print("Hello World!")
name = "Florian"
print("Hallo " + name + "!") #Alter weg
print(f"Hallo {name}!") #moderner weg

#Wichtige Parameter der print()-Funktion:
## sep: Seperaor zwischen 2 Variablen innerhalb einer print funktion
## end: Ende einer print-funktion (Was soll nach dem print passieren)
nachname = "Nietmann"
print(name, nachname, sep="*****")
print("Hallo", end=" ")
print("Welt")

# Input() mit Print() im Zusammenspiel
name= input("Name: ")
print(f"Hallo {name}")