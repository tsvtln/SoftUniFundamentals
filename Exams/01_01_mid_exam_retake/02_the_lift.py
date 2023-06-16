def place_people(queue: int, current_state: list):
    for fill in range(len(current_state)):
        spots = current_state[fill]
        while spots != 4 and queue != 0:
            queue -= 1; spots += 1; current_state[fill] += 1
    ES = True if current_state[-1] < 4 else False
    NES = True if queue > 0 else False
    result_queue = ' '.join(str(elem) for elem in current_state)
    return result_queue, queue, ES, NES


entry_queue = int(input())
entry_state = [int(x) for x in input().split()]
entry_state, entry_queue, ESR, NESR = place_people(entry_queue, entry_state)

print(f"The lift has empty spots!\n{entry_state}") if ESR else None
print(f"There isn't enough space! {entry_queue} people in a queue!\n{entry_state}") if NESR else None
print(entry_state) if not ESR and not NESR else None
