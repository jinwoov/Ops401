# Malware Traffic Analysis with Wireshark

- A software that designed to inflitrate or damage a computer system without the owner's informed consent.
- Malware can change their behavior and its source code slightly and behave differently to affect the computer.
- WastedLocker is a malware that attaches the word "wasted" to each encrypted file.
- The objective of malware analysis
    1. Breakdown the malware
        - Understanding the source code and the behavior is important to block malware entry and stop the spread.
    2. It investigates its characteristics
        - How does it spread and how fast does it replicate and TTP for camouflaging. 
        - Knowing this information help with mitigation
    3. Unravels its functionality
        - Malware will typically wait in hiding until the right time.
        - By doing an analysis, you can tell when this malware will execute.
    4. Traces the malware origin
        - Malware analysis aims to analyze adversary's IP, geographic location or even an organization.
    5. predict the impact
        - Enables company to plan and deploy mitigation steps.
- Malware analysis job is increasing due to these reasons.
- Malware analysis steps
    1. capture the malware
        - Use honeypot to attract adversary
    2. Build malware lab
        - Use things like VMS
    3. Install your tools
        - Cuckoo sandbox and other equivalent analysis enablers.
    4. Record Baseline
        - Creating a base line to make sure that each iteration is same is important
    5. Commerce your investigation
        - Take the malware apart before initiating these phases.
    6. Document the results
        - Document in detail what outcome you got. 
- Type of Malware analysis
    - static malware analysis
        - Quick static analysis reveals enough information needed to create an indicator
        - Indicator of compromise (IOC)
    - dynamic malware analysis
        - Running the malware will cause critical damage to its host
        - Dynamic malware analysis planform(DMA) is built by computer incident response center Luxembourg (CIRCL) to perform this type of analysis.
    - Manual Malware analysis
        - Analysis often reveals the strategic intent behind the malicious software.
        - Known as code reversing
        - break down code manually
    - Automated malware analysis
        - Automation can generate detailed reports and feeds data into an incdient response system.
- Key stages of Malware analysis