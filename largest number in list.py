def largest_in_list(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
d=int(input("enter fourth number:"))
print(largest_in_list([a,b,c,d]))
