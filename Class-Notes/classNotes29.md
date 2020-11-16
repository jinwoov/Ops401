hypothesis: a theory of suspecting the problem
threat hunter: the whole purpose is to head off and sit on the network and make the consistent server
weakest spot: where the weak spots are 
- malware attack vector: get in and spread
- threat actor : what do they do.

CYCLE

- Create a hypothesis
- investing using the tools and techniques
- Uncover new patterns and TTP
- Inform and Enrich Analytics

- looking for a sign that TTP 
- brute force
    - multiple authentication attempt and failure
- Detecting the TTP using Wireshark
- How to attempt to create a C2


- IoC: gif file
- Black list domain
- Behaioral antivirus, detect the change
- File becoming encrypted

- C2 server
    - Russia to infiltrate to cloud

- Beaconing
    - the process of having the minion asking the C2 server to check in
    - meterpreter is a sign that you look for
    - find it to 

- beacon with many things is strobe

- Rita
    - perform network analysis
    - Real intelligence threat analysis
    - 
- DNS tunneling detection: packets that sent to DNS server can be manipulated
- Load rita first and then zeek
- open source 
- Zeek: network security monitoring tool aka Bro

sniffer can be any way of tools
- Pcap -> zeek -> zeek logs

- conn.log
- dns.log - DNS request and responses
- https.lg
- SSL.log


show-beacons - what hosts are beaconing
show-exploded-dns: expose dns covert
show-long-connections longconnections
show-strodesstrobes
show-useragents: useragents