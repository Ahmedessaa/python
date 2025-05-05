def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count


string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
