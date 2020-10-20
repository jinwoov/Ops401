take the network ip and cidr block
- network address
- broadcast address

255.255.255.0
if it is 10.10.0.0/24
1-254

255 broadcast address, so its not valid address
network address: 10.10.0.0

Host values 10.10.0.1 ~ 10.10.0.254 class C

Subnet mask of 255.255.0.0 CDR /16 Class B

- IDS:
    - internet -> Firewall -> router -> switch -> computer
                                               -> IDS (watches this network)

        <---------------------------------------->

    - 192.168.0.0/24 
    - can watch AD/DC 
    - Can have IDS watch entire network or one specific device
    - Baseline network
    - IDS can call out something that doesn't belong there
    - how often do you want to have IDS alert you

- NIDS
    - Snort
    - Detection and watching the network and detect whats happening
    - if there is endpoint that is inside of the topology then firewall can't detect 
    - you can get eyes on different endpoints 
    - 
- IPS
    - Most similar to firewall
    - Internet -> firewall -> IPS => Router => Switch -> endpoint
    - Halts it so that rest of the hierchy doesn't get this signal
    - 
- HIDS
    - Hardware intrusion system