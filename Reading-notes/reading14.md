# Amazon Virtual Private Cloud

- VPC traffic mirroring is a Amazon VPC features that you can  use to copy the network traffic
- out of band security and monitoring appliance for
    - Content inspection
    - Threat monitoring
    - Troubleshooting
- Target: destination for mirrored traffic
- Filter: A set of rules that defines that traffic that is copied a traffic mirror session
- Session: An entity that describes Traffic Mirroring from a source to target using filter
- Working traffic mirroring
- Traffic Mirroring benefits
    - Simplified operation: Mirror any ranges of your VPC traffic without having to manage packet
    - Enhance security: Capture packets at the elastic network interface
    - Increased monitoring options: Send your mirrored traffic to any security device
- How traffic mirroring works
    - It copies incoming and outgoing traffic from the network interfaces that are attached to your Amazon EC2 instance
- Traffic mirror targets is the destination for mirrored traffic.
    - A network interface
    - A network Load balancer
- A traffic mirror filtered
    - a set of inbound and outbound traffic rules that define the traffic that is copied from the traffic mirror source
    - Traffic mirror filter rules
        - some of the parameter includes: traffic direction, action, protocol, source port range, source CIDR block and destination CIDR block
    - Traffic mirror session
        - a traffic mirror source
        - a traffic mirror target
        - a traffic mirror filter
    - if you want to send multiple traffic mirror session n the same source
- Example of creating a traffic mirror session policy
```json
{
 "Version": "2012-10-17",
 "Statement": [
    {
        "Effect": "Allow",
        "Action": "ec2:CreateTrafficMirrorSession",
        "Resource": [
        "arn:aws:ec2:*:*:traffic-mirror-target/tmt-12345645678",
        "arn:aws:ec2:*:*:traffic-mirror-filter/*",
        "arn:aws:ec2:*:*:network-interface/*"
        ]
    }
 ]
}
```
- 