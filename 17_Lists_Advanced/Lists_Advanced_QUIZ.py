import time

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


HAS_TIME = True
timer_duration = 900
start_time = time.time()
elapsed_time = 0

print(Fore.WHITE + 'Lists Advanced\nQUIZ by Mario Zahariev zahariev-webbersof@github')
print(Fore.LIGHTRED_EX + 'You will have 15 minutes to complete the QUIZ')
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = '', '', '', '', '', '', '', '', '', ''
a1g, a2g, a3g, a4g, a5g, a6g, a7g, a8g, a9g, a10g = False, False, False, False, False, False, False, False, False, False
score = 0
print(Fore.RED + "Provide the answers by typing 'a', 'b', 'c' or 'd'")
print()

while HAS_TIME and not a1g:
    # Question 1
    print(Fore.BLUE + '1. What is the purpose of a lambda function in Python?')
    print(Fore.BLUE + 'a) To define a named function')
    print(Fore.BLUE + 'b) To create anonymous functions ')
    print(Fore.BLUE + 'c) To iterate over a list')
    print(Fore.BLUE + 'd) To swap elements in a list\n')

    while not a1g:
        a1 = input('Your answer: ').lower()
        if a1 == 'a' or a1 == 'b' or a1 == 'c' or a1 == 'd':
            a1g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    # print(f"Time left: {timer_duration - elapsed_time:.0f}")
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")


while HAS_TIME and not a2g:
    # Question 2
    print(Fore.BLUE + '2. Which of the following is a correct syntax for list comprehension in Python?')
    print(Fore.BLUE + 'a) [x for x in range(10)]')
    print(Fore.BLUE + 'b) [for x in range(10) if x % 2 == 0]')
    print(Fore.BLUE + 'c) [x if x % 2 == 0 for x in range(10)] ')
    print(Fore.BLUE + 'd) [x in range(10) if x % 2 == 0]\n')
    while not a2g:
        a2 = input('Your answer: ').lower()
        if a2 == 'a' or a2 == 'b' or a2 == 'c' or a2 == 'd':
            a2g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")

while HAS_TIME and not a3g:
    # Question 3
    print(Fore.BLUE + '3. How can you swap the elements of two lists in Python?')
    print(Fore.BLUE + 'a) Using the swap() method')
    print(Fore.BLUE + 'b) Using the zip() function')
    print(Fore.BLUE + 'c) Using list concatenation')
    print(Fore.BLUE + 'd) Using simultaneous assignment or a temporary variable\n')
    while not a3g:
        a3 = input('Your answer: ').lower()
        if a3 == 'a' or a3 == 'b' or a3 == 'c' or a3 == 'd':
            a3g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")

while HAS_TIME and not a4g:
    # Question 4
    print(Fore.BLUE + '4. Which function is used to extract unique elements from a list in Python?')
    # print(Fore.LIGHTYELLOW_EX + 'my_list = [1, 2, 3]')
    # print(Fore.LIGHTYELLOW_EX + 'my_list.remove(2)')
    # print(Fore.LIGHTYELLOW_EX + 'print(my_list)')
    # print()
    print(Fore.BLUE + 'a) unique()')
    print(Fore.BLUE + 'b) distinct()')
    print(Fore.BLUE + 'c) set()')
    print(Fore.BLUE + 'd) list()\n')
    while not a4g:
        a4 = input('Your answer: ').lower()
        if a4 == 'a' or a4 == 'b' or a4 == 'c' or a4 == 'd':
            a4g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")

while HAS_TIME and not a5g:
    # Question 5
    print(Fore.BLUE + '5. What does the sorted() function do in Python?')
    print(Fore.BLUE + 'a) Sorts the elements of a list in ascending order ')
    print(Fore.BLUE + 'b) Sorts the elements of a list in descending order')
    print(Fore.BLUE + 'c) Removes duplicates from a list')
    print(Fore.BLUE + 'd) Reverses the order of elements in a list\n')
    print()
    while not a5g:
        a5 = input('Your answer: ').lower()
        if a5 == 'a' or a5 == 'b' or a5 == 'c' or a5 == 'd':
            a5g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")

