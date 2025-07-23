# def factorial(n):
#   if n<=1:
#     return 1
#   else:
#     return n*factorial(n-1)
  
# n=int(input("Enter a number"))
# print(factorial(n))
# module inbuilt userdefined,3rd party modular,user defined module
# package ,library

# def rotate_left(arr, d):
#     n = len(arr)
#     d = d % n  # Just in case d is larger than the list length

#     rotated = []

#     # First, add elements starting from d to the end
#     i = d
#     while i < n:
#         rotated.append(arr[i])
#         i += 1

#     # Then, add the first d elements
#     j = 0
#     while j < d:
#         rotated.append(arr[j])
#         j += 1

#     return rotated



# # Try it out
# arr = [1, 2, 3, 4, 5]
# steps = 2
# print(rotate_left(arr, steps))
def left_rotations(s):
    n = len(s)
    rotations = []
    for i in range(n):
        rotated = ""
        for j in range(n):
            rotated += s[(i + j) % n]
        rotations.append(rotated)
    return rotations

# Example usage
s = "abcd"
for rotation in left_rotations(s):
    print(rotation)
