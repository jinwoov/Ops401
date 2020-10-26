# Threat Analysis, Cyber Kill-Chain, and Stuxnet

## Breaking the Kill-Chain: A Defensive Approach

- Developed by Lockheed Martin
- The 7 sequential steps:
    1. [Reconnaissance](#Reconnaissance)
    2. [Weaponization](#Weaponization)
    3. Delivery
    4. Exploitation
    5. Installation
    6. Command and Control
    7. Actions on Objectives
- To disrupt the attack, few steps above must be misaligned to fail.
- To do that you need to know about the play book.
- NIST cybersecurity framework will be a good reference


## Reconnaissance

- Gathering information about the victim.
- There are two stages of reconnaissance which are passive and active
- During the passive phase, attacker will gather victim's information by WHOIS, ARIN registration, Google, Shodan, Job Listings and company website
- After attacker have gained enough infromation, they will move into active phase
- During this phase, attacker will be actively probe victim's computer by actively looking for open ports and services.
- Defending ourselves can be done by limiting our information online and job postings.
- The first line of defense is to close any unused ports and services.
- `Honeypots` is great way to distract attacker and divert attention away from real valuable information.
- Firewall with IPS capabilities will provide filtering and segmentation and also monitor port scans and banner grabbing
- The entire

## Weaponization
- Once the attacker found the weakness, next step is to create the attack that will exploit the vulnerability
- Weapons include:
    - Metasploit
    - Veil framework
    - Social Engineering
- `Patch managment` is used to cover any attack
- Office macros, javascript and browser are all common avenue for an attacker to exploit.
- Endpoint and network edge malware protection

## Delivery 
- Attacker can deliver their weapon through websites
- Social media platform: cat phishing via social networks
- User input: using webserver or database
- Email: attackers love phishing email
- USB: common attack to leave the USB in public area
- User awareness is the single best defense against delivery
- DKIM and SPF are email auth method to check if its spoofed email.

## Exploitation
- During the exploitation phase, attacker has penetrated to the victim's computer.
- The exploit can come as buffer overflow, SQL injection, malware, that was undetected. 
- DEP (Data Execution Prevention): a software and hardware feature which attempts to prevent the execution of code
- Some of the post infection tool include sandbox, EDR, or a SIEM to find indicator of compromise.
- This is not the finale, as ultimate goal of attacker is to gain full access.

## Installation
- inject a payload that will give more access to the attacker 
- DLL hijacking
- Registry changes to make my program autmatically startup

## Command and Control
- system has been completely compromise