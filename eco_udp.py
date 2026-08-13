import socket

HOST, PORT = "127.0.0.1", 5001

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

print(f"[udp] ouvindo em {HOST}:{PORT}", flush=True)

while True:
    dado, endereco = s.recvfrom(1024)

    print(f"[udp] recebi {dado!r} de {endereco}", flush=True)

    s.sendto(dado, endereco)