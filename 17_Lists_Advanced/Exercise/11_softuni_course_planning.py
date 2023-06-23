def add_lesson(lesson_title: str, lessons: list) -> list:
    if lesson_title not in lessons:
        lessons.append(lesson_title)
    return lessons


def insert_lesson(lesson_title: str, index: int, lessons: list) -> list:
    if lesson_title not in lessons:
        lessons.insert(index, lesson_title)
    return lessons


def remove_lesson(lesson_title: str, lessons: list) -> list:
    LESSON_EXIST, LESSON_EXERCISE_EXIST = False, False
    index_exercise, index_lesson = 0, 0
    if lesson_title in lessons:
        LESSON_EXIST = True
        index_lesson = lessons.index(lesson_title)
        if lesson_title + '-Exercise' in lessons:
            LESSON_EXERCISE_EXIST = True
            index_exercise = lessons.index(lesson_title + '-Exercise')
    if LESSON_EXERCISE_EXIST and LESSON_EXIST:
        lessons.pop(index_exercise)
        lessons.pop(index_lesson)
    elif LESSON_EXIST:
        lessons.pop(index_lesson)
    return lessons


def swap_lesson(lesson_title: str, lesson_title_two: str, lessons: list) -> list:
    FIRST_EXIST, FIRST_EXERCISE_EXIST, SECOND_EXIST, SECOND_EXERCISE_EXIST = False, False, False, False
    index_first_lesson, index_exercise_first_lesson, index_second_lesson, index_exercise_second_lesson = 0, 0, 0, 0
    if lesson_title in lessons:
        FIRST_EXIST = True
        index_first_lesson = lessons.index(lesson_title)
        if lesson_title + '-Exercise' in lessons:
            FIRST_EXERCISE_EXIST = True
            index_exercise_first_lesson = lessons.index(lesson_title + '-Exercise')
    if lesson_title_two in lessons:
        SECOND_EXIST = True
        index_second_lesson = lessons.index(lesson_title_two)
        if lesson_title_two + '-Exercise' in lessons:
            SECOND_EXERCISE_EXIST = True
            index_exercise_second_lesson = lessons.index(lesson_title_two + '-Exercise')
    if FIRST_EXIST and FIRST_EXERCISE_EXIST and SECOND_EXIST and SECOND_EXERCISE_EXIST:
        title_second_lesson = lessons[index_second_lesson]
        title_exercise_second_lesson = lessons[index_exercise_second_lesson]
        lessons[index_second_lesson] = lessons[index_first_lesson]
        lessons[index_exercise_second_lesson] = lessons[index_exercise_first_lesson]
        lessons[index_first_lesson] = title_second_lesson
        lessons[index_exercise_first_lesson] = title_exercise_second_lesson
    elif FIRST_EXIST and FIRST_EXERCISE_EXIST and SECOND_EXIST:
        title_first_lesson = lessons[index_first_lesson]
        title_first_lesson_exercise = lessons[index_exercise_first_lesson]
        title_second_lesson = lessons[index_second_lesson]
        if index_second_lesson > index_exercise_first_lesson:
            lessons.pop(index_second_lesson)
            lessons.pop(index_exercise_first_lesson)
            lessons.pop(index_first_lesson)
        else:
            lessons.pop(index_exercise_first_lesson)
            lessons.pop(index_first_lesson)
            lessons.pop(index_second_lesson)
        lessons.insert(index_first_lesson, title_second_lesson)
        lessons.insert(index_second_lesson, title_first_lesson)
        lessons.insert(index_second_lesson + 1, title_first_lesson_exercise)
    elif FIRST_EXIST and SECOND_EXIST and SECOND_EXERCISE_EXIST:
        title_first_lesson = lessons[index_first_lesson]
        title_second_lesson = lessons[index_second_lesson]
        title_second_lesson_exercise = lessons[index_exercise_second_lesson]
        if index_second_lesson > index_first_lesson:
            lessons.pop(index_exercise_second_lesson)
            lessons.pop(index_second_lesson)
            lessons.pop(index_first_lesson)
        else:
            lessons.pop(index_first_lesson)
            lessons.pop(index_exercise_second_lesson)
            lessons.pop(index_second_lesson)
        lessons.insert(index_first_lesson, title_second_lesson)
        lessons.insert(index_first_lesson + 1, title_second_lesson_exercise)
        lessons.insert(index_second_lesson + 1, title_first_lesson)
    elif FIRST_EXIST and SECOND_EXIST:
        title_second_lesson = lessons[index_second_lesson]
        lessons[index_second_lesson] = lessons[index_first_lesson]
        lessons[index_first_lesson] = title_second_lesson
    return lessons


def exercise_lessons(lesson_title: str, lessons: list) -> list:
    LESSON_EXIST, LESSON_EXERCISE_EXIST = False, False
    if lesson_title in lessons:
        LESSON_EXIST = True
        if lesson_title + '-Exercise' in lessons:
            LESSON_EXERCISE_EXIST = True
    if LESSON_EXIST and not LESSON_EXERCISE_EXIST:
        index_lesson = lessons.index(lesson_title)
        lessons.insert(index_lesson + 1, lesson_title + '-Exercise')
    elif not LESSON_EXIST:
        lessons.append(lesson_title)
        lessons.append(lesson_title + '-Exercise')
    return lessons


courses = input().split(', ')
command, prt_index = '', 0
while command != 'course start':
    entry_command = input()
    if entry_command == 'course start':
        command = 'course start'
        continue
    else:
        entry_command = entry_command.split(':')
        if entry_command[0] == 'Add':
            g_lesson_title = entry_command[1]
            courses = add_lesson(g_lesson_title, courses)
        elif entry_command[0] == 'Insert':
            g_lesson_title = entry_command[1]
            g_index = int(entry_command[2])
            courses = insert_lesson(g_lesson_title, g_index, courses)
        elif entry_command[0] == 'Remove':
            g_lesson_title = entry_command[1]
            courses = remove_lesson(g_lesson_title, courses)
        elif entry_command[0] == 'Swap':
            g_lesson_title = entry_command[1]
            g_lesson_title_two = entry_command[2]
            courses = swap_lesson(g_lesson_title, g_lesson_title_two, courses)
        elif entry_command[0] == 'Exercise':
            g_lesson_title = entry_command[1]
            courses = exercise_lessons(g_lesson_title, courses)

for lesson in courses:
    prt_index += 1
    print(f"{prt_index}.{lesson}")
