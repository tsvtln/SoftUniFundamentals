import numpy as np
from array import array
from sys import maxsize as maxnum

initial_list = [int(x) for x in input().split(' ')]
command = []
resulting_list = []
CONTINUE = True

while CONTINUE:
    command = input()
    if command == 'end':
        CONTINUE = False
        continue
    else:
        command = command.split(' ')

    # Exchange logic
    if command[0] == 'exchange':
        exchange_value = int(command[1])
        if exchange_value + 1 > len(initial_list) or exchange_value < 0:
            print('Invalid Index')
        else:
            # for exchange in range(len(initial_list) // 2):
            resulting_list.append(initial_list[exchange_value + 1:])
            # for exchange in range(len(initial_list) // 2):
            # exchange_value = int(command[1])
            resulting_list.append(initial_list[:exchange_value + 1])
            resulting_list = sum(resulting_list, [])
            initial_list = [int(x) for x in resulting_list]
            # print(initial_list)
            resulting_list.clear()

    # Max even/odd logic
    elif command[0] == 'max':
        if command[1] == 'even':
            array_list = np.array(initial_list)
            even_mask = array_list % 2 == 0
            if even_mask.any():
                ipme = 0  # index position max even
                mne = 0  # max number even
                for length_of_list in range(len(initial_list)):
                    # for find_index in initial_list:
                    if initial_list[length_of_list] % 2 == 0:
                        if initial_list[length_of_list] > mne:
                            mne = initial_list[length_of_list]
                            ipme = length_of_list
                print(ipme)
            else:
                print('No matches')

        elif command[1] == 'odd':
            array_list = np.array(initial_list)
            odd_mask = array_list % 2 == 1
            if odd_mask.any():
                ipmo = 0  # index position max odd
                mno = 0  # max number odd
                for length_of_list in range(len(initial_list)):
                    # for find_index in initial_list:
                    if initial_list[length_of_list] % 2 == 1:
                        if initial_list[length_of_list] > mno:
                            mno = initial_list[length_of_list]
                            ipmo = length_of_list
                        # if index_position < find_index:
                        #     index_position = find_index
                print(ipmo)
                # odd_arr = array_list[odd_mask]
                # max_odd_index = odd_arr.argmax()
                # print(np.where(odd_mask)[0][-1])
                # max_odd_index_output = np.where(odd_mask)[-1][max_odd_index]
                # print(np.where(odd_mask)[0][max_odd_index])
                # print(np.where(odd_mask)[0][-1])
                # print(max_odd_index_output)
            else:
                print('No matches')

    # Min even/odd logic
    elif command[0] == 'min':
        if command[1] == 'even':
            if command[1] == 'even':
                array_list = np.array(initial_list)
                even_mask = array_list % 2 == 0
                if even_mask.any():
                    index_min_num_even = 0
                    min_num_even = maxnum
                    for length_of_list in range(len(initial_list)):
                        if initial_list[length_of_list] % 2 == 0:
                            if initial_list[length_of_list] < min_num_even:
                                min_num_even = initial_list[length_of_list]
                                index_min_num_even = length_of_list
                    print(index_min_num_even)
                else:
                    print('No matches')

        elif command[1] == 'odd':
            array_list = np.array(initial_list)
            odd_mask = array_list % 2 == 1
            if odd_mask.any():
                index_min_num_odd = 0
                min_num_odd = maxnum
                for length_of_list in range(len(initial_list)):
                    if initial_list[length_of_list] % 2 == 1:
                        if initial_list[length_of_list] < min_num_odd:
                            min_num_odd = initial_list[length_of_list]
                            index_min_num_odd = length_of_list
                print(index_min_num_odd)
            else:
                print('No matches')

    # First even/odd logic
    elif command[0] == 'first':
        count = int(command[1])
        if count > len(initial_list):
            print('Invalid count')
        else:
            result_first = []
            if command[2] == 'even':
                while count != 0:
                    for cycle_list in initial_list:
                        if cycle_list % 2 == 0:
                            result_first.append(cycle_list)
                            count -= 1
                        if count == 0:
                            break
                        if cycle_list == initial_list[-1]:
                            count = 0
                print(result_first)

            elif command[2] == 'odd':
                while count != 0:
                    for cycle_list in initial_list:
                        if cycle_list % 2 == 1:
                            result_first.append(cycle_list)
                            count -= 1
                        if count == 0:
                            break
                        if cycle_list == initial_list[-1]:
                            count = 0
                print(result_first)

    # Last even/odd logic:
    elif command[0] == 'last':
        count = int(command[1])
        if count > len(initial_list):
            print('Invalid count')
        else:
            count = int(command[1])
            if command[2] == 'even':
                last_even = []
                for cycle_list in initial_list:
                    if cycle_list % 2 == 0:
                        last_even.append(cycle_list)
                if len(last_even) > count:
                    last_even = last_even[len(last_even) - count:]
                print(last_even)
                last_even.clear()

            elif command[2] == 'odd':
                last_odd = []
                for cycle_list in initial_list:
                    if cycle_list % 2 == 1:
                        last_odd.append(cycle_list)
                if len(last_odd) > count:
                    last_odd = last_odd[len(last_odd) - count:]
                print(last_odd)
                last_odd.clear()

print(initial_list)
