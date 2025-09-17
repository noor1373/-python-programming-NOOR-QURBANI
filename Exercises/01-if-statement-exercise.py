# 1. Check sign
tal = float(input("Ange ett tal: "))

# Kontrollera om talet är positivt, negativt eller noll
if tal > 0:
    print("Talet är positivt. ")
elif tal < 0:
    print("Talet är negativt. ")
else:
    print("Talet är noll. ")


# 2. Smallest
tal1 = float(input("Ange det första talet: "))
tal2 = float(input("Ange det andra talet: "))

# Jämför och skriv ut det minsta talet
if tal1 > tal2:
   print(f"Det minsta talet är {tal2}")
elif tal2 > tal1:
    print(f"Det minsta talet är {tal1}")
else:
    print("Talen är lika stora.")


# 3. Right angle
vinkel1 = float(input("Ange vinkel 1: "))
vinkel2 = float(input("Ange vinkel 2: "))
vinkel3 = float(input("Ange vinkel 3: "))

# Kolla om vinklarna är giltiga
if vinkel1 <= 0 or vinkel2 <= 0 or vinkel3 <=0:
    print("En vinkel måste vara större än 0. ")
elif vinkel1 + vinkel2 + vinkel3 != 180:
    print("Summan av vinklar måste vara 180. ")
else:
    if 90 in (vinkel1, vinkel2, vinkel3):
        print("Triangeln är rättvinklig. ")
    else:
        print("Triangeln är inte rättvinklig. ")


# 4. Medicine
age = int(input("Ange ålder i år. "))
weight = float(input("Ange vikt i kg. "))

# Kontrollera vikt och visa rekommenderad tabllet intag.
if weight > 40:
    print("Rekommenderad dos: 1 - 2 tabletter. ")
elif 26 <= weight <= 40:
    print("Rekommenderad dos: 1/2 - 1 tablett. ")
elif 15 <= weight <= 25:
    print("Rekommenderad dos: 1/2 tablett. ")
else:
    print("Ej rekommenderad dos.")

# 5. Divisible
tal = int(input("Ange ett heltal: "))

# Kontrollera om talen är jämnt eller udda
if tal % 2 == 0:
    print("Talet är jämnt. ")
else:
    print("Talet är udda. ")

# Kontrollera om talet är delar med 5
if tal % 5 == 0:
    print("Talet är delbar med 5. ")
else:
    print("Talet är inte delbar med 5. ")

# Kontrollera om talet är delbar med 5 och udda.
if tal % 5 == 0 and tal % 2 != 0:
    print("Talet är både delabar med 5 och udda. ")

# 6. Luggage size
# Kontrollera mått och vikt på väskan
weight = float(input("Ange vikt på handbagagen i kg. "))
length = float(input("Ange längd i cm: "))
width = float(input("Ange bredd i cm: "))
height = float(input("Ange höjd i cm: "))
if weight <= 8 and length <= 55 and width <= 40 and height <= 23:
    print("Väskan är godkänd som handbagage. ")
else:
    print("Väskan är för stor eller för tung. ")

name = input("Vad heter du? ")
while name == "":
    print("Du har inte anget ditt namn. ")
    name = input("Vad heter du? ")

print(f"Hej {name} ")