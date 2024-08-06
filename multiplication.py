def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
x= int(input("enter a number:"))
multiplication_table(x)
