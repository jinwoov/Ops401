# Cloud incident response in AWS EC2

- Historically, company that didn't have plan for EC2 lost valuable data and risked not being able to fully contain the incident.
- Being able to detect outside threat and creating a remediation plan quickly is something org has to think about.
- Minimizing and containment is another thing one should consider. 
- Mitigiation of the weakness. It is crucial to know your org and the enemy. 
- Restoration is a final step. Being able to solve the problem before restoring is the key to prevent future attack
- `Incident`: any violation of policy, law, or unacceptable act that involves information assets, such as computers, network, smartphones, tablets, voice recording systems, cameras and etc
- Downloading and installing software involves in event. 
- Operating Systems supported EC2 supports Linux
- Webserver: connected to the public internet responsible for displaying the site images and interacting with your customers
- Application server: open connection with your payment processor.
- Database Server: where your data for customer and payment information may resides.
## The incident
- Sites was configured Linux,Apache, MySQL, PHP (LAMP)
- secret SSH was generated to authenticate the protect and communication channel.
- IT management decide that default account for developers would be "root"
