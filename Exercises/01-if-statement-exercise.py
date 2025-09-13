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
