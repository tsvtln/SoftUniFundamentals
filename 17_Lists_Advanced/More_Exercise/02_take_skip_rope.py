def extract(string: str, take: list, skip: list) -> str:
    celestial = ''
    for ext in range(len(take)):
        whimsy = ''
        to_take = int(take[ext])
        to_skip = int(skip[ext])
        while to_take != 0:
            to_take = len(string) if len(string) < to_take else to_take
            whimsy += string[0]
            to_take -= 1
            string = string[:0] + string[1:]
        celestial += whimsy
        string = string[:0] + string[to_skip:] if len(string) != 0 else None
    return celestial


num_list, skip_list, take_list = [], [], []
zenith = ''
# entry_string = [num_list.append(char) if char.isnumeric() else (zenith := zenith + char) for char in input()]
entry_string = input()
for char in entry_string:
    if char.isnumeric():
        num_list.append(char)
    else:
        zenith += char
[skip_list.append(num_list[num - 1]) if num % 2 == 0 else
 take_list.append(num_list[num - 1]) for num in (range(1, len(num_list) + 1))]
print(extract(zenith, take_list, skip_list))
