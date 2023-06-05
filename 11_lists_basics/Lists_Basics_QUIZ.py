CSI = '\033['
OSC = '\033]'
BEL = '\a'


def code_to_chars(code):
    return CSI + str(code) + 'm'


def set_title(title):
    return OSC + '2;' + title + BEL


def clear_screen(mode=2):
    return CSI + str(mode) + 'J'


def clear_line(mode=2):
    return CSI + str(mode) + 'K'


class AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.
        # Upon instantiation we define instance attributes, which are the same
        # as the class attributes but wrapped with the ANSI escape sequence
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class AnsiCursor(object):
    def UP(self, n=1):
        return CSI + str(n) + 'A'

    def DOWN(self, n=1):
        return CSI + str(n) + 'B'

    def FORWARD(self, n=1):
        return CSI + str(n) + 'C'

    def BACK(self, n=1):
        return CSI + str(n) + 'D'

    def POS(self, x=1, y=1):
        return CSI + str(y) + ';' + str(x) + 'H'


class AnsiFore(AnsiCodes):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    RESET = 39

    # These are fairly well-supported, but not part of the standard.
    LIGHTBLACK_EX = 90
    LIGHTRED_EX = 91
    LIGHTGREEN_EX = 92
    LIGHTYELLOW_EX = 93
    LIGHTBLUE_EX = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX = 96
    LIGHTWHITE_EX = 97


class AnsiBack(AnsiCodes):
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47
    RESET = 49

    # These are fairly well-supported, but not part of the standard.
    LIGHTBLACK_EX = 100
    LIGHTRED_EX = 101
    LIGHTGREEN_EX = 102
    LIGHTYELLOW_EX = 103
    LIGHTBLUE_EX = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX = 106
    LIGHTWHITE_EX = 107


class AnsiStyle(AnsiCodes):
    BRIGHT = 1
    DIM = 2
    NORMAL = 22
    RESET_ALL = 0


Fore = AnsiFore()
Back = AnsiBack()
Style = AnsiStyle()
Cursor = AnsiCursor()

print(Fore.WHITE + 'Lists Basics\nQUIZ by Mario Zahariev zahariev-webbersof@github')
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = '', '', '', '', '', '', '', '', '', ''
a1g, a2g, a3g, a4g, a5g, a6g, a7g, a8g, a9g, a10g = False, False, False, False, False, False, False, False, False, False
score = 0
print(Fore.RED + "Provide the answers by typing 'a', 'b', 'c' or 'd'")
print()

# Question 1
print(Fore.BLUE + '1. What is the correct way to create an empty list?')
print(Fore.BLUE + 'a) `list = []`')
print(Fore.BLUE + 'b) `list = {}`')
print(Fore.BLUE + 'c) `list = ()`')
print(Fore.BLUE + 'd) `list = ''`\n')

while not a1g:
    a1 = input('Your answer: ').lower()
    if a1 == 'a' or a1 == 'b' or a1 == 'c' or a1 == 'd':
        a1g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")

# Question 2
print(Fore.BLUE + '2. Which method is used to add an element to the end of a list?')
print(Fore.BLUE + 'a) `append()`')
print(Fore.BLUE + 'b) `extend()`')
print(Fore.BLUE + 'c) `insert()`')
print(Fore.BLUE + 'd) `remove()`\n')
while not a2g:
    a2 = input('Your answer: ').lower()
    if a2 == 'a' or a2 == 'b' or a2 == 'c' or a2 == 'd':
        a2g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 3
print(Fore.BLUE + '3. How do you access the third element of a list?')
print(Fore.BLUE + 'a) `list[0]`')
print(Fore.BLUE + 'b) `list[1]`')
print(Fore.BLUE + 'c) `list[2]`')
print(Fore.BLUE + 'd) `list[3]`\n')
while not a3g:
    a3 = input('Your answer: ').lower()
    if a3 == 'a' or a3 == 'b' or a3 == 'c' or a3 == 'd':
        a3g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 4
print(Fore.BLUE + '4. What is the result of the following code?')
print(Fore.LIGHTYELLOW_EX + 'my_list = [1, 2, 3]')
print(Fore.LIGHTYELLOW_EX + 'my_list.remove(2)')
print(Fore.LIGHTYELLOW_EX + 'print(my_list)')
print()
print(Fore.BLUE + 'a) `[1, 2, 3]`')
print(Fore.BLUE + 'b) `[1, 3]`')
print(Fore.BLUE + 'c) `[2, 3]`')
print(Fore.BLUE + 'd) `Error`\n')
while not a4g:
    a4 = input('Your answer: ').lower()
    if a4 == 'a' or a4 == 'b' or a4 == 'c' or a4 == 'd':
        a4g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")

