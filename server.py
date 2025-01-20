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

# Получение зашифрованного сообщения от клиента
encrypted_message = pickle.loads(conn.recv(1024))
decrypted_message = ''.join([chr(ord(char) ^ K) for char in encrypted_message])
print(f"Сообщение от клиента: {decrypted_message}")

# Шифрование ответа
response = "Привет, клиент!"
encrypted_response = ''.join([chr(ord(char) ^ K) for char in response])
conn.send(pickle.dumps(encrypted_response))

conn.close()
