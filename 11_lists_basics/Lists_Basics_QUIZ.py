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

print(Fore.WHITE + 'Data Types and Variables\nQUIZ by Mario Zahariev zahariev-webbersof@github')
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = '', '', '', '', '', '', '', '', '', ''
a1g, a2g, a3g, a4g, a5g, a6g, a7g, a8g, a9g, a10g = False, False, False, False, False, False, False, False, False, False
score = 0
print(Fore.RED + "Provide the answers by typing 'a', 'b', 'c' or 'd'")
print()

# Questions
questions = [Fore.BLUE + f"1. What is the correct way to create an empty list?\n"
                         f"   a) `list = []`\n   b) `list = {}`\n   c) `list = ()`\n"
                         f"   d) `list = ''`\n\n\n", f"2. Which method is used to add an element to the "
                                                     f"end of a list?\n   a) `append()`\n   b) `extend()`\n"
                                                     f"   c) `insert()`\n   d) `remove()`"]

# Question 1
print(Fore.BLUE + '1. What is the data type of the variable age in the following code snippet?')
print(Fore.LIGHTYELLOW_EX + ' age = 25')
print(Fore.BLUE + 'a) int')
print(Fore.BLUE + 'b) str')
print(Fore.BLUE + 'c) bool')
print(Fore.BLUE + 'd) float')
print()
while not a1g:
    a1 = input('Your answer: ').lower()
    if a1 == 'a' or a1 == 'b' or a1 == 'c' or a1 == 'd':
        a1g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 2
print(Fore.BLUE + '2. Which of the following is a numeric data type in Python?')
print(Fore.BLUE + 'a) list')
print(Fore.BLUE + 'b) tuple')
print(Fore.BLUE + 'c) int')
print(Fore.BLUE + 'd) dict')
print()
while not a2g:
    a2 = input('Your answer: ').lower()
    if a2 == 'a' or a2 == 'b' or a2 == 'c' or a2 == 'd':
        a2g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 3
print(Fore.BLUE + '3.  What is the result of the following expression?')
print(Fore.LIGHTYELLOW_EX + 'a, b = 1.25, 1.25')
print(Fore.LIGHTYELLOW_EX + 'result = a + b')
print(Fore.LIGHTYELLOW_EX + "print(f'{result:.1f}')")
print(Fore.BLUE + 'a) 2')
print(Fore.BLUE + 'b) 2.5')
print(Fore.BLUE + 'c) 2.0')
print(Fore.BLUE + 'd) 2.2')
print()
while not a3g:
    a3 = input('Your answer: ').lower()
    if a3 == 'a' or a3 == 'b' or a3 == 'c' or a3 == 'd':
        a3g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 4
print(Fore.BLUE + '4. Which data type is used to store a sequence of characters in Python?')
print(Fore.BLUE + 'a) str')
print(Fore.BLUE + 'b) int')
print(Fore.BLUE + 'c) bool')
print(Fore.BLUE + 'd) float')
print()
while not a4g:
    a4 = input('Your answer: ').lower()
    if a4 == 'a' or a4 == 'b' or a4 == 'c' or a4 == 'd':
        a4g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 5
print(Fore.BLUE + '5. What is the value of the variable is_valid in the following code snippet?')
print(Fore.LIGHTYELLOW_EX + 'if isinstance(123, str):')
print(Fore.LIGHTYELLOW_EX + '    is_valid = True')
print(Fore.LIGHTYELLOW_EX + 'else:')
print(Fore.LIGHTYELLOW_EX + '    is_valid = False')
print(Fore.LIGHTYELLOW_EX + 'print(is_valid)')
print()
print(Fore.BLUE + 'a) True')
print(Fore.BLUE + 'b) False')
print(Fore.BLUE + 'c) 1')
print(Fore.BLUE + 'd) 0')
print()
while not a5g:
    a5 = input('Your answer: ').lower()
    if a5 == 'a' or a5 == 'b' or a5 == 'c' or a5 == 'd':
        a5g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 6
print(Fore.BLUE + '6. Which data type is used to store multiple values in an ordered and changeable manner?')
print(Fore.BLUE + 'a) list')
print(Fore.BLUE + 'b) set')
print(Fore.BLUE + 'c) tuple')
print(Fore.BLUE + 'd) dict')
print()
while not a6g:
    a6 = input('Your answer: ').lower()
    if a6 == 'a' or a6 == 'b' or a6 == 'c' or a6 == 'd':
        a6g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 7
print(Fore.BLUE + '7. What does the len() function return when called on a string?')
print(Fore.BLUE + 'a) The number of characters in the string.')
print(Fore.BLUE + 'b) True')
print(Fore.BLUE + 'c) False')
print(Fore.BLUE + 'd) The string itself')
print()
while not a7g:
    a7 = input('Your answer: ').lower()
    if a7 == 'a' or a7 == 'b' or a7 == 'c' or a7 == 'd':
        a7g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 8
print(Fore.BLUE + '8. Which of the following is an example of a floating-point number?')

print(Fore.BLUE + 'a) 42')
print(Fore.BLUE + 'b) 3.14')
print(Fore.BLUE + 'c) "Hello"')
print(Fore.BLUE + 'd) True')
print()
while not a8g:
    a8 = input('Your answer: ').lower()
    if a8 == 'a' or a8 == 'b' or a8 == 'c' or a8 == 'd':
        a8g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 9
print(Fore.BLUE + '9. Which data type is used to represent a condition with two possible values: True or False?')
print(Fore.BLUE + 'a) str')
print(Fore.BLUE + 'b) bool')
print(Fore.BLUE + 'c) int')
print(Fore.BLUE + 'd) float')
print()
while not a9g:
    a9 = input('Your answer: ').lower()
    if a9 == 'a' or a9 == 'b' or a9 == 'c' or a9 == 'd':
        a9g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()

# Question 10
print(Fore.BLUE + '10. How do you assign a value to a variable in Python?')

print(Fore.BLUE + 'a) using the var keyword')
print(Fore.BLUE + 'b) using the value keyword')
print(Fore.BLUE + 'c) using the = operator ')
print(Fore.BLUE + 'd) using the assign keyword')
print()
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
    print(Fore.BLUE + f"1.  a) list = []\n2.  a) append()\n3.  c) list[2]\n4.  b) [1, 3]\n5.  d) len(list)")
    print(Fore.BLUE + f"6.  a) list.sort()\n7.  a) The two lists are combined into a single list")
    print(Fore.BLUE + f"8.  a) list.clear()\n9.  a) index()\n10. a) value in list")
else:
    print(Fore.BLUE + 'Thank you for taking this QUIZ. Bye!')

