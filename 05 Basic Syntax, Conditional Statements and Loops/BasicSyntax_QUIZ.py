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

    # These are fairly well supported, but not part of the standard.
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

    # These are fairly well supported, but not part of the standard.
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

print(Fore.WHITE + 'Basic Syntax, Conditional Statements and Loops\nQUIZ by Mario Zahariev zahariev-webbersof@github')
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = '', '', '', '', '', '', '', '', '', ''
a1g, a2g, a3g, a4g, a5g, a6g, a7g, a8g, a9g, a10g = False, False, False, False, False, False, False, False, False, False
score = 0
print(Fore.RED + "Provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
# Question 1
print(Fore.BLUE + '1. Which of the following is the correct syntax for a Python comment?')
print(Fore.BLUE + 'a) // This is a comment')
print(Fore.BLUE + 'b) # This is a comment')
print(Fore.BLUE + 'c) /* This is a comment */')
print(Fore.BLUE + 'd) ** This is a comment **')
while not a1g:
    a1 = input('Your answer: ')
    if a1 == 'a' or a1 == 'b' or a1 == 'c' or a1 == 'd':
        a1g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 2
print(Fore.BLUE + '2. What is the output of the following code snippet?')
print(Fore.LIGHTYELLOW_EX + 'x = 10')
print(Fore.LIGHTYELLOW_EX + 'if x > 5:')
print(Fore.LIGHTYELLOW_EX + '  print("x is greater than 5")')
print(Fore.LIGHTYELLOW_EX + 'else:')
print(Fore.LIGHTYELLOW_EX + '  print("x is less than or equal to 5")')
print(Fore.BLUE + 'a) x is greater than 5')
print(Fore.BLUE + 'b) x is less than or equal to 5')
print(Fore.BLUE + 'c) x')
print(Fore.BLUE + 'd) The code will produce a syntax error.')
while not a2g:
    a2 = input('Your answer: ')
    if a2 == 'a' or a2 == 'b' or a2 == 'c' or a2 == 'd':
        a2g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 3
print(Fore.BLUE + '3. Which of the following is the correct way to define a Python function?')
print(Fore.BLUE + 'a) function_name(argument1, argument2):')
print(Fore.BLUE + 'b) def function_name(argument1, argument2):')
print(Fore.BLUE + 'c) function_name = def(argument1, argument2)')
print(Fore.BLUE + 'd) def = function_name(argument1, argument2)')
while not a3g:
    a3 = input('Your answer: ')
    if a3 == 'a' or a3 == 'b' or a3 == 'c' or a3 == 'd':
        a3g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 4
print(Fore.BLUE + '4.What is the output of the following code snippet?')
print(Fore.LIGHTYELLOW_EX + 'i = 0')
print(Fore.LIGHTYELLOW_EX + 'while i < 5:')
print(Fore.LIGHTYELLOW_EX + '  print(i)')
print(Fore.LIGHTYELLOW_EX + '  i += 1')
print(Fore.BLUE + 'a) 0 1 2 3 4')
print(Fore.BLUE + 'b) 1 2 3 4 5')
print(Fore.BLUE + 'c) 0 1 2 3')
print(Fore.BLUE + 'd) 1 2 3 4')
while not a4g:
    a4 = input('Your answer: ')
    if a4 == 'a' or a4 == 'b' or a4 == 'c' or a4 == 'd':
        a4g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 5
print(Fore.BLUE + '5.Which of the following is the correct way to declare a list in Python?')
print(Fore.BLUE + 'a) list_name = [value1, value2, value3]')
print(Fore.BLUE + 'b) list_name = {value1, value2, value3}')
print(Fore.BLUE + 'c) list_name = (value1, value2, value3)')
print(Fore.BLUE + 'd) list_name = {value1: value2, value3}')
print()
print()
print()
while not a5g:
    a5 = input('Your answer: ')
    if a5 == 'a' or a5 == 'b' or a5 == 'c' or a5 == 'd':
        a5g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 6
print(Fore.BLUE + '6.What is the output of the following code snippet?')
print(Fore.LIGHTYELLOW_EX + 'for i in range(5):')
print(Fore.LIGHTYELLOW_EX + '    if i == 2:')
print(Fore.LIGHTYELLOW_EX + '      break')
print(Fore.LIGHTYELLOW_EX + '    print(i)')
print(Fore.BLUE + 'a) 0 1 2 3 4')
print(Fore.BLUE + 'b) 1 2')
print(Fore.BLUE + 'c) 0 1')
print(Fore.BLUE + 'd) 0 1 3 4')
print()
print()
print()
while not a6g:
    a6 = input('Your answer: ')
    if a6 == 'a' or a6 == 'b' or a6 == 'c' or a6 == 'd':
        a6g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 7
print(Fore.BLUE + '7.Which of the following is the correct way to define a Python dictionary?')
print(Fore.BLUE + 'a) dict_name = {key1, key2, key3: value1, value2, value3}')
print(Fore.BLUE + 'b) dict_name = {key1: value1, key2: value2, key3: value3}')
print(Fore.BLUE + 'c) dict_name = [key1, key2, key3: value1, value2, value3]')
print(Fore.BLUE + 'd) dict_name = (key1, key2, key3: value1, value2, value3)')

while not a7g:
    a7 = input('Your answer: ')
    if a7 == 'a' or a7 == 'b' or a7 == 'c' or a7 == 'd':
        a7g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 8
print(Fore.BLUE + '8.What is the output of the following code snippet?')
print(Fore.LIGHTYELLOW_EX + 'x = 5')
print(Fore.LIGHTYELLOW_EX + 'y = 10')
print(Fore.LIGHTYELLOW_EX + 'if x > y:')
print(Fore.LIGHTYELLOW_EX + '    print("x is greater than y")')
print(Fore.LIGHTYELLOW_EX + 'elif x == y:')
print(Fore.LIGHTYELLOW_EX + '    print("x is equal to y")')
print(Fore.LIGHTYELLOW_EX + 'else:')
print(Fore.LIGHTYELLOW_EX + '    print("x is less than y")')

print(Fore.BLUE + 'a) x is greater than y')
print(Fore.BLUE + 'b) x is equal to y')
print(Fore.BLUE + 'c) x is less than y')
print(Fore.BLUE + 'd) The code will produce a syntax error.')

while not a8g:
    a8 = input('Your answer: ')
    if a8 == 'a' or a8 == 'b' or a8 == 'c' or a8 == 'd':
        a8g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 9
print(Fore.BLUE + '9.Which of the following is the correct syntax for a Python for loop that iterates over a list?')
print(Fore.BLUE + 'a) for i in range(list_name):')
print(Fore.BLUE + 'b) for i in list_name:')
print(Fore.BLUE + 'c) for i in len(list_name):')
print(Fore.BLUE + 'd) for i in range(len(list_name)):')

while not a9g:
    a9 = input('Your answer: ')
    if a9 == 'a' or a9 == 'b' or a9 == 'c' or a9 == 'd':
        a9g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print()
print()
print()
# Question 10
print(Fore.BLUE + '10.What is the output of the following code snippet?')
print(Fore.LIGHTYELLOW_EX + 'i = 0')
print(Fore.LIGHTYELLOW_EX + 'while i < 5:')
print(Fore.LIGHTYELLOW_EX + '    print(i)')
print(Fore.LIGHTYELLOW_EX + '    i += 2')
print(Fore.BLUE + 'a) 0 1 2 3 4')
print(Fore.BLUE + 'b) 0 2 4')
print(Fore.BLUE + 'c) 1 3 5')
print(Fore.BLUE + 'd) 2 4 6')

while not a10g:
    a10 = input('Your answer: ')
    if a10 == 'a' or a10 == 'b' or a10 == 'c' or a10 == 'd':
        a10g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")

if a1 == 'b':
    score += 1
if a2 == 'a':
    score += 1
if a3 == 'b':
    score += 1
if a4 == 'a':
    score += 1
if a5 == 'a':
    score += 1
if a6 == 'c':
    score += 1
if a7 == 'b':
    score += 1
if a8 == 'c':
    score += 1
if a9 == 'd':
    score += 1
if a10 == 'b':
    score += 1
print()

print(Fore.LIGHTGREEN_EX + f"Your final score is {score}/10 correct asnwers.")
print("To see the correct answers, type 'y'. To exit type any key.")
final_answers = input()
if final_answers == 'y':
    print(Fore.BLUE + "1 -  b) # This is a comment")
    print(Fore.BLUE + "2 -  a) x is greater than 5")
    print(Fore.BLUE + "3 -  b) def function_name(argument1, argument2):")
    print(Fore.BLUE + "4 -  a) 0 1 2 3 4")
    print(Fore.BLUE + "5 -  a) list_name = [value1, value2, value3]")
    print(Fore.BLUE + "6 -  c) 0 1")
    print(Fore.BLUE + "7 -  b) dict_name = {key1: value1, key2: value2, key3: value3}")
    print(Fore.BLUE + "8 -  c) x is less than y")
    print(Fore.BLUE + "9 -  d) for i in range(len(list_name)):")
    print(Fore.BLUE + "10 - b) 0 2 4")
else:
    print(Fore.BLUE + 'Thank you for taking this QUIZ. Bye!')
