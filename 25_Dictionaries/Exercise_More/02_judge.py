line = input()
total_scores = {}
results_by_contest = {}

while line != "no more time":
    split_line = line.split(" -> ")
    username, contest, points = split_line[0], split_line[1], int(split_line[2])
    if contest not in results_by_contest:
        results_by_contest[contest] = {}
    if points > results_by_contest[contest].get(username, 0):
        results_by_contest[contest][username] = points
    line = input()

for key, value in results_by_contest.items():
    for name, points in value.items():
        if name not in total_scores:
            total_scores[name] = 0
        total_scores[name] += points

for contest, data in results_by_contest.items():
    data = sorted(data.items(), key=lambda x: (-x[1], x[0]))
    results_by_contest[contest] = data

total_scores = sorted(total_scores.items(), key=lambda x: (-x[1], x[0]))

for contest, data in results_by_contest.items():
    print(f"{contest}: {len(data)} participants")
    for position, (username, points) in enumerate(data, start=1):
        print(f"{position}. {username} <::> {points}")
print("Individual standings:")
for position, (username, points) in enumerate(total_scores, start=1):
    print(f"{position}. {username} -> {points}")

""" 50 / 100"""
# command = ''
# participation_data = dict()
# contests = dict()
# cc, sc, crnt_pts = 0, 0, 0
# while command != 'no more time':
#     command = input()
#     if command == 'no more time':
#         continue
#
#     username, contest, points = command.split(' -> ')
#     points = int(points)
#     if contest not in contests.keys():
#         contests[contest] = {username: points}
#     elif contest in contests.keys():
#         if username not in contests[contest].keys():
#             contests[contest][username] = points
#         elif username in contests[contest].keys() and points > contests[contest][username]:
#             crnt_pts = participation_data[username]
#             contests[contest][username] = points
#     if username not in participation_data.keys():
#         points -= crnt_pts
#         participation_data[username] = points
#     elif username in participation_data.keys():
#         points -= crnt_pts
#         participation_data[username] += points
#     crnt_pts = 0
#
# for contest, user_data in contests.items():
#     cc = 0
#     print(f"{contest}: {len(user_data)} participants")
#     sorted_users_score = sorted(user_data.items(), key=lambda item: item[1], reverse=True)
#     for user, score in sorted_users_score:
#         cc += 1
#         print(f"{cc}. {user} <::> {score}")
#
# sorted_indiviual_standings = sorted(participation_data.items(), key=lambda item: item[1], reverse=True)
# print("Individual standings:")
# for participant, score in sorted_indiviual_standings:
#     sc += 1
#     print(f"{sc}. {participant} -> {score}")
