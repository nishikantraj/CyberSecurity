import socket
import termcolor


def scan(targets, ports):
    print('\n','** Scanning for '+targets +":")
    for port in range (1,ports):
        scan_ports(targets,port)

def scan_ports(ipaddress, ports):
    try:
        sckt = socket.socket()
        sckt.connect((ipaddress,ports))
        print(termcolor.colored(('[+]'),'green')+" Port Opened "+str(ports))
        sckt.close()
    except:
        pass

targets = input("[*] Enter Targets to Scan(for multiple scan separate them by comma): ")
ports = int(input("[*] How many ports you want to Scan: "))

if ',' in targets:
    print(termcolor.colored(('\n[*] Scanning multiple targets:'),'green'))
    for target in targets.split(','):
        scan(target.strip(),ports)
else:
    scan(targets.strip(),ports)