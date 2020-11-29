# Scanning and Enumeration with NMAP

- NMAP is a powerful tool allows it to monitor all of the open ports, os and software versions.
- NMAP can be misused and ethically one should prevent themselves from doing so.
- It will report what port is open and should not be accessible by external network.
## Basic Scans

```sh

$ namp -sn `subnet`

$ nmap `specific ip endpoint`

```
- useful flags
    - `-sS` scanning flag for Nmap
    - `-T` timing that range from 0 to 5.
    - 0 is slowest and 5 being the fastest and most overt.
    - `-iL` multiple targets 
    - `-F` uses common 100 ports
    - `-O` operating system scan
    - `--open` only scan for port that is open
    - `-sV` allows you to get as detailed infromation as possible about the services running on a machine
    - `-p` ports scan
    - `-p-` scan every ports
    - `-A` all ports
    - 


```sh
## scanning multiple IPs using the text file
$ vim ~/Documents/targets.txt
192.168.1.4
192.168.1.10
192.168.1.35
192.168.1.102
192.168.1.128

$ nmap -sS -T4 -iL /home/user/Documents/targets.txt

# logging the output
$ nmap -sS -p- -oN  Documents/full-scan.txt 192.168.7.105

```
