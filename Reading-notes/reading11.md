# Network Packet Analysis with Wireshark

- Wireshark is a great tools to capture network packets.
- All of the packets that arrive at network card goes through validation stage to see if packet is arrived at correct destination.
- If the destination match, the packets are destined f your PC and will be passed up to the CPU and processed.
- If the destination address in the packet does not match the address of the network card the packet will simply be ignored and discard.
- If you want to grab stuff that others are sending to each other, you've got a porblem.
- If you want to tell your wireshark, you want to except everything, you want to use `Promiscuous Mode`
- Monitor mode is also is another monitor mode that you can use to see radio information
- YOu can use npcap instead of WinPCAP to sniff the data packet.
- Why you are not seeing the packet in promiscuous mode is because they are connected to switches.
- Switches make sure that packet that doesn't belong is not going to the network card
- `SPAN port` is a switch port analyzer using mirror and monitor ports, simply by monitoring and mirroring the packet

```
Switch(config)#monitor session 1 source interface gigabitEthernet 1/3 both
Switch(config)#monitor session 1 destination interface gigabitEthernet 1/24
```

- To configure, you need you need really good switch with admin previlege.
- To see unencrypted protocols 
     - go to the packet you want to analzye and right click -> follow -> TCP stream
- TO you can get a access to the temp key by using Session key log file or private key of the server
- Both of getting the key is going to hard task and only way to decrypt is using WireShark which will be through RSA
- Each of the line on the bottom shows the layer of internet request
- when there is full drop after incline on the graph it is packet drop for 3 ACK then when it climbs up again it goes through fast recovery
- Slow start comes up when there is a drop and wait
     - increase exponentially growth after packet drop