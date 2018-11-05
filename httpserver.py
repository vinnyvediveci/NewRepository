#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import os
import socket
import json
import signal



# create info.json
os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/public")
info = {
    "host_name": socket.gethostname(),
    "version": 1
}
with open('info.json', 'w') as outfile:
    json.dump(info, outfile)

#get pid of server
pid = open("pid.txt", "w")
pid.write(str(os.getpid()))
print("process working")

pid.close()

# configure and run the server
PORT = 9000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print(socket.gethostname())
httpd.serve_forever()


pid = open('public/pid.txt', "r").read()
os.kill(int(pid), 15)



#put new process into install folder





