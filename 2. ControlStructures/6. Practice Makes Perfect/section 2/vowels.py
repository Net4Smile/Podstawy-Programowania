###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

# Count vowels in the text
# replace for with while
while True:
    char = text[0]
    if char in vowels:
        vowel_count += 1
    # removes first character from the text
    text = text[1:]
    if len(text) == 0:
        break

print(f"The number of vowels in the text is: {vowel_count}")