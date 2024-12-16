# **Network Vulnerability Scanner**

## **Overview**  
The **Network Vulnerability Scanner** is a Python-based tool designed to detect vulnerabilities in networks and web applications. It scans for open ports, identifies running services, checks for known vulnerabilities using CVEs, and evaluates basic web security configurations. A detailed report is generated after every scan.

---

## **Features**  
1. **Port Scanning**: Scans a range of ports to identify open ports.  
2. **Service Detection**: Identifies services running on the detected open ports.  
3. **Vulnerability Checking**: Maps services to known vulnerabilities using CVE data.  
4. **Web Vulnerability Testing**: Checks for missing HTTP security headers and outdated SSL/TLS configurations.  
5. **Comprehensive Reporting**: Creates a detailed report of the findings in a text file.  

---

## **Getting Started**  

### **Requirements**  
- Python 3.8 or higher  
- Operating System: Linux, Windows, or macOS  
- Active Internet connection (for vulnerability checks and web scans)  

### **Dependencies**  
Install the required Python libraries using the `requirements.txt` file:  
```bash
pip install -r requirements.txt
```

## **How to Use**
1.  Run the scanner with a target IP or domain:
    ```bash
    python scanner.py --target <TARGET_IP_OR_DOMAIN> --ports <PORT_RANGE>
    ```  
2.  To include web vulnerability scanning:
    ```bash
    python scanner.py --target <TARGET_DOMAIN> --ports <PORT_RANGE> --web
    ```
3.  View the reports in the `reports` directory.

## **WARNING**
**Use responsibly and only with authorization**. Unauthorized scanning, penetration testing, or vulnerability scanning without permission may be illegal and could result in legal consequences. Always have explicit permission from the network or system owner before running any scanning tools.
