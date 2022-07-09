def game(c):  # Функция переноса введённых координат на поле
    x, y = list(map(int, c))
    if not all(x.isdigit() for x in c) or x < 0 or (x not in default_coord) or (y not in default_coord):
        print('Введены неверные координаты!')
        m_print(filed)
        return
    global count
    if filed[y + 1][x + 1] == '-':
        if count:
            filed[y + 1][x + 1] = '0'
            m_print(filed)
            count -= 1
        else:
            filed[y + 1][x + 1] = 'X'
            count += 1
            m_print(filed)
    else:
        print('\n', 'Клетка занята, или не является игровым полем!')
        m_print(filed)
    return filed


def m_print(b):  # Печать игрового поля
    for i in b:
        print(' '.join(i))


def check():  # Проверка условий победы
    global result
    if filed[1][1] == filed[2][2] == filed[3][3] and filed[1][1] != '-':
        if filed[1][1] == '0':
            print('Победа ноликов!')
            result = True
        else:
            print('Победа крестиков!')
            result = True
    if filed[3][1] == filed[2][2] == filed[1][3] and filed[3][1] != '-':
        if filed[3][1] == '0':
            print('Победа ноликов!')
            result = True
        else:
            print('Победа крестиков!')
            result = True
    for i in filed[1:]:
        if i[1] == i[2] == i[3] and i[1] != '-':
            if i[1] == '0':
                print('Победа ноликов!')
                result = True
                break
            else:
                print('Победа крестиков!')
                result = True
                break
    for j in range(3):
        if filed[1][j + 1] == filed[2][j + 1] == filed[3][j + 1] and filed[1][j + 1] != '-':
            if filed[1][j + 1] == '0':
                print('Победа ноликов!')
                result = True
                break
            else:
                print('Победа крестиков!')
                result = True
                break

    if not result and '-' not in [*filed[0], *filed[1], *filed[2], *filed[3]]:
        print('Ничья!')
        result = True


filed = [[' ', '0', '1', '2'], ['0', '-', '-', '-'], ['1', '-', '-', '-'], ['2', '-', '-', '-']]  # Создание поля
m_print(filed)

count = 0
result = False
default_coord = [0,1,2]

while not result:
    if count:
        print("Куда поставить нолик?")
        a = tuple(input("Введите координаты точки через запятую ").split(','), )
        print('\n')
        game(a)
        check()
    else:
        print("Куда поставить крестик?")
        a = tuple(input("Введите координаты точки через запятую ").split(','))
        print('\n')
        game(a)
        check()
