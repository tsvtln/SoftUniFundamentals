string = input().split(', ')
VALID = False
for word in string:
    if 3 <= len(word) <= 16:
        characters = [ch for ch in word]
        for char in characters:
            if char.isnumeric() or char.isalpha() or '-' in char or '_' in char:
                VALID = True
            else:
                VALID = False
                break
        print(word) if VALID else None
        VALID = False
