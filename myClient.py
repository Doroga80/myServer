import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connection Data
host = '217.25.94.158'
port = 55555

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = input('')
        if message.startswith('@'):  # Check if it's a command or a message
            client.send(message.encode('ascii'))
        else:
            client.send('{}: {}'.format(nickname, message).encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
