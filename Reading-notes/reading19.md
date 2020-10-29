#  Threat Modeling with DFDs, STRIDE

- STRIDE framework
    - Spoof, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
    - This framework was to design to proactively limit threats as you build your systems.
- Spoofing: When someone claims to be a person or system they are not
    - Single key: many API uses single key authentication.
        - The value is static
        - Anyone who obtain the key has access to the systems
    - Access token: A value that authenticates a request. Access is limited in a way that it is available for short period.
    - Signature: Each request is signed by shared secret that you can verify.
- Tampering: Not only the data is vulnerable, physical machines or hardware may also be vulnerable.
    - Firewall and partitioned storage are among the technique that you can use to have data not overwritten
- Repudiation: Takes aim at your auditing and tracing.
    - All events with security importance should be logged
    - often repudiation is intertwined with other STRIDE components
- Information Disclosure: Any sensitive information being disclosed. Disclosure can be caused by backups and other file left in accessible location.
- Denial of service: Overloading the system with incoming requests, making it impossible for user to connect.
- Elevation of Privilege: When attacker extend their role from user to admin.