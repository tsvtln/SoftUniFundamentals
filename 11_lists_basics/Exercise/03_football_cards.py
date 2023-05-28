team_A = ["A-" + str(s) for s in range(1, 12)]
team_B = ["B-" + str(s) for s in range(1, 12)]
GAME = True
cards = input().split(' ')
for player in range(len(cards)):
    if cards[player] in team_A:
        team_A.remove(cards[player])
    elif cards[player] in team_B:
        team_B.remove(cards[player])
    else:
        continue
    if len(team_A) < 7 or len(team_B) < 7:
        GAME = False
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if not GAME:
    print("Game was terminated")
