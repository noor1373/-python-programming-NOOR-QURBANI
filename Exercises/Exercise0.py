# Vi börjar med att importera math-biblioteket för att kunna räkna kvadratrötter
import math

# 1. Pythagoras sats
# a) Beräkna hypotenusan med hjälp av Pythagoras sats 
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(f"Längden på hypotenusan är {c}.")


# b) Beräkna den saknade kateten
c = 7.0
a = 5.0
b = math.sqrt(c**2 - a**2)

# Avrunda till 1 decimal
print(f"Längden på den andra kateten är {round (b,1)}.")


# 2. Klassificeringsnoggrannhet
correct_prognos = 300
total_prognos = 365
# Räknar noggrannheten 
accuracy = correct_prognos / total_prognos
# Avrunda till 2 decimaler
print(f"noggrannheten är: {round(accuracy, 2)}.")


# 3. Modell för att upptäcka brand
true_positive = 2
false_positive = 2
false_negative = 11
true_negative = 985
accuracy = (true_positive + true_negative) / (true_negative + true_positive + false_negative + false_positive)
print(f"Modellens noggrannhet är: {round(accuracy, 3)}.")


# 4. Linjens ekvation
# Punkterna A(4,4) och B(0,1)
x1 = 4
y1 = 4
x2 = 0
y2 = 1
# Räkna lutningen
k = (y2 - y1) / (x2  - x1)
m = y1 - k * x1
print(f"Linjens ekvation är: y = {k}x + {m}.")


# 5. Avstånd mellan två punkter i 2D
# P1 = (3,5) och P2 = (-2,4)
x1 = 3
y1 = 5
x2 = -2
y2 = 4
# Räkna avtåndet mellan två punkter
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Avståndet är {round(distance, 2)} längdenheter.")


# 6. Euklidiskt avstånd i 3D
# P1 = (2,1,4) och P2 = (3,1,0)
x1 = 2
y1 = 1
z1 = 4
x2 = 3
y2 = 1
z2 = 0
# Räkna avstånd mellan tre punkter
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
print(f"Avståndet i 3D är {round(distance, 2)}")
