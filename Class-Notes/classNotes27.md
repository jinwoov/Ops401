SIEM Data pipeline

- topology
- process
- data flow
- SIEM is doing data input

1 data input => 2. data storage (parsing, indexing) => 3. Data searching

readable 
SIEM will attach meta data
- host name
- source
- source data type
- Time stamp 
- 
Parsing
- 


Splunk components
- forwarder <--- Windows server 2019
    1. Universal
    2. Heavy

- Indexer <---splunk ubuntu
    1. parser, indexer
- Head <-- browser
    1. Search Head
        - just searching keyword
    2. Search peer
        - search result and indexing

- splunk is like SQL database

- Forwarder: universal subtype of forwarder send the data from
- indexer: sort it/ parse it
- Sysmon: event log
    - sends those out some where else

- forwarder
- forwarder
- forwardr


- Windows server -> splunk ubunutu -> 