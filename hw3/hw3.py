# Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.



def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)


def move_X(board):
    nX = int(input('Куда поставить X? (необходимо ввести номер ячейки): '))
    board[nX-1] = 'X'
    return board


def move_0(board):
    n0 = int(input('Куда поставить 0? (необходимо ввести номер ячейки): '))
    board[n0-1] = '0'
    return board


def check_win(board) -> bool:
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        draw_board(board)
        print('Игра окончена, есть победитель!')
        return True
    else:
        return False


def play_game(i=0):
    board = list(range(1, 10))
    while check_win(board) == False:
        if i < 4:
            draw_board(board)
            move_X(board)
            if check_win(board) == True:
                break
            move_0(board)
            if check_win(board) == True:
                break
            i += 1
        else:
            draw_board(board)
            print('Ходов больше нет! Начните игру заново')
            break


play_game()