"""
v.7.1
- Changed text: "To exit type any key." to "To exit press any key."

v.7
- Questions are now in json file and called here.

v.6
- Cropped some unnecessary code.
- Added time formatting.
- Added contributors.
- Added time left between questions.
- Added time spent taking the QUIZ.
- Minor code formatting.
- Recolored some things.
"""

import time
import json

# Text Coloration
CSI = '\033['


def code_to_chars(code):
    return CSI + str(code) + 'm'


class AnsiCodes(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class AnsiToColor(AnsiCodes):
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = 30, 31, 32, 33, 34, 35, 36, 37


class AnsiStyle(AnsiCodes):
    BRIGHT, DIM, NORMAL, RESET_ALL = 1, 2, 22, 0


# Formatting the seconds to minutes:seconds (eg. 675seconds = 11:25)
def format_time(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    formatted_time = "{:02d}:{:02d}".format(minutes, remaining_seconds)
    return formatted_time


# Variables
questions = json.load(open('questions.json', 'r'))
Color, Style = AnsiToColor(), AnsiStyle()
start_time = time.time()
time_limit = 15 * 60  # 15 minutes
score, elapsed_time, time_left = 0, 0, 0

print(Color.WHITE, Style.BRIGHT + "Text Processing\nQUIZ by Mario Zahariev @\n"
                                  "GITHUB: https://github.com/zahariev-webbersof")
print(Color.MAGENTA + 'Mantained by tsvtln@\nDiscord:    PotKor#1842\nGITHUB:     https://github.com/tsvtln')
print(Color.MAGENTA + 'CONTRIBUTORS\nСтефи @\nDiscord:    Стефи#3040\nGITHUB:     https://github.com/stefipop')
print(Color.RED + "Provide the answers by typing 'a', 'b', 'c' or 'd'")
print()

for question_num, question_data in questions.items():
    print(Color.BLUE + f"{question_num}. {question_data['question']}")
    for option, text in question_data['options'].items():
        print(Color.BLUE + f"{option}) {text}")
    print()
    while True:
        answer = input(Color.GREEN + 'Your answer: ').lower()
        if answer in ['a', 'b', 'c', 'd']:
            if answer == question_data['answer']:
                score += 1
            elapsed_time = time.time() - start_time
            time_left = time_limit - elapsed_time
            print(Color.RED + f'Time left: {format_time(int(time_left))} minutes.')
            break
        else:
            print(Color.RED + "Incorrect input, please provide the answers by typing 'a', 'b', 'c' or 'd'")
    print("\n\n")

    if elapsed_time >= time_limit:
        print("Time's up! You have reached the time limit.")
        break

if elapsed_time >= time_limit:
    print("Time's up! You have reached the time limit.")

else:
    print(Color.GREEN + f"Your final score is {score}/{len(questions)} correct answers.")
    print(f'Time spent taking the QUIZ: {format_time(int(elapsed_time))} minutes.')
    print("To see the correct answers, type 'y'. To exit press any key.")
    final_answers = input().lower()
    if final_answers == 'y':
        for q_num, q_data in questions.items():
            print(Color.BLUE + f"{q_num}. {q_data['question']}")
            print(Color.BLUE + f"Correct Answer: {q_data['answer']}) '{q_data['options'][q_data['answer']]}'\n")
        print(Color.BLUE + 'Thank you for taking this QUIZ. Bye!')
    else:
        print(Color.BLUE + 'Thank you for taking this QUIZ. Bye!')
