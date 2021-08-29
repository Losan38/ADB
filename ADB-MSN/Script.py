import socket
import subprocess as sb
from time import sleep

def Runcommand(cmd):
    command = cmd.split(" ")
    process = sb.run(command,stdout=sb.PIPE)
    OUTPUT = process.stdout
    return OUTPUT
    

def ADB_start():
    _ = Runcommand("sudo adb start-server")
    _ = Runcommand("sudo adb tcpip 5555")
    
def Active_ips():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localip = s.getsockname()[0]
    ip = localip.split(".")
    cmd = "sudo fping -a -s -i1 -g "+ip[0]+"."+ip[1]+"."+ip[2]+"."+"1 "+ip[0]+"."+ip[1]+"."+ip[2]+"."+"255"
    OUT = Runcommand(cmd)
    liveips = OUT.decode().split("\n")
    print("")
    print("-" * 70)
    print("Your IP: ")
    print("        ",localip)
    print("Live IPs: ")
    liveips.pop()
    liveips.remove(localip)
    for index,IP in enumerate(liveips):
    	print("         ",index+1,"- ",IP,sep="")
    return liveips

ADB_start()
Ips = Active_ips()

print("-" * 70)

while True:
    print("")
    Ipindex = input("Choose IP's Index: ")
    print("")
    if Ipindex.isdigit():
        if Ipindex == "999":
            print("")
            iplastdigit = input("Enter the last digit: ")
            ipdigits = Ips[0].split(".")
            ip = ipdigits[0] + "." +  ipdigits[1] + "." + ipdigits[2] + "." + iplastdigit
            print("")
        else:
            ipindex = int(Ipindex)
            ip = Ips[ipindex-1]
        print("")
        print("Selected IP:	",ip) 
        print("")
        break 	
    else:
    	print("")
    	print("Enter Digit")
    	print("")
print("-" * 70)
print("Type in the ADB port or leave it blank for default Port:5555)")
while True:
    print("")
    Port = input("Type in the TCP port: ")
    print("")
    if len(Port) == 0 or Port == " ":
        print("")
        print("Set port to 5555")
        print("")
        port = str(5555)
        break
    elif Port.isdigit():
    	port = Port
    	print("")
    	print("Set port to",port)
    	print("")
    	break
    else:
    	print("")
    	print("Enter Digit")
    	print("")

print("")
print("-" * 70)
print("")

cmd = "sudo adb connect " + ip + ":" + port
OUT = Runcommand(cmd)
print(OUT.decode())	






