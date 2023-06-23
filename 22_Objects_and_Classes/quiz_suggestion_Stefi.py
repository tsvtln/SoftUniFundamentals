import time
import json

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


def format_time(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    formatted_time = "{:02d}:{:02d}".format(minutes, remaining_seconds)
    return formatted_time


class Quiz:
    def __init__(self):
        self.questions = []

    def load_questions_from_json(self, json_file):
        with open(json_file, 'r') as file:
            self.questions = json.load(file)

    def run_quiz(self):
        Color, Style = AnsiToColor(), AnsiStyle()
        start_time = time.time()
        time_limit = 15 * 60  # 15 minutes
        score, elapsed_time, time_left = 0, 0, 0

        print(Color.RED + "Provide the answers by typing 'a', 'b', 'c' or 'd'")
        print()

        for question_num, question_data in self.questions.items():
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
            print(Color.GREEN + f"Your final score is {score}/{len(self.questions)} correct answers.")
            print(f'Time spent taking the QUIZ: {format_time(int(elapsed_time))} minutes.')
            print("To see the correct answers, type 'y'. To exit type any key.")
            final_answers = input().lower()
            if final_answers == 'y':
                for q_num, q_data in self.questions.items():
                    print(Color.BLUE + f"{q_num}. {q_data['question']}")
                    print(Color.BLUE + f"Correct Answer: {q_data['answer']}) '{q_data['options'][q_data['answer']]}'\n")
            else:
                print(Color.BLUE + 'Thank you for taking this QUIZ. Bye!')


# Usage example
quiz = Quiz()
quiz.load_questions_from_json
