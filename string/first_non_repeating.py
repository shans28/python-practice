# Problem Statement

# Given a string, return the first non-repeating character.
# If none exists, return None.

def first_non_repeating(input: str, case_sensitive: bool = True):
    char_count = {}
    if not case_sensitive:
        input = input.lower()
    for char in input:
        count = char_count.get(char, 0)
        # char_count.update({char: count + 1})
        char_count[char]= count+1
    # print(char_count)
    for char in input:
        if char_count[char] == 1:
            print(f"String has '{char}' as first non-repeating character")
            return char

    