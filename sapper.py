import random
import sys


def startGame():
    print("\033[31mДобро пожаловать в игру сапер .... Давайте взорвем всех лошадок\033[0m")
    player_field = []
    for _ in range(9):
        row = ['\033[32m*\033[0m'] * 9
        player_field.append(row)

    mines_field = []
    for _ in range(9):
        row = ['\033[32m \033[0m'] * 9
        mines_field.append(row)

    mines = 0
    while mines < 10:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if mines_field[x][y] != '\033[32m@\033[0m':
            mines_field[x][y] = '\033[32m@\033[0m'
            mines += 1

    print('\033[32m   ' + '   '.join([str(i + 1) for i in range(9)]) + '         ' + '   ' + '   '.join([str(i + 1) for i in range(9)]) + '\033[0m')
    print('\033[32m  ' + '─' * 37 + '      ' + '  ' + '─' * 37 + '\033[0m')
    for i in range(len(player_field)):
        row_player = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(['\033[32m' + cell + '\033[0m' for cell in player_field[i]]) + ' \033[32m│\033[0m      '
        row_mines = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(['\033[32m' + cell + '\033[0m' for cell in mines_field[i]]) + ' \033[32m│\033[0m'
        print('\033[32m' + row_player + row_mines + '\033[0m')
        print('\033[32m' + '  ' + '─' * 37 + '      ' + '  ' + '─' * 37 + '\033[0m')

    while True:
        user_input = input("\033[31mВведите координаты (например, w1): \033[0m")
        if len(user_input) != 2:
            print("Ошибка.")
            continue

        column = int(user_input[1]) - 1
        row = ord(user_input[0].upper()) - 65

        if column < 0 or column >= 9 or row < 0 or row >= 9:
            print("Ошибка.")
            continue

        if player_field[row][column] != '\033[32m*\033[0m':
            print("Эта ячейка уже открыта!")
            continue

        if mines_field[row][column] == '\033[32m@\033[0m':
            player_field[row][column] = '\033[31m!\033[0m'
            print('\033[31mбум бах! Игра окончена.\033[0m')
            sys.exit()
        else:
            count = countAdjacentMines(mines_field, row, column)
            player_field[row][column] = str(count) if count > 0 else ' '

        closed_cells = sum(row.count('\033[32m*\033[0m') for row in player_field)
        if closed_cells == mines:
            print("Поздравляю! Вы открыли все ячейки без мин. Вы победили!")
            sys.exit()

        print('\033[32m   ' + '   '.join([str(i + 1) for i in range(9)]) + '         ' + '   ' + '   '.join([str(i + 1) for i in range(9)]) + '\033[0m')
        print('\033[32m  ' + '─' * 37 + '      ' + '  ' + '─' * 37 + '\033[0m')
        for i in range(9):
            row_player = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(['\033[32m' + cell + '\033[0m' for cell in player_field[i]]) + ' \033[32m│\033[0m      '
            row_mines = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(['\033[32m' + cell + '\033[0m' for cell in mines_field[i]]) + ' \033[32m│\033[0m'
            print('\033[32m' + row_player + row_mines + '\033[0m')
            print('\033[32m' + '  ' + '─' * 37 + '      ' + '  ' + '─' * 37 + '\033[0m')


def countAdjacentMines(field, row, column):
    count = 0
    for i in range(max(0, row - 1), min(row + 2, 9)):
        for j in range(max(0, column - 1), min(column + 2, 9)):
            if field[i][j] == '\033[32m@\033[0m':
                count += 1
    return count


startGame()

