# Data file encryption

- CIA triad is and how you can apply B2B data transfer
- Confidentiality: way of business to restrict access to or knowledge of certain pieces of information to certain individuals.
    - Main in the middle attack to eavesdrop on a transmission or hack directly into a server
    - Coutermeasure to mitigate cyber attack to prevent any access to the data
- Integrity: Preventing dtat from being tampered. 
    - preventing unauthorize user to temper with data
    - cna prevent man-in-middle attack
- Availability: 
    - power interruption, network interruption, server failures, missing files, DDoS attacks and nautral disaster are just some of the many unfortunate events that can cause data inaccessible
- Encryption is a example of keeping data unreadable thereby preserving that data's confidentiality
- Data-in-transit encryption can be done through SSL and data-at-rest can be done through OpenPGP
- To retain integrity of the data, hash functions and digital signatures can be used to keep the file secure
- You can set-up two or more server in such a way that they are both active servers. Also known as active-active high availability configuration
- CIA triad in one
    - Data-in-motion encryption through secure file transfer protocols like FTPS, SFTP, HTTPS, WebDAVs, AS2 over HTTPS, and OFTP (secured by SSL)
    - Data-at-rest encryption through OpenPGP 
    - End-to-end encryption, which can be achieved through automation-enabling features known as triggers. 
    - 2-factor authentication
    - Data integrity checking mechanisms that employ hash functions and digital signatures.
    - Built-in support for High Availability configurations, active-active and active-passive
    Data Loss Prevention (DLP), which automatically detects the presence of sensitive data and take appropriate action (e.g. cancel the download or apply encryption)