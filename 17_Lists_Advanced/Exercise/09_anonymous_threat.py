sequence = input().split()
command = ''
while command != '3:1':
    command = input()
    if command == '3:1':
        continue
    command, start_index, end_index = command.split()
    if command == 'merge':
        start_index, end_index = int(start_index), int(end_index)
        start_index = max(0, start_index)
        end_index = min(len(sequence) - 1, end_index)
        if start_index >= end_index:
            continue
        resulting_list = []
        for merge in range(start_index, end_index + 1):
            resulting_list.append(sequence[merge])
            # sequence.pop(merge)
        # resulting_list.reverse()
        for remove in range(end_index, start_index - 1, - 1):
            sequence.pop(remove)
        # if len(resulting_list) > 0:
        sequence.insert(start_index, ''.join(resulting_list))

    elif command == 'divide':
        index = int(start_index)
        partitions = int(end_index)
        element = sequence[index]
        divider = len(element) // partitions
        resulting_list_div = []

        # elements_list = [char for char in sequence[index]]
        string = ''
        for i in range((partitions - 1) * divider):
            string += element[i]
            if len(string) == divider:
                resulting_list_div.append(string)
                string = ''
        string = ''
        for z in range((partitions - 1) * divider, len(element)):
            string += element[z]
        resulting_list_div.append(string)
        sequence.pop(index)
        #
        # sequence.insert(index, ' '.join(resulting_list_div))
        for j in range(len(resulting_list_div)):
            sequence.insert(index + j, resulting_list_div[j])
print(' '.join(sequence))
