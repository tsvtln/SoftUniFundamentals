ppl_in_circle = [int(people) for people in input().split()]
number_k = int(input())
executed_order = []
index = number_k - 1

for execution_list in range(len(ppl_in_circle)):
    for execute in ppl_in_circle:
        if index > len(ppl_in_circle) - 1:
            index %= len(ppl_in_circle)
        # while index < len(ppl_in_circle):
        executed_order.append(ppl_in_circle[index])
        # ppl_in_circle[index] = None
        del ppl_in_circle[index]
        index += number_k - 1

print(f'{executed_order}'.replace(" ", ''))

        # if number_k > len(ppl_in_circle):
        #     number_k_temp = number_k % len(ppl_in_circle)
        # else:
        #     number_k_temp = number_k
        # if ppl_in_circle[number_k] in executed_order:
        #     number_k += 1
        #     if number_k > len(ppl_in_circle):
        #         number_k_temp = number_k % len(ppl_in_circle)
        #     else:
        #         number_k_temp = number_k
        # executed_order.append(ppl_in_circle[number_k_temp])
        # # ppl_in_circle.pop(number_k_temp)
        # number_k += number_k



