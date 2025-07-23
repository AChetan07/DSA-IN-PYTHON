

# code for getting an input from as user the first name and last name and removing the last two characters from the first name and second and printing them and reversing the name and orinting
# def nick(firstname, lastname):
#         if firstname!='' and lastname!=' ':
#             if len(firstname)<1 and len(lastname)<1: 
#                 if 
#                         print("name cannot be containing empty characters,numbers,specialcharacters,")

#         nickname = firstname[-2:] + lastname[:2]
#         print (nickname)
    

# first = input(" first name: ")
# last = input(" last name: ")
# nickname =nick(first, last)
# print("Your nickname is:", nickname)


import random


n= random.randint(1,1000)
ch=5;
while ch>0:

          ui=int(input("Enter an integer from 1 to 1000:"))
          ch-=1
          if ui==n:
                  print("yes correct")
                  break
          else:
                  print(f"Wrong guess no of tries left is {ch}")
        
        
          if ch==0:
                   print(f"The number was {n}")        



import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)

print(np.max(np.min(arr, axis=1)))
# a = [1, 2, 3, 4, 5, 6]

# # Integer division to find the middle index
# mid = len(a) // 2

# # Elements from the start to the middle


# # Elements from the middle to the end
# y= a[mid:]

# print(x)
# print(y)


