#!/usr/bin/python
import socket
from colorama import Fore

ip = raw_input("Target IP: ")
for porta in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((ip, porta)) == 0:
                print (Fore.GREEN)
                print "[+] Port",porta,"is Opened"
                s.close()