while HAS_TIME and not a6g:
    # Question 6
    print(Fore.BLUE + '6. What is the purpose of the map() function in Python?')
    print(Fore.BLUE + 'a) To extract elements based on a condition')
    print(Fore.BLUE + 'b) To transform elements of a list based on a function ')
    print(Fore.BLUE + 'c) To sort elements in a list')
    print(Fore.BLUE + 'd) To extract unique elements from a list\n')
    while not a6g:
        a6 = input('Your answer: ').lower()
        if a6 == 'a' or a6 == 'b' or a6 == 'c' or a6 == 'd':
            a6g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")

while HAS_TIME and not a7g:
    # Question 7
    print(Fore.BLUE + '7. Which function is used to filter elements from a list based on a condition in Python?')
    print(Fore.BLUE + 'a) select()')
    print(Fore.BLUE + 'b) find()')
    print(Fore.BLUE + 'c) filter() ')
    print(Fore.BLUE + 'd) match()\n')
    while not a7g:
        a7 = input('Your answer: ').lower()
        if a7 == 'a' or a7 == 'b' or a7 == 'c' or a7 == 'd':
            a7g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")

while HAS_TIME and not a8g:
    # Question 8
    print(Fore.BLUE + '8. How can you check if a number is divisible by 3 using a lambda function in Python?')
    print(Fore.BLUE + 'a) lambda x: x % 3 == 0 ')
    print(Fore.BLUE + 'b) lambda x: x / 3 == 0')
    print(Fore.BLUE + 'c) lambda x: x == 3')
    print(Fore.BLUE + 'd) lambda x: x % 3\n')
    while not a8g:
        a8 = input('Your answer: ').lower()
        if a8 == 'a' or a8 == 'b' or a8 == 'c' or a8 == 'd':
            a8g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")

while HAS_TIME and not a9g:
    # Question 9
    print(Fore.BLUE + '9.What is the output of the following list comprehension?')
    print(Fore.LIGHTYELLOW_EX + 'numbers = [1, 2, 3, 4, 5]')
    print(Fore.LIGHTYELLOW_EX + 'squares = [x ** 2 for x in numbers]')
    print(Fore.LIGHTYELLOW_EX + 'print(squares)')
    print()
    print(Fore.BLUE + 'a) [1, 4, 9, 16, 25] ')
    print(Fore.BLUE + 'b) [2, 4, 6, 8, 10]')
    print(Fore.BLUE + 'c) [1, 3, 5, 7, 9]')
    print(Fore.BLUE + 'd) [1, 2, 3, 4, 5]\n')
    while not a9g:
        a9 = input('Your answer: ').lower()
        if a9 == 'a' or a9 == 'b' or a9 == 'c' or a9 == 'd':
            a9g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False
    print("\n\n\n")

while HAS_TIME and not a10g:
    # Question 10
    print(Fore.BLUE + '10. What is the output of the following:')
    print(Fore.LIGHTYELLOW_EX + 'my_list = [1, 2, 3]')
    print(Fore.LIGHTYELLOW_EX + 'my_list.extend([4, 5])')
    print()
    print(Fore.BLUE + 'a) No output')
    print(Fore.BLUE + 'b) Extend is not a valid function')
    print(Fore.BLUE + 'c) [4, 5, 1, 2, 3]')
    print(Fore.BLUE + 'd) [1, 2, 3, 4, 5]\n')

    while not a10g:
        a10 = input('Your answer: ').lower()
        if a10 == 'a' or a10 == 'b' or a10 == 'c' or a10 == 'd':
            a10g = True
            continue
        else:
            print(Fore.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer_duration:
        HAS_TIME = False

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

