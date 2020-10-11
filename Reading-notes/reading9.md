# PKI - Public Key Infrastructure

- PKI is a technology for authenticating users and devices in the digital world
- Digitally sign documents certifying that a particular cryptographic key belongs to particular user or device.
- The key can be used as an identity for the user
- The users and devices that have keys are often called entities
- The purpose of PKI is to securely associate key with an entity
- The secret key of each entity is only know by that entity and is used for signing which is called `private key`
- `X.509 standards`
    - PKI uses standardized machine readable certificate format for the certificate document.
    - This is called X.509v3
- Common use of certificates
    - Secure Web site - HTTPS
        - Most of the PKI is in SSL certificate 
        - SSL: Secure Sockets Layer
        - TLS: transport layer security: newer version
        - HTTPS ensures that no one can eavesdrop on your connection 
        - For secure communications it is necessary to authenticate the communicating 
    - SSH
        - supports certificates for authenticating hosts and users
        - Tectia SSH uses standard-based X.509
        - OpenSSH uses its own proprietary certificate formats
    - Email Signing and encryption
        - PGP and its free version GNU privacy guard uses their own certificate format and somewhat different trust model
- Security limitation of public key infrastructure
    - the main down side of PKI is that, any certification can sign a certificate for any person or computer
    - The intelligence agencies can use fraudulent certificate for espionage, malware injection, and forging messages or evidence to disrupt or discredit adversaries

---

