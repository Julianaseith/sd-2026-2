import socket

HOST, PORT = "127.0.0.1", 5001

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Digite mensagens (ou 'sair'):")

while True:
    msg = input("> ")

    if msg == "sair":
        break

    s.sendto(msg.encode(), (HOST, PORT))

    dado, endereco = s.recvfrom(1024)

    print("eco:", dado.decode())

s.close()