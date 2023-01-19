#!/usr/local/bin/python3

import socket, struct, requests, sys, re
keyinput = ""

def showoptions():
        print("back backspace down enter forward home info left literal play power InstantReplay reverse right search select up volumedown volumemute volumeup")

while(keyinput != "quit"):
	keyinput = input("Which button?")
	if keyinput == "show":
		showoptions();
	else:
		url = 'http://' + '192.168.1.4' +':' + '8060'+ '/keypress/' + keyinput
		requests.post(url, timeout=2)
