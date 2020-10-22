ICMP ping
- echo request to the target destinatinon IP
- ICMP echo request
- firewall block ICMP

![ICMP](./assets/icmp.png)

ARP: Address resolution protocol
- Totally different behavior
    - switch -> .1
            -> .2
            -> .3
if I know that there is .2 
- ARP is on same subnet
- When you arp you will get table of different devices
- Switch with multiple computer that Arping all of the devices
    - packet storm
    - 
- OPs challenge
    - ARPing the subnet
    - just output psitive

--- 
Cloud Security
- physical security controls - control access
- Some of the settings are in default
- Default and instance security configuration
- shared responsibility
    - business critical instance
- how you access it, VPN, Key pairs.
- NIST - has to be compliant to the regulation
- Database
- Elasticity
- private cloud vs public cloud vs hybrid cloud
    - private

- types 
    - IaaS: infrastructure as a service
    - SaaS
    - PaaS


VPC
- AWS
    - shared cloud with others
    - Linux
    - how do i separate myself from others
    - virtual private cloud
    - build our lan topology
- VPC separates network
- cloud -> firewall -> router -> switch -> endpoints 3
` IP chicken`
- public IP 
- Elastic IP
    - failing to assigning 
    - Gateway - internet gateway
- if you forget to assign gateway
    - there is no route to out side
- deploy VPC
    - recommend 172.31.0.0/16 <-- class B
    - AWS recommend class B
        - Each VPC needs subnet and subnet
            - they will have CIDR block will have 24
            - 172.31.1.0/24 <--- last octet
    - if the routing is messed up then it will be messed up
        - 