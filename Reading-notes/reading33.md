# Malware Analysis with PEStudio

- Windows binary are packaged into portable executable, PE.
- Identify the hash value, strings and library imports to draw some conclusion based on our past experience.
- PeStudio is all in ne tool that analyze Portable Executables.
- In the PeStudio, there is XML file that carries all of the blacklisted items.
- PeStudio can query VirusTotal to see if the malware passes the test.
- Drag and drop analysis to see if the file is malware
- If the file is packed knowing the packer can help identify how to unpack the file.
- ASLR is a feature which simple loads an applictation into memory at somewhat randomized preventing the ability to successfull perform buffer overflow attack.
- Data execution prevention (DEP) code execution from the data section in memory
- 