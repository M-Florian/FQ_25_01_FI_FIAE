# Variable vs Konstante
## keine konstanten in Python!
## ABER: Konvention - "Konstanten" werden IMMER groß geschrieben

PI = 3.14
MY_CONSTANT ="fsdfskdjf"


# Numerisch
#Dezimalsystem
x = 10
print("x:", x)

y = 1_000_000_000
print("y:", y)

z = x + y

print("Summe:", z)

# Binär
print("x(bin):", bin(x))

# hex
print("x(hex):", hex(x))

# octal
print("x(oct):", oct(x))

# String:

vorname = "Florian"
nachname = "Nietmann"

print(vorname + " " + nachname)
print(vorname, nachname)

x2 =str(x)
print("type(x):", type(x), "type(x2)", type(x2))

# Bool
wahre_aussage = True
falsche_aussage = False
print(type(wahre_aussage))

# None
none_database = None
print(type(none_database))

# ID

print(id(x), id(y))
print(id(x) - id(y))