# Question 5
print(Fore.BLUE + '5. How can you find the number of elements in a list?')
print(Fore.BLUE + 'a) `list.length()`')
print(Fore.BLUE + 'b) `list.count()`')
print(Fore.BLUE + 'c) `list.size()`')
print(Fore.BLUE + 'd) `len(list)`\n')
print()
while not a5g:
    a5 = input('Your answer: ').lower()
    if a5 == 'a' or a5 == 'b' or a5 == 'c' or a5 == 'd':
        a5g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 6
print(Fore.BLUE + '6. What method is used to sort a list in ascending order?')
print(Fore.BLUE + 'a) `list.sort()`')
print(Fore.BLUE + 'b) `list.reverse()`')
print(Fore.BLUE + 'c) `list.append()`')
print(Fore.BLUE + 'd) `list.remove()`\n')
while not a6g:
    a6 = input('Your answer: ').lower()
    if a6 == 'a' or a6 == 'b' or a6 == 'c' or a6 == 'd':
        a6g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 7
print(Fore.BLUE + '7. What happens when you use the `+` operator to concatenate two lists?')
print(Fore.BLUE + 'a) The two lists are combined into a single list.')
print(Fore.BLUE + 'b) The `+` operator cannot be used with lists.')
print(Fore.BLUE + 'c) An error is thrown.')
print(Fore.BLUE + 'd) The lists remain unchanged.\n')
while not a7g:
    a7 = input('Your answer: ').lower()
    if a7 == 'a' or a7 == 'b' or a7 == 'c' or a7 == 'd':
        a7g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 8
print(Fore.BLUE + '8. How do you remove all elements from a list?')
print(Fore.BLUE + 'a) `list.clear()`')
print(Fore.BLUE + 'b) `list.remove_all()`')
print(Fore.BLUE + 'c) `list.delete_all()`')
print(Fore.BLUE + 'd) `list.pop()`\n')
while not a8g:
    a8 = input('Your answer: ').lower()
    if a8 == 'a' or a8 == 'b' or a8 == 'c' or a8 == 'd':
        a8g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 9
print(Fore.BLUE + '9. Which method is used to obtain the index of an element in a list?')
print(Fore.BLUE + 'a) `index()`')
print(Fore.BLUE + 'b) `find()`')
print(Fore.BLUE + 'c) `search()`')
print(Fore.BLUE + 'd) `locate()`\n')
while not a9g:
    a9 = input('Your answer: ').lower()
    if a9 == 'a' or a9 == 'b' or a9 == 'c' or a9 == 'd':
        a9g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 10
print(Fore.BLUE + '10. How do you check if a value exists in a list?')

print(Fore.BLUE + '    a) `value in list`')
print(Fore.BLUE + '    b) `list.contains(value)`')
print(Fore.BLUE + '    c) `list.exists(value)`')
print(Fore.BLUE + '    d) `list.include(value)`\n')

while not a10g:
    a10 = input('Your answer: ').lower()
    if a10 == 'a' or a10 == 'b' or a10 == 'c' or a10 == 'd':
        a10g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")


answers = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
for i in range(len(answers)):
    if answers[i] == 'a' and i in [0, 1, 5, 6, 7, 8, 9]:
        score += 1
        continue
    elif answers[i] == 'b' and i in [3]:
        score += 1
        continue
    elif answers[i] == 'c' and i in [2]:
        score += 1
        continue
    elif answers[i] == 'd' and i in [4]:
        score += 1
        continue
print()

print(Fore.LIGHTGREEN_EX + f"Your final score is {score}/10 correct answers.")
print("To see the correct answers, type 'y'. To exit type any key.")
final_answers = input().lower()
if final_answers == 'y':
    print(Fore.BLUE + "1 -  a) list=[]")
    print(Fore.BLUE + "2 -  a) append()")
    print(Fore.BLUE + "3 -  c) list[2]")
    print(Fore.BLUE + "4 -  b) [1, 3]")
    print(Fore.BLUE + "5 -  d) len(list)")
    print(Fore.BLUE + "6 -  a) list.sort()")
    print(Fore.BLUE + "7 -  a) The two lists are combined into a single list")
    print(Fore.BLUE + "8 -  a) list.clear()")
    print(Fore.BLUE + "9 -  a) index()")
    print(Fore.BLUE + "10 - a) value in list")
else:
    print(Fore.BLUE + 'Thank you for taking this QUIZ. Bye!')

