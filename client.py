import socket
import pickle
import os

# Загрузка или генерация ключей
if os.path.exists("client_private_key.txt"):
    with open("client_private_key.txt", "r") as f:
        a = int(f.read())
else:
    a = 6  # Секретный ключ клиента
    with open("client_private_key.txt", "w") as f:
        f.write(str(a))

# Параметры для протокола Диффи-Хеллмана
p = 23  # Общее простое число
g = 5   # Общий базовый показатель

A = (g ** a) % p  # Публичный ключ клиента

# Подключение к серверу
HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

# Отправка публичного ключа серверу
sock.send(pickle.dumps((p, g, A)))

# Получение публичного ключа сервера
server_data = sock.recv(1024)
B = pickle.loads(server_data)

# Вычисление общего секрета
K = (B ** a) % p
print(f"Общий секрет (клиент): {K}")

sock.close()
