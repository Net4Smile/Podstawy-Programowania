sentence = "hello universe"
vowels = "aeiou"
count = 0

for char in sentence:
    if char in vowels:
        count = count

print("Vowel count:", count)  # Output is incorrect