positions = list(input().split())
letters_to_numbers = {'a': 0,
                      'b': 1,
                      'c': 2,
                      'd': 3,
                      'e': 4,
                      'f': 5,
                      'g': 6,
                      'h': 7}
position_1 = int(positions[0][1]) - 1, letters_to_numbers[positions[0][0]]
position_2 = int(positions[1][1]) - 1, letters_to_numbers[positions[1][0]]
chess_desk = [0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0]

count_steps = 1
can_step = 0


def one_step(x, y):
    if x < 6:
        if y < 7:
            chess_desk[x + 2][y + 1] = count_steps
        if y > 0:
            chess_desk[x + 2][y - 1] = count_steps
    if x < 7:
        if y > 1:
            chess_desk[x + 1][y - 2] = count_steps
        if y < 6:
            chess_desk[x + 1][y + 2] = count_steps
    if x > 0:
        if y > 1:
            chess_desk[x - 1][y - 2] = count_steps
        if y < 6:
            chess_desk[x - 1][y + 2] = count_steps
    if x > 1:
        if y > 0:
            chess_desk[x - 2][y - 1] = count_steps
        if y < 7:
            chess_desk[x - 2][y + 1] = count_steps



if (position_1[0] % 2 == 1 and position_1[1] % 2 == 1 or position_1[0] % 2 == 0 and position_1[1] % 2 == 0) \
        and (position_2[0] % 2 == 1 and position_2[1] % 2 == 1 or position_2[0] % 2 == 0 and position_2[1] % 2 == 0) \
        or ((position_1[0]+1) % 2 == 1 and position_1[1] % 2 == 1 or (position_1[0]+1) % 2 == 0 and position_1[1] % 2 == 0) \
        and ((position_2[0]+1) % 2 == 1 and position_2[1] % 2 == 1 or (position_2[0]+1) % 2 == 0 and position_2[1] % 2 == 0):
    one_step(position_1[0], position_1[1])
    count_steps = 2
    while chess_desk[position_2[0]][position_2[1]] == 0:
        for i in range(8):
            for j in range(8):
                if chess_desk[i][j] == count_steps - 1:
                    one_step(i, j)
        count_steps += 1
    print(chess_desk[position_2[0]][position_2[1]] // 2)
else:
    print(-1)
