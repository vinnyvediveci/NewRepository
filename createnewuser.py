#!/usr/bin/python

import os


#argv to input user and group potentially

os.system("sudo useradd marcus")
#os.system("sudo groupadd newgroup")
os.system("sudo usermod -g newgroup marcus")
os.system("sudo chmod 700 newgroup")
os.system("sudo su - marcus")
os.system("ssh-keygen")


