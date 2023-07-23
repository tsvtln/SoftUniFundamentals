data_players = {}
COMMON_POSITION = False
command = ''

while command != 'Season end':
    command = input()
    if command == 'Season end':
        continue

    if ' -> ' in command:
        command = command.split(' -> ')
        player, position_input, skill = command[0], command[1], int(command[2])

        if player not in data_players:
            data_players[player] = {position_input: skill}
        elif position_input not in data_players[player] or skill > data_players[player][position_input]:
            data_players[player][position_input] = skill

    elif ' vs ' in command:
        command = command.split(' vs ')
        player_one, player_two = command[0], command[1]

        if player_one in data_players and player_two in data_players:
            # Check for common positions
            for position in data_players[player_one].keys():
                COMMON_POSITION = False
                if position in data_players[player_two].keys():
                    COMMON_POSITION = True
                    break
            if COMMON_POSITION:
                pts_player_one = sum(data_players[player_one].values())
                pts_player_two = sum(data_players[player_two].values())

                if pts_player_one > pts_player_two:
                    del data_players[player_two]
                elif pts_player_two > pts_player_one:
                    del data_players[player_one]

# Sort players by total skill in descending order and by name in ascending order
sorted_players = sorted(data_players.items(), key=lambda x: (-sum(x[1].values()), x[0]))

for player, positions in sorted_players:
    sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))
    print(f"{player}: {sum(positions.values())} skill")
    for pos, skill in sorted_positions:
        print(f"- {pos} <::> {skill}")
