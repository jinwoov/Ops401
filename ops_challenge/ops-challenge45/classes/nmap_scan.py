import nmap
from time import sleep


def scanUni(ip_add, port_range, nmap_mode, t_u):
    scanner = nmap.PortScanner()
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_add, port_range, nmap_mode)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_add].state())
    if(t_u == "t"):
        print("Open Ports: ", scanner[ip_add].all_tcp())
    else:
        print("Open Ports: ", scanner[ip_add].all_udp())

def get_os(ip_add, port_range):
    nm = nmap.PortScanner()
    print(nm.scan(ip_add, arguments="-O")["scan"][ip_add]["osmatch"][0]["name"])

def nmap_interface():
    print("Nmap Automation Tool")
    print("--------------------")

    ip_addr = input("IP address to scan: ")
    print("The IP you entered is: ", ip_addr)
    type(ip_addr)

    resp = input("""\nSelect scan to execute:
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Get Operating System Info            \n""") ### TODO: Select what your third scan type will be
    print("You have selected option: ", resp)


    ### TODO: Prompt the user to type in a port range for this tool to scan
    port_r = input("What port range do you want to scan? (ie. 1-10)")
    port_r = port_r.replace(" ", "")

    if resp == '1':
        scanUni(ip_addr, port_r, "-v -sS", "t")
    elif resp == '2':
        scanUni(ip_addr, port_r, "-v -sU", "u")
    else:
        get_os(ip_addr, port_r)
