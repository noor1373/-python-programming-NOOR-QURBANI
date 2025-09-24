import matplotlib.pyplot as plt
import numpy as np
import math

pichu_length, pichu_width = [], []
pikachu_length, pikachu_width = [], []

# https://www.youtube.com/watch?v=BRrem1k3904
# open and read the file
try:
    with open ("datapoints.txt") as file:
        
        for line in file:
            clear_line = line.strip()
            if not clear_line:
                continue
            parts = clear_line.split(", ")

            if len(parts) == 3:    
                length = float(parts[0])
                width = float(parts[1])
                pokemon_type = int(parts[2])

                if pokemon_type == 0: # 0 means Pichu
                    pichu_length.append(length)
                    pichu_width.append(width)
                else: # 1 means Pikachu
                    pikachu_length.append(length)
                    pikachu_width.append(width)
except:
    print("The file you want to read doesn't exist")


# https://www.w3schools.com/python/matplotlib_labels.asp
# plots a scatter graph of Pichu and Pikachu
plt.scatter(pichu_length, pichu_width, color="blue", label="Pichu")
plt.scatter(pikachu_length, pikachu_width, color="red", label="Pikachu")
plt.xlabel("Length")
plt.ylabel("Width")
plt.title("Pichu vs Pikachu")
plt.legend()
plt.show()

test_points = []
first_line = True

try:
    with open ("testpoints.txt", "r") as file:

        for line in file:
            if first_line:
                first_line = False
                continue
            # Remove numbering and parentheses
            if line.strip():
                clear_line = line.split(". ", 1)[-1].strip()
                clear_line = clear_line.replace("(", "").replace(")", "")

                length, width = clear_line.split(", ")
                test_points.append((float(length), float(width)))

except:
    print("The file you want to read doesn't exist")


def calculate_distance(length1, width1, length2, width2):
    """Calculate distance between two points using pythagorean theorem"""
    return math.sqrt((length2 - length1)**2 + (width2 - width1)**2)


def classify_points(test_length, test_width):
    """Classify a point as Pichu or Pikachu based on nearest neighbor"""
    min_distance = float("inf") # start with a very large number
    closest_pokemon = "Unkown"

    # Check all Pichu and Pikachu points
    for i in range(len(pichu_length)):
        distance = calculate_distance(test_length, test_width, pichu_length[i], pichu_width[i])

        if distance < min_distance:
            min_distance = distance
            closest_pokemon = "Pichu"
    
    for i in range(len(pikachu_length)):
        distance = calculate_distance(test_length, test_width,pikachu_length[i], pikachu_width[i])

        if distance < min_distance:
            min_distance = distance
            closest_pokemon = "Pikachu"

    return closest_pokemon



    


    

