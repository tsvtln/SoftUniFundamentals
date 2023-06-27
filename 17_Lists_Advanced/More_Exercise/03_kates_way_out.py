"""WIP"""


def escape(maze):
    moves = 0
    for index, move in enumerate(maze):
        pass


def possibility_to_escape(maze):
    POSSIBLE = False
    for row in maze:
        for char in row:
            if ' ' in char:
                POSSIBLE = True
                break
        if POSSIBLE:
            break
    return POSSIBLE


def empty_cells(maze):
    cells_list = []
    for empty in maze:
        if ' ' in empty:
            for index, cell in enumerate(empty):
                if cell == ' ':
                    cells_list.append(index)
            break
    return cells_list


def fnd_kate(maze):
    index_kate = 0
    index_row = 0
    for index, find_kate in enumerate(maze):
        if 'k' in find_kate:
            index_row = index
            for index_, kate in enumerate(maze[index_row]):
                if 'k' in kate:
                    index_kate = index_
    return index_kate, index_row


rows_in_maze = int(input())
maze_structure = []
for m in range(rows_in_maze):
    line = input()
    maze_structure.append(line)
print(fnd_kate(maze_structure))
