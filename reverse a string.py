def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
x = input("enter a word:")
print(reverse_string(x))
