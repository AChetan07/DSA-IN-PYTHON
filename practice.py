import numpy as np

# Step 1: Read the dimensions of the array
n, m = input().split()
n = int(n)  # number of rows
m = int(m)  # number of columns

# Step 2: Create an empty list to store the rows
data = []

# Step 3: Read each row of the matrix
for i in range(n):
    row = input().split()            # Take input and split it into a list
    row = [int(x) for x in row]      # Convert each element to integer
    data.append(row)                 # Add the row to the data list

# Step 4: Convert the list of lists into a NumPy array
array = np.array(data)

# Step 5: Find the minimum value in each row
min_values = []
for row in array:
    min_value = min(row)
    min_values.append(min_value)

# Step 6: Find the maximum among the minimum values
result = max(min_values)

# Step 7: Print the result
print(result)