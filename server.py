import socket
import pickle

# Параметры для протокола Диффи-Хеллмана
p = 23  # Общее простое число
g = 5   # Общий базовый показатель

# Секретный ключ сервера
b = 15
B = (g ** b) % p  # Публичный ключ сервера

# Настройка сервера
HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

# Получение публичного ключа клиента
client_data = conn.recv(1024)
p, g, A = pickle.loads(client_data)

# Отправка публичного ключа сервера клиенту
conn.send(pickle.dumps(B))

# Вычисление общего секрета
K = (A ** b) % p
print(f"Общий секрет (сервер): {K}")

conn.close()
