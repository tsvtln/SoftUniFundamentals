number_of_commands = int(input())
parking_data = dict()
for cars in range(number_of_commands):
    use_parking = input().split()
    if use_parking[0] == 'register':
        username, license_plate_number = use_parking[1], use_parking[2]
        if username in parking_data.keys():
            print(f"ERROR: already registered"
                  f" with plate number {parking_data[username]}")
        else:
            parking_data[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif use_parking[0] == 'unregister':
        username = use_parking[1]
        if username not in parking_data.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_data[username]

for user, license_plate_number in parking_data.items():
    print(f"{user} => {license_plate_number}")

