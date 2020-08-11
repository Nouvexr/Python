#!/usr/bin/python
import socket
import sys

if len(sys.argv) = 3:
	print "use: python EnumSMTP.py IP usuario"
	sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1],25)) #necessario passar o endereço
banner = s.recv(1024)
print banner

s.send("VRFY "+sys.argv[2]+ "\r\n") #necessario passar o nome do usuario
r = s.recv(1024)
print r
