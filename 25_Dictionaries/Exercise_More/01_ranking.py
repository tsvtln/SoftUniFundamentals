contests_data, participants_data = dict(), dict()
receive_contests_data, receive_participants = '', ''
max_points, max_user = 0, ''


def calculate_total_points(user_data: dict):
    total_points = 0
    for contest_points in user_data.values():
        total_points += contest_points
    return total_points


while receive_contests_data != 'end of contests':
    receive_contests_data = input()
    if receive_contests_data == 'end of contests':
        continue
    contest, password = receive_contests_data.split(':')
    contests_data[contest] = password

while receive_participants != 'end of submissions':
    receive_participants = input()
    if receive_participants == 'end of submissions':
        continue
    participants = receive_participants.split('=>')
    if participants[0] in contests_data.keys():
        if participants[1] == contests_data[participants[0]]:
            contest = participants[0]
            password = participants[1]
            username = participants[2]
            points = int(participants[3])
            if username not in participants_data.keys():
                participants_data[username] = {contest: points}
            elif username in participants_data.keys():
                if contest not in participants_data[username]:
                    participants_data[username][contest] = points
                elif contest in participants_data[username] and points > participants_data[username][contest]:
                    participants_data[username][contest] = points


for user, points in participants_data.items():
    total_points = calculate_total_points(points)
    if total_points > max_points:
        max_points, max_user = total_points, user
print(f"Best candidate is {max_user} with total {max_points} points.\nRanking:")
sorted_users = sorted(participants_data.items())
for user, score in sorted_users:
    print(user)
    sorted_contests = sorted(score.items(), key=lambda item: item[1], reverse=True)
    for contest, points in sorted_contests:
        print(f"#  {contest} -> {points}")
