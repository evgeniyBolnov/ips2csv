import os


def main():
    login = 'admin'
    passw = 'admin'
    ip_count = 50
    path_to_inp_file = 'c:\\test\\IPs.txt'
    path_to_out_file = 'c:\\test\\ip_out_'
    print('Использовать стандартные настройки?\nДа[y]/Нет[n]')
    if input() != 'y':
        select = menu()
        while select != 0:
            if select == 1:
                os.system('cls')
                print('Логин = ', end='')
                login = input()
            elif select == 2:
                os.system('cls')
                print('Пароль = ', end='')
                passw = input()
            elif select == 3:
                os.system('cls')
                print('Путь до входного файла = ', end='')
                path_to_inp_file = input()
            elif select == 4:
                os.system('cls')
                print('Путь до выходного файла = ', end='')
                path_to_out_file = input()
            elif select == 5:
                os.system('cls')
                print('Количество IP в файле = ', end='')
                ip_count = int(input())
            select = menu()

    file = open(path_to_inp_file, 'r')

    k = 0
    j = 1

    for line in file:
        csv = open(path_to_out_file + str(j) + '.csv', 'a')
        temp = '"' + str(k) + '_ip","0","' + line[
                                             0:-1:1] + '","8000","0","' + login + '","' + passw + '","0","1","0","0"' + '\n'
        csv.write(temp)
        k += 1
        if k % ip_count == 0:
            j += 1
        csv.close()

    file.close()
    print('Готово')
    print('Press any key to continue...')
    input()


def menu():
    os.system('cls')
    print('Что меняем?', end='\n')
    print('[1] Логин', end='\n')
    print('[2] Пароль', end='\n')
    print('[3] Путь до входного файла', end='\n')
    print('[4] Путь до выходного файла', end='\n')
    print('[5] Количество IP в файле')
    print('[0] Выполнить', end='\n')
    return int(input())


if __name__ == '__main__':
    main()
