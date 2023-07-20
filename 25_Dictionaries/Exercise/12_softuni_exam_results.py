command = ''
results = dict()
language_count = dict()
while command != 'exam finished':
    command = input()
    if command == 'exam finished':
        continue

    try:
        username, language, points = command.split('-')
    except ValueError:
        username, language = command.split('-')

    if language == 'banned':
        results[username] = 'banned'
        continue

    points = int(points)

    if username in results.keys():
        if results[username] == 'banned':
            language_count[language] += 1
            continue

    if username not in results.keys():
        results[username] = points
    elif username in results.keys() and points > results[username]:
        results[username] = points
    if language not in language_count.keys():
        language_count[language] = 1
    else:
        language_count[language] += 1

print("Results:")
for user, score in results.items():
    if score != 'banned':
        print(f"{user} | {score}")
print("Submissions:")
for lang, count in language_count.items():
    print(f"{lang} - {count}")
