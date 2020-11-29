# Reconnaissance

- Penetration test is also known as a pen test.
- web application firewall (WAF).
- pentest involves breaching of any number of application system.
- to uncover vulnerabilities such as unsensitized inputs that susceptible to code injection
- Five stages of pen testing
    1. Planning and reconnaissance
    - Defining the scope and goals of a test
    - Gathering intelligence
    2. scanning
    - Static analysis: it behaves while running.
    - dynamic analysis: inspecting an applications code in running state.
        - it provides a real time view into an app performance
    3. gaining access
        - XSS, sql injection and backdoors to uncover target's vulnerability
    4. Maintaining access
        - imitate APT persistence often remains for several months
    5. Analysis WAF configuration
        - compile detailed reports
        - sensitive data that was accessed
        - Amount of time the pen tester was able to remain in the system undetected.
- Penetration testing methods
    - External testing
        - The goal is to gain access and extract valuable data
    - Internal testing
        - tester with access to an application behind its firewall simulates an attack by a malicious insider.
    - Blind testing
        - only given the name of the enterprise
    - Double blind testing
        - security personnel have no prior knowledge
    - Targeted testing
        - keep each other appraised of their movements. This is valuable training exercise that provides a security team with real time feedback.
- Pen testing and WF are exclusive
    - WAF admin can benefit from pen testing data. Using this information WAF configuration can be updated to secure against the weak spot discovered in the test.
     