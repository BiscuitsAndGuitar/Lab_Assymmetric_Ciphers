import socket
import pickle

# Параметры для протокола Диффи-Хеллмана
p = 23  # Общее простое число
g = 5   # Общий базовый показатель

# Секретный ключ клиента
a = 6
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

# Шифрование сообщения
message = "Привет, сервер!"
encrypted_message = ''.join([chr(ord(char) ^ K) for char in message])
sock.send(pickle.dumps(encrypted_message))

# Получение зашифрованного ответа от сервера
encrypted_response = pickle.loads(sock.recv(1024))
decrypted_response = ''.join([chr(ord(char) ^ K) for char in encrypted_response])
print(f"Ответ от сервера: {decrypted_response}")

sock.close()
