# ISCM with Nagios

## Security Operations Center: Ultimate SOC Quick Start Guide

- Cybersecurity threat is becoming more prominent and is becoming more dangerous and more difficult to detect and mitigate.
- To mitigate, detect and prevent any cyberattack is a purpose of Security Operations Center
- SOC is traditionally a physical facility with an organization
- SOC team are made up of management, security analysts, and sometimes security engineers.
- SOCs are a proven way to improve threat detection, decrease the likelihood of security breaches.
- `CSIRT` computer security incident response team, is responsible for receiving, analyzing, and responding to security incidents.
- CSIRT can work under SOCs or can stand alone
- CSIRT is to minimize and manage damage caused by an incident the CSIRT does not just deal with the attack itself.
    - They also talk to clients,excutives, and the board
- Usually SOC and CSIRT is desirable as a single entity
- Both SOC teams and CSIRT teams use security orchestration, automation, and response tools.
- Collects logs and events from hundreds of security tools and organizational systems and generates actionabl security alerts, which the SOC team can analyze and respond to.
- SOC team has two core responsibilities
    - Maintaining security monitoring tools - Team must maintain and update tools regularly.
    - Investigate suspicious activities - investigate suspicious and malicious activity within the networks and systems
- SOC team has several roles
    - Security analyst - Responsible for detecting potential security threats
    - Security engineer - charge of maintaining and updating tools and systems and is usually a software or hardware specialist.
    - SOC manager - Directs SOC operations, responsible for the SOC team. Responsible for syncing between analysts and engineers, hiring, training, and security strategy.
    - Chief information security officer - establishes security related strategies, policies, and operations. work closely with CEO
    - Director of incident response - responsible for managing incidents in large companies
- SOC analysts are organized in four tiers
    - SIEM alerts flow to Tier 1 analysts who monitor, prioritize and investigate them.
    - Real threats are passed to Tier 2 analysts, who does analysis and decides on a strategy for containment
    - Critical breaches are moved up to a Tier 3 senior analyst, who manages the incdent. Tier 3 analysts are also responsible for actively hunting for threats
    - Tier 4 analyst is SOC manager, in charge of recruitment, strategy, priorities and the direct management of SOC staff
- The benefit of security operation centers 
    - incident response - SOCs operates around the clocks detects and response to the threat
    - Threat intelligence and rapid analysis - Socs use threat intelligence feeds and security tools to quickly address threats
    - Reduce cybersecurity costs - although a SOC represents a major expense, in a long run it reduce the whole some cost of cyber attacks
    - Reduce the complexity of investigations - SOC teams can streamline their investigative efforts. SOC teams have visibility into the network environment so the SOC can simplify the tasks of drilling into logs and forensic information for example.
- Challenges facing security operation centers
    - Increased volumes of security alerts - requires a significant amount of an analysts time. 
    - Management of many security tools- SOC can use more than 20 tools and it can be hard to keep track of and control individually making it important to have a central source and a single platform
    - Resource allocation - staffing or lack of qualified individuals is an issue. Organization may decide to outsource, however, the issue of greater vulnerability that comes with remote working conditions arises. Some organization uses MSSP to help them with their SOC services via outsourcing.
- 5 Steps to setting up your first SOC
    1. Ensure everyone understands what the SOC does
        - SOC checks endpoints and the network of the organization, and isolates and addresses possible security issues
    2. Provides Infrastructure for your SOC
        - Without proper tools given to SOC team, team is bound to fail
    3. Find the right people
    4. Have an incident response plan ready
    5. Defend
- 3 Security Operations center best practices
    1. Detect threats through all stages of an attack
        - Organization must deploy prevention and detection approaches through out the entire attack chain
        - Design the technologies to function together and communicate information
    2. Investigate all alerts to ensure nothing is overlooked
        - Organizations need to develop solutions that not only group alerts but automate investigation and validate them.
    3. Gather forensic evidence for investigation and remediation
        - Organization should find solution for forensics that are simple ot use and automated
- Some of the tools used by SOC
    - Security information and event management (SIEM)
    - Governance, risk and compliance (GRC) systems
    - Vulnerability scanners and penetration testing tools
    - Intrusion detection systems (IDS), intrusion prevention systems (IPS), and wireless intrusion prevention
    - Firewalls and next-generation firewalls (NGFW) which can function as an IPS
    - Log management systems (commonly as part of the SIEM)
    - Cyber threat intelligence feeds and databases

---

# Introduction to Nagios Monitoring Tool
- Nagios is monitoring tool for monitoring the network in several ways.
- Nagios is capable of monitoring the server and find the performance drop.
1. Services offered
    - Nagios operates in Linux so that it can be monitored for UNIX operating systems.
    - Various types of network services can be monitored, including SMTP,HTTP,POP2, SNMP, NNTP, SSH, FTP
2. Importance of Nagios
    - Server can be continuously monitored to check for security and performance issues. 
    - Tools support many different programming languages that can b identified in network and application. 
3. Nagios Features 
    - Easily find the issues present in-network.
    - manages the log and database system.
    - Provides informative web interface and easy to use interface so that network can be monitored easily.
    - When there is crash in the app, it will notify user to take immediate action
    - Bottleneck can be identified by Nagios
    - Tools offer continuous monitoring options
    - tool can monitor many network services
    - Provides failover capability and continuous monitoring so that performance can be stable.
4. Nagios Architecture
    - It is like client server type architecture.
    - nagios monitoring provides different plugins and provides intelligence so that the network can be host by Nagios core.
5. Nagios Benefits
    - Tool help to increase availability of services, server, app, and process so that user can use to monitor the network.
    - Server failover can be easily detected