import re

filter = (r"(?P<front_group>.*)>(?P<group_one>\d+)\|(?P<group_two>"
          r"[a-z]+)\|(?P<group_three>[A-Z]+)\|(?P<group_four>.+[^<>])<(?P<end_group>.*)")

receive_inputs = int(input())
for receive in range(receive_inputs):
    get_password = input()
    check_password = re.search(filter, get_password)
    if check_password:
        if check_password.group('front_group') == check_password.group('end_group'):
            print(f"Password: {check_password.group('group_one')}"
                  f"{check_password.group('group_two')}"
                  f"{check_password.group('group_three')}"
                  f"{check_password.group('group_four')}")
        else:
            print("Try another password!")
    else:
        print("Try another password!")
