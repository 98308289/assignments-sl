s = "madam"
is_palindrome = True
for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        is_palindrome = False
        break
print(is_palindrome)
