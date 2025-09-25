import matplotlib.pyplot as plt
import math

pichu_length, pichu_width = [], []
pikachu_length, pikachu_width = [], []

# https://www.youtube.com/watch?v=BRrem1k3904
# open and read the data points file
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


test_points = []

# open and read the test points file
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
    x = length2 - length1
    y = width2 - width1
    distance = math.sqrt((x)**2 + (y)**2)
    return distance


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
print('\n--- Classification Results ---')
classifications = []
for point in test_points:
    length, width = point
    classification = classify_point(length, width)
    classifications.append(classification)
    print(f"Point ({length}, {width}) classified as {classification}")


# https://www.w3schools.com/python/matplotlib_labels.asp
# plots a scatter graph of Pichu and Pikachu (test points & data points)
plt.scatter(pichu_length, pichu_width, color="blue", label="Pichu (training)")
plt.scatter(pikachu_length, pikachu_width, color="red", label="Pikachu (training)")

# plot test points
for i, point in enumerate(test_points):
    length, width = point
    color = "green" if classifications[i] == "Pichu" else "orange"
    marker = "X" if classifications[i] == "Pichu" else "*" # * for Pikachu

    plt.scatter(length, width, color=color, marker=marker, edgecolors="black", s=100)

plt.scatter([], [], color="green", marker="X", label="Test Pichu", edgecolors="black")
plt.scatter([], [], color="orange", marker="*", label="Test Pikachu", edgecolors="black")
plt.xlabel("Length (cm)")
plt.ylabel("Width (cm)")
plt.title("Pichu vs Pikachu - Classification Results")
plt.legend()
plt.show()

# https://realpython.com/knn-python/#find-the-k-nearest-neighbors
# https://www.w3schools.com/python/python_ml_knn.asp
# https://www.digitalocean.com/community/tutorials/k-nearest-neighbors-knn-in-python?utm_source=chatgpt.com#the-idea-behind-k-nearest-neighbours-algorithm
# Get points from user with error handling
while True:
    user_input = input('\nEnter a point as ("length", "width") or "q" to exit: ')

    if user_input.lower() == "q":
        print("\nExiting the program...")
        break

    parts = user_input.split(",")
    if len(parts) != 2:
        print("Error: Please enter exactly two numbers separated by comma")
        continue

    try:
        test_length = float(parts[0].strip())
        test_width = float(parts[1].strip())

        if test_length < 0 or test_width < 0:
            print("Error: Use only positive numbers")
            continue

        # Classify point (task 1)
        result1 = classify_point(test_length, test_width)
        print(f"1 Nearest neighbors: {test_length}, {test_width} -> {result1}")


    except:
        print("Error: Please enter a valid numbers, e.g. 25, 32")


def classify_point_k_nearest(test_length, test_width, k=10): # k is number of neighbors
    """Classify a point as Pichu or Pikachu based on k nearest neighbors"""
    distances = []

    # Calculate distance to all Pichu
    for i in range(len(pichu_length)):
        distance = calculate_distance(test_length, test_width, pichu_length[i], pichu_width[i])
        distances.append((distance, "Pichu"))

    # Calculate distance to all Pikachu points
    for i in range(len(pikachu_length)):
        distance = calculate_distance(test_length, test_width, pikachu_length[i], pikachu_width[i])
        distances.append((distance, "Pikachu"))

    # sort the list by distance and get k nearest
    def get_distance(item):
        return item[0]
    
    distances.sort(key=get_distance)
    k_nearest = distances[:10]

    Pichu_votes = 0
    Pikachu_votes = 0

    for item in k_nearest:
        distance = item[0]
        pokemon_type = [1]

        if pokemon_type == "Pichu":
            Pichu_votes += 1
        else:
            Pikachu_votes += 1
    
    print("\nVotes: Pichu:", Pichu_votes, "Pikachu:", Pikachu_votes)


    if Pichu_votes > Pikachu_votes:
        return "Pichu"
    else:
        return "Pikachu"

print("\nTesting 10-nearest neighbors on test points:")

for i in range(len(test_points)):
    length, width = test_points[i]
    
    # 1-nearest neighbor
    result_1 = classify_point(length, width)
    
    # 10-nearest neighbors
    resultat_10 = classify_point_k_nearest(length, width)
    
    print("Point", (length, width))
    print("  1-nearest:", result_1)
    print("  10-nearest:", resultat_10)
    print()