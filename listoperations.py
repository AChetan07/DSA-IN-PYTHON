def noperations(n):
    store=[]

    for i in range(n):
        print("ENter the operation you wanna perform")
        print("1:add element to list")
        print("2:remove element from a list")
        print("3: return the largest element from a list")
        x=int(input("ENter the operation you wanna perform"))

        if x==1:
            num=int(input("enter the number to be inserted"))
            store.append(num)
        elif x==2:
            num=int(input("Enter the number to be removed"))
            store.pop(num)
        elif x==3:
            if not store:
                print("List is empty to determine the max")
            else:
                print( f" {max(store)} is the maximum element") 
        else:
            print("Invalid operation")


n=int(input("Enter the no of operations"))
noperations(n)



    