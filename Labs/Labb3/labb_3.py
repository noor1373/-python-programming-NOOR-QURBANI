import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


try:
    data = pd.read_csv("unlabelled_data.csv", header=None, names=["x", "y"])
    print("File 'unlabelled_data.csv' loaded successfully!\n")
except:
    print("Error: Could not load 'unlabelled_data.csv'")
    exit()

k = -2
m = 0

def classify_point(x, y, k, m):
    line_y = k * x + m
    if y > line_y:
        return 1
    else:
        return 0
    

classes = [] # create an empty list to store each point's class (0 or 1)

for i in range(len(data)):
    x_value = data["x"][i]
    y_value = data["y"][i]
    point_class = classify_point(x_value, y_value, k, m)
    classes.append(point_class)

data["class"] = classes

# save the classified data to a new CSV file
data.to_csv("labelled_data.csv", index=False)

# Plot final result with colors
plt.figure(figsize=(10, 6))
colors = ["blue" if c == 0 else "red" for c in data["class"]]

x_line = np.linspace(data["x"].min(), data["x"].max(), 100)
y_line = [k * x + m for x in x_line]

plt.scatter(data["x"], data["y"], c=colors, alpha=0.6, label= "Data points")
plt.plot(x_line, y_line, color="black", linewidth=2, label=f"y = {k}x + {m}")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Classification of Points")
plt.legend()
plt.show()