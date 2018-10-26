#!/usr/bin/python
#./install
import os


pid = open('public/pid.txt', "r").read()

os.kill(int(pid), 15)

