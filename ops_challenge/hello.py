import subprocess

# nmap -sV 10.0.2.4
ip_address = input("what ip/url do you want to scan ")
port = input("what port do you want to scan ")

process = subprocess.Popen(["nmap", "-sV", ip_address])
try:
    process.wait(timeout=3)
except:
    process.kill()

# "telnet ip port"
process1 = subprocess.Popen(["telnet", ip_address, port])
try:
    process1.wait(timeout=3)
except:
    process1.kill()