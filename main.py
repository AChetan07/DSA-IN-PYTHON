# # def TwoSum(arr,key):
# #     first=second=-1
# #     store={}
# #     for i in range(len(arr)):
# #         remainder= key-arr[i]
# #         if remainder  in store.keys():
# #             return[store[remainder],i]
# #         store[arr[i]]=i
# #     return[-1,-1]
# # print (TwoSum([10,2,3,4,5,6],14))        


# # def frequency(value):
# #      res={char:value.count(char) for char in value}
    
# #      for x in res:
# #           print(f"{x}={res[x]},",end="")
     
    


# # frequency("abocbfikbif")
          

# # def anagram(val1,val2):
# #         # if sorted(val1)==sorted(val2):
# #         #         print(f"{val1} and {val2} are anagrams")
# #         # else:
# #         #         print(f"{val1} and {val2} are not anagrams")

# #         counter={}
# #         for char in val1:
# #                 counter[char]=counter.get(char,0)+1
# #         for char in  val2:
# #                 if counter.get(char,0)==0:
# #                         return False
# #                 return True

# # val1=input("word1:")
# # val2=input("word2:")
# # anagram(val1,val2)
# # def FirstNonOccur(value):
# #     res={}
# #     res={char:value.count(char) for char in value}
# #     print(res)
# #     for char in value:
# #          occur[char]=occur.get(char,0)+1
# #          print(char)


# # FirstNonOccur("true")
 



# def parkingslot(lot):
#         maxcount=count=0
#         for car in lot:
#                 if car =="x":
#                         maxcount=max(maxcount,0)
#                         count=0
#                 else:
#                         count+=1
#                 return maxcount
# print(parkingslot("xsxsxssxsxsx"))
    

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def create():
#     new=Node


#   slow and fast pointers
# def findcycle(head):
#     slow=fast=head
#     while slow and fast:
#         slow=slow.next
#         fast=fast.next.next
#         if slow==fast:
#             break
#     slow=head

#     while slow!=fast and slow and fast:
#         slow=slow.next
#         fast=fast.next.next
#     return slow==fast
#     head=create()

# print(findcycle(head))

# to find dupicates ina list consisting of elements

# def findDuplicate(arr):
#     slow=fast=arr[0] # start slow and fast at the same point
#     while True:
#         slow=arr[slow]# slow moves at 1x
#         fast= arr[arr[fast]] # fast moves at 2x
#         if slow==fast: # when they interact the found a cycle
#             break
#     slow=arr[0]
#     while slow!=fast: #veryify the cycle until they meet
#         slow=arr[slow] #move both util they meet at 1x
#         fast=arr[fast]
#     return slow # slow always points at begining of the cycle
# # which means the duplicate number is the cycles joint

# print (findDuplicateind([1,3,2,3,2,2]))              

# print(ascii('x')) function to print ascii value of character




# write a program to split to two equal halves and find sum of each half check whether both half are equal or not if equal check if its prime  and odd or even
# l=[2,5,0,1,4,2]
# mid=len(l)//2
# a=l[:mid]
# b=l[mid:]
# def prime(n):
#       if n%2==0:
#            return False
#       if n<=1:
#            return  False
#       if n==2:
#            return True
      
#       for i in range(3,n,2):
#            if n%i==0:
#                 return False
#            return True

# print(f"The first half of list {a}")
# print(f"The second half of list {b}")
# x=sum(a)
# y=sum(b)

# if x==y:
#         if x%2==0:
#               print("sum is even")
#         else:
#               print("sum is odd")
#               print(f" prime number:{prime(x)}")
# else:
#       print("Not equal")
    
    
#             l=[1,2,3,4]
# n=int (input())
#        print(l[n:]+l[:n])            
#    for i in range(N):
#       rv=l.pop()
#       l.insert(0,rv)
# patterns
# 5 4 3 2 *
# 5 4 3 * 1
# 5 4 * 2 1
# 5 * 3 2 1
# * 4 3 2 1
# check code for errors
n=5
for i in range(n):
    for j in range(n):
        if j==n-i-1:
                print("*",end=" \n")
        else:
               print(n - j,end="  ")
print()
