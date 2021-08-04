# ===================================== SERVER =====================================
# Код принимает сообщение с локальной Grafana через hook. Парсит. Решает повторяется ли прошлое сообщение или нет.
# По мотивам видео: https://www.youtube.com/watch?v=f5ic6D30_mQ
# Autor: Mister I
# 03.08.2021

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаём обьект сервер который пользует сокет.
#server.bind(('127.0.0.1', 2000))  # Привязываем сервер к ip и порту
server.bind(('0.0.0.0', 2000))  # Привязываем сервер к ip и порту
server.listen(4)  # Слушаем 4 входящих соединения
print('Working...')

# Logical variables ============
count = 0  # Cтартовое значение
old_data = 'first'
new_data = 'second'
# Logical variables ============
# ===================================== SERVER =====================================





# ===================================== Jira =====================================

#https://id.atlassian.com/manage-profile/security/api-tokens
#curl -v https://playsdev.atlassian.net --user dobryjsok60@gmail.com:XaJFElW8LewGF1GJOWQ8AF8B
#Test PlaysDev
#30.04.2021

from jira import JIRA

jira_options = {'server': 'https://playsdev.atlassian.net'}
#jira = JIRA(options=jira_options, basic_auth=(login, api_key))
jira = JIRA(options=jira_options, basic_auth=('dobryjsok60@gmail.com', 'XaJFElW8LewGF1GJOWQ8AF8B'))

def printInfoJiraissue(): #From Test
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, ')  # Press Ctrl+F8 to toggle the breakpoint.
    issue = jira.issue('LAB-55')

    summary = issue.fields.summary  # 'Field level security permissions'
    description = issue.fields.description
    # comment2 = issue.fields.comment
    print(summary)
    print(description)

def createIssueToMelnikov(priority,description):
    # priority = 'Low'
    issue_dict = {
        'project': {'key': 'LAB'},
        'summary': 'New issue from jira-python',
        'description': description, # 'Look into this one'
        'issuetype': {'name': 'Bug'},
        'labels': ['2book', 'python-author'],
        'priority': {'name': priority},  # Работает. Ставит приоритет.
        'assignee': {'accountId': "609cd2615998a60068f5959f"},  # неработает
    }
    new_issue = jira.create_issue(fields=issue_dict)

def parsing(data):
    if data.find('[Alerting] Test notification') > -1:
        descriptionTask = "[Alerting] Test notification"
        print(descriptionTask)
        return descriptionTask
    elif data.find('Memory less') > -1:
        descriptionTask = "Ram Alarm"
        print(descriptionTask)
        return descriptionTask
    elif data.find('title":"[Alerting] CPU% Basic alert') > -1:
        descriptionTask = "CPU% Basic alert"
        print(descriptionTask)
        return descriptionTask
    else:
        descriptionTask = "Not parsed"
        print(descriptionTask)
        return descriptionTask

# ===================================== Jira =====================================



while True:  # В цикле бесконечном слушаем и печатаем входящие данные
    client_socket, address = server.accept()  # Тут задержка программы пока не придут данные на сокет. Сокет - програмный интерфейс приаттаченный к порту
    data = client_socket.recv(1624).decode('utf-8')  # Принимаем 1624 байта и декодируем их как строку в utf-8 кодировке

    # ============= Инкримент вход сообщений. Нужен для обработки повторов
    count = count + 1
    print("count:")
    print(count)
    # ============= Инкримент вход сообщений. Нужен для обработки повторов

    print('\n=========================\n')
    print(data)

    split_data = data.split("\n")  # Нарезаем в массив строк по символу переноса строки

    # print("split_data:")
    # print(split_data)

    # print("split_data[0]:")
    # print(split_data[0])

    # print("split_data[7]:")
    # print(split_data[7],'\n')

    # messadge_string = split_data[7].split(",")  #Нарезаем в массив строк по символу ЗАПЯТАЯ
    # message_string = [0, 1, 2]
    message_string = split_data[len(split_data) - 1].split(
        ",")  #  [len(split_data)-1] = Последний элемент массива. Счёт с нуля поэтому -1; Нарезаем в массив строк по символу ЗАПЯТАЯ ;
    print("\nmessage_strings [all] :")
    # print(messadge_string[0])
    # print(len(messadge_string) )    #len() тут кол во элементов в массиве
    for x in message_string:  # Перебирает все элементы массива и распечатывает
        print(x)  # Перебирает все элементы массива и распечатывает
    print("===================\n")


    # Парсим на предмет - тестовоя нотификация, превышение cpu, превышение ram
    if data.find('title') > -1:
        count = data.find('title')       +len("title") +3
        count2 = data.find('}', count) -1
        # count += len("title") +3
        #print('count:')
        #print(count)
        #print(data[count:count+25])
        #print("===================\n")
        print(data[count:count2])
        descriptionTask=data[count:count2]
    else:
        descriptionTask = "Not parsed"
    # Cоздание вопроса в Jira
    createIssueToMelnikov(priority="High", description=descriptionTask)
    # Cоздание вопроса в Jira

print('shutdown this shit...')




# Обработка повторяемости. Не работает. Разный ruleId":8240654365311143909
#if count % 2 == 0:
#    new_data = message_string
#
#else:
#    old_data = message_string

#if new_data == old_data:
#    print("Povtor!")
#else:
#    print("Net Povtora")
#    print(old_data)
#    print(new_data)
# Обработка повторяемости
