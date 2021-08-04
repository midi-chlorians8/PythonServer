dataTestAlerting ="""POST / HTTP/1.1
Host: 18.193.93.213:2000
User-Agent: Grafana
Content-Length: 386
Content-Type: application/json
Accept-Encoding: gzip

{"dashboardId":1,"evalMatches":[{"value":100,"metric":"High value","tags":null},{"value":200,"metric":"Higher Value","tags":null}],"message":"Someone is testing the alert notification within Grafana.","orgId":0,"panelId":1,"ruleId":7751783831957464368,"ruleName":"Test notification","ruleUrl":"http://localhost:3000/","state":"alerting","tags":{},"title":"[Alerting] Test notification"}"""#= client_socket.recv(1024).decode('utf-8')  # Принимаем 1024 байта и декодируем их как строку в utf-8 кодировке

dataMemoryAlerting ="""POST / HTTP/1.1
Host: 18.193.93.213:2000
User-Agent: Grafana
Content-Length: 1131
Content-Type: application/json
Accept-Encoding: gzip

{"dashboardId":2,"evalMatches":[{"value":535699456,"metric":"172.30.0.232:19100_Avaliable","tags":{"__name__":"node_memory_MemAvailable_bytes","instance":"172.30.0.232:19100","job":"Monitoring","nodename":"PROD-MKTG02"}},{"value":593313792,"metric":"172.30.1.223:19100_Avaliable","tags":{"__name__":"node_memory_MemAvailable_bytes","instance":"172.30.1.223:19100","job":"Monitoring","nodename":"ansible-from-legacy-monitorings"}},{"value":290000896,"metric":"172.30.2.131:19100_Avaliable","tags":{"__name__":"node_memory_MemAvailable_bytes","instance":"172.30.2.131:19100","job":"Monitoring","nodename":"PROD-CONTENT"}},{"value":568360960,"metric":"172.30.2.251:19100_Avaliable","tags":{"__name__":"node_memory_MemAvailable_bytes","instance":"172.30.2.251:19100","job":"Monitoring","nodename":"BastionHost-MassageBook-from-legacy-monitorings"}}],"message":"Memory less 3.5gb on pro"""

dataCPUAlerting ="""POST / HTTP/1.1
Host: 18.193.93.213:2000
User-Agent: Grafana
Content-Length: 390
Content-Type: application/json
Accept-Encoding: gzip

{"dashboardId":2,"evalMatches":[{"value":99.71666666666654,"metric":"{instance=\"172.30.1.223:19100\"}","tags":{"instance":"172.30.1.223:19100"}}],"orgId":1,"panelId":14,"ruleId":88,"ruleName":"CPU% Basic alert","ruleUrl":"http://localhost:3000/d/wGHmL2znz/monitorings-with-alerts?tab=alert\u0026viewPanel=14\u0026orgId=1","state":"alerting","tags":{},"title":"[Alerting] CPU% Basic alert"}"""
data = dataCPUAlerting

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

split_data = data.split("\n")  # Нарезаем в массив строк по символу переноса строки
message_string = split_data[len(split_data) - 1].split(",") #[len(split_data)-1] = Последний элемент массива. Счёт с нуля поэтому -1; Нарезаем в массив строк по символу ЗАПЯТАЯ ;

for x in message_string:  # Перебирает все элементы массива и распечатывает
    print(x)  # Перебирает все элементы массива и распечатывает
print("===================\n")

#print( dataCPUAlerting.find('[Alerting] CPU% Basic alert') )

# Парсим на предмет - тестовоя нотификация, превышение cpu, превышение ram
parsing(data)





#stroka = "banana"
#data  = dataTest.find('value')
#print('data:')
#print(data)
