# 29.07.2021
# Код принимает сообщение с локальной Grafana через hook. Парсит. Решает повторяется ли прошлое сообщение или нет.
# По мотивам видео: https://www.youtube.com/watch?v=f5ic6D30_mQ
# Autor: Mister I

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Создаём обьект сервер который пользует сокет.
server.bind(('127.0.0.1',2000)) #Привязываем сервер к ip и порту
server.listen(4) #Слушаем 4 входящих соединения
print('Working...')

# Logical variables ============
count = 0 #Cтартовое значение
old_data = 'first'
new_data = 'second'
# Logical variables ============

while True: #В цикле бесконечном слушаем и печатаем входящие данные
    client_socket, address = server.accept() #Тут задержка программы пока не придут данные на сокет. Сокет - програмный интерфейс приаттаченный к порту
    data = client_socket.recv(1024).decode('utf-8') #Принимаем 1024 байта и декодируем их как строку в utf-8 кодировке

    # ============= Инкримент вход сообщений. Нужен для обработки повторов
    count=count+1
    print("count:")
    print(count)
    # ============= Инкримент вход сообщений. Нужен для обработки повторов

    print('\n=========================\n')
    print(data)

    split_data = data.split("\n") #Нарезаем в массив строк по символу переноса строки

    #print("split_data:")
    #print(split_data)

    #print("split_data[0]:")
    #print(split_data[0])

    #print("split_data[7]:")
    #print(split_data[7],'\n')

    #messadge_string = split_data[7].split(",")  #Нарезаем в массив строк по символу ЗАПЯТАЯ
    message_string = split_data[len(split_data)-1].split(",")  # Нарезаем в массив строк по символу ЗАПЯТАЯ ; [len(split_data)-1] = Последний элемент массива. Счёт с нуля поэтому -1
    print("message_strings [all] :")
    #print(messadge_string[0])
    #print(len(messadge_string) )   #len() тут кол во элементов в массиве
    for x in message_string:        #Перебирает все элементы массива и распечатывает
        print(x)                    #Перебирает все элементы массива и распечатывает

    #Обработка повторяемости. Не работает. Разный ruleId":8240654365311143909
    if count % 2 == 0:
        new_data = message_string

    else:
        old_data = message_string

    if new_data == old_data:
        print("Povtor!")
    else:
        print("Net Povtora")
        print(old_data)
        print(new_data)
    #Обработка повторяемости

print('shutdown this shit...')
