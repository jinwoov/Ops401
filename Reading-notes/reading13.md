# Cloud Architecture Security

- VPC stands for virtual private cloud which is a virtual data center in the cloud.
- VPC gives full control on virtual networking environment, selection of own private IP.
- The benefit of having VPC is that it helps in aspects of cloud computing, privacy, security and preventing loss of proprietary data.
- `subnet`: a subnet is a dividing a large network into smaller network
- `Route Table`: table containing a set of rules called routes which determine where traffic ha to be directed.
- `IGW`: internet gateway is both hardware and software that provides private network with route to the world outside. Only one gateway can be attached to a VPC.
- `NAT`: network address translation maps private IP address to the public address on the way out and vice versa.
- `Security group`: set of firewall rules. Cannot create a rule to deny on AWS.
- `Customer Gateway`: is a VPC VPN connection links your data center to your Amazon VPC (virtual private cloud). It can be physical or software appliance.
- `Virtual private gateway` - In AWS, you can create a virtual private gateway and attach it to the VPC from which you want to create the VPN connection
- `VPC peering` - allows you to route traffic between two VPC using IPv4 and 6 private address. You can create VPC connection through your own VPC to AWS VPC.
- `Network Access Control Lists` - NACL is optional layer of security for your VPC that controls traffic in and out of ne or more subnets. 

--- 

## AWS VPC

- AWS management console - provides web interface that you can use to access your VPC
- AWS command line interface (CLI) - provides commands for a broad set of AwS services
- AwS SDKs - provides language specific API
- Query API - provides low level API actions that you can make HTTPS request. 