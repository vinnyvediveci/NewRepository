#!/usr/bin/python

import os
from sys import argv


# argv to input user and group potentially
username = argv[1]
groupname = argv[2]
os.system("sudo useradd " + username)
os.system("sudo groupadd " + groupname)
os.system("sudo usermod -g " + groupname + username)
os.system("sudo chmod 700 " + groupname)
os.system("sudo su - " + username)
os.system("ssh-keygen")




