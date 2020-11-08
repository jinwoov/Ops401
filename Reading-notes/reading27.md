# Adding Data Sources with Splunk SIEM

## Getting data into Splunk from Windows endpoints

- Universal forwarder: The most efficient way to collect data is to use universal forwarder.
- Registery monitoring can be done using forwarder
- Universal forwarder offers more scalability than WMI.
- WMI utilize methods of access which is considered insecure with well understood exploitation
- Due to the vulnerability and scalability, splunk is recommend for forwarder
- The best practice is not windows specific but what is unique to Windows is installation user interface.
- Initial things to consider before deploying Splunk
    - Authentication: Splunk enterprise must run s a user with credentials to access those machine
    - Disk bandwidth: Splunk needs a lot of disk I/O bandwidth. Configure anti virus to avoid monitoring Splunk Enterprise directories.
- To install the universal forwarder with a static configuration
    - You don't need to configure later
