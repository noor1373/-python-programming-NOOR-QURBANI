import matplotlib.pyplot as plt

pichu_length = []
pichu_width = []
pikachu_length = []
pikachu_width = []

file = open ("datapoints.txt")
first_line = file.readline() # Skip the header (first line)

for line in file:
   remove_space = line.strip()
   parts = remove_space.split(", ")

   width = float(parts[0])
   length = float(parts[1])
   pokemon_type = int(parts[2])

   if pokemon_type == 0: # 0 means Pichu
      pichu_length.append(length)
      pichu_width.append(width)
   elif pokemon_type == 1: # mens Pikachu
      pikachu_length.append(length)
      pikachu_width.append(width)

      
      


print("Pichu lengths:", pichu_length, pichu_width)
print("Pikachu lengths:", pikachu_length, pikachu_width)
        
        

