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

print(Fore.WHITE + 'Lists Advanced\nQUIZ by Mario Zahariev zahariev-webbersof@github')
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = '', '', '', '', '', '', '', '', '', ''
a1g, a2g, a3g, a4g, a5g, a6g, a7g, a8g, a9g, a10g = False, False, False, False, False, False, False, False, False, False
score = 0
print(Fore.RED + "Provide the answers by typing 'a', 'b', 'c' or 'd'")
print()

# Question 1
print(Fore.BLUE + '1. Which keyword is used to define a function in Python?')
print(Fore.BLUE + 'a) method')
print(Fore.BLUE + 'b) def ')
print(Fore.BLUE + 'c) function')
print(Fore.BLUE + 'd) define\n')

while not a1g:
    a1 = input('Your answer: ').lower()
    if a1 == 'a' or a1 == 'b' or a1 == 'c' or a1 == 'd':
        a1g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")

# Question 2
print(Fore.BLUE + '2. What is the purpose of the lambda keyword in Python?')
print(Fore.BLUE + 'a) To define a class')
print(Fore.BLUE + 'b) To create a variable')
print(Fore.BLUE + 'c) To declare a function')
print(Fore.BLUE + 'd) To define an anonymous function\n')
while not a2g:
    a2 = input('Your answer: ').lower()
    if a2 == 'a' or a2 == 'b' or a2 == 'c' or a2 == 'd':
        a2g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 3
print(Fore.BLUE + '3. What does the len() function return when applied to a list in Python?')
print(Fore.BLUE + 'a) The sum of all elements in the list')
print(Fore.BLUE + 'b) The number of items in the list ')
print(Fore.BLUE + 'c) The average of all elements in the list')
print(Fore.BLUE + 'd) The maximum value in the list\n')
while not a3g:
    a3 = input('Your answer: ').lower()
    if a3 == 'a' or a3 == 'b' or a3 == 'c' or a3 == 'd':
        a3g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 4
print(Fore.BLUE + '4. How do you call a function named my_function in Python?')
# print(Fore.LIGHTYELLOW_EX + 'my_list = [1, 2, 3]')
# print(Fore.LIGHTYELLOW_EX + 'my_list.remove(2)')
# print(Fore.LIGHTYELLOW_EX + 'print(my_list)')
# print()
print(Fore.BLUE + 'a) call my_function()')
print(Fore.BLUE + 'b) my_function')
print(Fore.BLUE + 'c) invoke my_function()')
print(Fore.BLUE + 'd) my_function()\n')
while not a4g:
    a4 = input('Your answer: ').lower()
    if a4 == 'a' or a4 == 'b' or a4 == 'c' or a4 == 'd':
        a4g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")

# Question 5
print(Fore.BLUE + '5. What is the return type of the range() function in Python?')
print(Fore.BLUE + 'a) Integer')
print(Fore.BLUE + 'b) List')
print(Fore.BLUE + 'c) Tuple')
print(Fore.BLUE + 'd) Range object\n')
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
print(Fore.BLUE + '6. What does the map() function do in Python?')
print(Fore.BLUE + 'a) Applies a function to each element of an iterable ')
print(Fore.BLUE + 'b) Filters out elements from an iterable')
print(Fore.BLUE + 'c) Computes the sum of all elements in an iterable')
print(Fore.BLUE + 'd) Sorts the elements of an iterable\n')
while not a6g:
    a6 = input('Your answer: ').lower()
    if a6 == 'a' or a6 == 'b' or a6 == 'c' or a6 == 'd':
        a6g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 7
print(Fore.BLUE + '7. Can a function in Python have multiple return statements?')
print(Fore.BLUE + 'a) Yes ')
print(Fore.BLUE + 'b) No')
print(Fore.BLUE + 'c) Only if the function has a single parameter')
print(Fore.BLUE + 'd) Only if the function is defined using lambda\n')
while not a7g:
    a7 = input('Your answer: ').lower()
    if a7 == 'a' or a7 == 'b' or a7 == 'c' or a7 == 'd':
        a7g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 8
print(Fore.BLUE + '8. Can a function in Python have optional parameters?')
print(Fore.BLUE + 'a) Yes ')
print(Fore.BLUE + 'b) No')
print(Fore.BLUE + 'c) Only if the function is defined using lambda')
print(Fore.BLUE + 'd) Only if the function has a single line of code\n')
while not a8g:
    a8 = input('Your answer: ').lower()
    if a8 == 'a' or a8 == 'b' or a8 == 'c' or a8 == 'd':
        a8g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 9
print(Fore.BLUE + '9. What is the scope of a variable defined inside a function in Python?')
print(Fore.BLUE + 'a) Global scope')
print(Fore.BLUE + 'b) Class scope')
print(Fore.BLUE + 'c) Function scope ')
print(Fore.BLUE + 'd) Module scope\n')
while not a9g:
    a9 = input('Your answer: ').lower()
    if a9 == 'a' or a9 == 'b' or a9 == 'c' or a9 == 'd':
        a9g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
print("\n\n\n")


# Question 10
print(Fore.BLUE + '10. What is a recursive function in Python?')

print(Fore.BLUE + 'a) A function that calls itself ')
print(Fore.BLUE + 'b) A function defined inside another function')
print(Fore.BLUE + 'c) A function that accepts a variable number of arguments')
print(Fore.BLUE + 'd) A function that returns a boolean value\n')

while not a10g:
    a10 = input('Your answer: ').lower()
    if a10 == 'a' or a10 == 'b' or a10 == 'c' or a10 == 'd':
        a10g = True
        continue
    else:
        print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")


answers = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
for i in range(len(answers)):
    if answers[i] == 'a' and i in [1, 4, 7, 8, 9]:
        score += 1
        continue
    elif answers[i] == 'b' and i in [0, 5]:
        score += 1
        continue
    elif answers[i] == 'c' and i in [3, 6]:
        score += 1
        continue
    elif answers[i] == 'd' and i in [2]:
        score += 1
        continue
print()

print(Fore.LIGHTGREEN_EX + f"Your final score is {score}/10 correct answers.")
print("To see the correct answers, type 'y'. To exit type any key.")
final_answers = input().lower()
if final_answers == 'y':
    print(Fore.BLUE + "1. b) To create anonymous functions")
    print(Fore.BLUE + "2. a) [x for x in range(10)]")
    print(Fore.BLUE + "3. d) Using simultaneous assignment or a temporary variable")
    print(Fore.BLUE + "4. c) set()")
    print(Fore.BLUE + "5. a) Sorts the elements of a list in ascending order")
    print(Fore.BLUE + "6. b) To transform elements of a list based on a function")
    print(Fore.BLUE + "7. c) filter()")
    print(Fore.BLUE + "8. a) lambda x: x % 3 == 0")
    print(Fore.BLUE + "9. a) [1, 4, 9, 16, 25]")
    print(Fore.BLUE + "10. a) [1, 2, 3, 4, 5]")
else:
    print(Fore.BLUE + 'Thank you for taking this QUIZ. Bye!')

