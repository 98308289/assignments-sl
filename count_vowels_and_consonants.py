s = "hello world"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in s:
    if char.isalpha():
        if char.lower() in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print({'vowels': vowel_count, 'consonants': consonant_count})
