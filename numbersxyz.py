
def values(numbers):
    li = []
    for num in numbers:
        if num not in li:
            li.append(num)
    print(li)

n = list(map(int, input("Enter numbers separated by commas: ").split(",")))
values(n)


