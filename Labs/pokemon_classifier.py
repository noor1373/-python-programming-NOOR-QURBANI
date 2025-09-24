import matplotlib.pyplot as plt
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
                length, width, pokemon_type = float(parts[0]), float(parts[1]), int(parts[2])
                
                if pokemon_type == 0: # 0 means Pichu
                    pichu_length.append(length)
                    pichu_width.append(width)
                else: # 1 means Pikachu
                    pikachu_length.append(length)
                    pikachu_width.append(width)
except:
    print("The file you want to read doesn't exist")


# https://www.w3schools.com/python/matplotlib_labels.asp
# plots a scatter graph of Pichu and Pikachu (data points)
plt.scatter(pichu_length, pichu_width, color="blue", label="Pichu")
plt.scatter(pikachu_length, pikachu_width, color="red", label="Pikachu")
plt.xlabel("Length")
plt.ylabel("Width")
plt.title("Pichu vs Pikachu")
plt.legend()
plt.show()

test_points = []

try:
    with open ("testpoints.txt", "r") as file:
        lines = file.readlines()
        for line in lines[1:]: # Skip first line

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


def classify_point(test_length, test_width):
    """Classify a point as Pichu or Pikachu based on nearest neighbor"""
    min_distance = float("inf") # start with a very large number
    closest_pokemon = "Unknown"

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

# Classify test points
print("\n--- Classification Results ---")
classifications = []
for point in test_points:
    length, width = point
    classification = classify_point(length, width)
    classifications.append(classification)
    print(f"Point ({length}, {width}) classified as {classification}")

# plots a scatter graph of Pichu and Pikachu (test points & data points)
# plot datapoints
plt.scatter(pichu_length, pichu_width, color="blue", label="Pichu (training)")
plt.scatter(pikachu_length, pikachu_width, color="red", label="Pikachu (training)")

# plot test points
for i, point in enumerate(test_points):
    length, width = point
    color = "green" if classifications[i] == "Pichu" else "orange"
    marker = "X" if classifications[i] == "Pichu" else "*" # * for Pikachu

    plt.scatter(length, width, color=color, marker=marker, edgecolors="black", s=100)

plt.scatter([], [], color="green", marker="X", s=100, label="Test Pichu", edgecolors="black")
plt.scatter([], [], color="orange", marker="*", s=100, label="Test Pikachu", edgecolors="black")
plt.xlabel("Length (cm)")
plt.ylabel("Width (cm)")
plt.title("Pichu vs Pikachu - Classification Results")
plt.legend()
plt.show()

print("\n--- Clasification Summary ---")
for i, point in enumerate(test_points, 1):
    length, width = point
    print(f"Test point {i}: ({length}, {width}) -> {classifications[i-1]}")

    

