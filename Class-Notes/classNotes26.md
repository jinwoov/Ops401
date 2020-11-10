Standard input: stdin
standard output: stdout
standard error: stderr

data stream

create a output that has an error

- CIRT: computer incident response team
- Cloud CIRT: cloud CIRT <-- Top Stakeholder 
- Availability incident: due to system being down and data is not available.
- Cloud CIRT: put together.

- IR lifecycle
1. Preparation
2. Detection & analysis
3. Containment, radiation, recovery
4. Post-incident activities.

- SQRRL automation maturity model
    - 0 -> 1 -> 2 -> 3-> 4
    initial               
    - how automated is it?
    - 0: automated, no collection in place
    - 1: some data collection, some threat intelligence searches
    - 2: Procedures, data collection
    - 3: innovative: create new data
        - high level of data collection
    - 4: leading, wants the company to be
        - heavily automated, data collection
    - different company has different level maturity
- SIEM: Security information event management
    - The mission to create a birds eye view for infrastructure
    - SIEM server: aggregate all of the data into server
    - Event and log collection
    - layered views
    - normalization
        - to make it same timezone and data is not agreeing with each other
        - system has own version of reality
        - you can normalize the data
    - Correlation
        - If one flag raises and other department raises then it can correlate
    - Adaptability
        - How scalable is your solution.
        - Kiwi syslog
    - Reporting/alerting
    - log management
    - Ingest: to take in
    - Digest: to break it down
    - accept data from anything

### SIEM 
- Logs
- send it logs over a port #
- Event collection
- Devices & logs
- Security onions has suricata and SIEM
- Dedicated ports

### NIDS
- packets sniffing
- Promiscuous dedicated network interface
- Dedicated sniffing port
- Baseline network activities
- Packets and IP

- Unify the endpoints log
- 