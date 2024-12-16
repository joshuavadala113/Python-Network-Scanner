

# **Network Vulnerability Scanner**

## **Overview**  
The **Network Vulnerability Scanner** is a Python-based tool designed to detect vulnerabilities in networks and web applications. It performs an in-depth analysis of target systems, including scanning for open ports, identifying running services, cross-referencing known vulnerabilities (CVEs), and evaluating web security configurations. The tool aims to provide actionable insights to improve network and web application security. A detailed report is generated after each scan, summarizing the findings and highlighting potential risks.

This tool is ideal for cybersecurity professionals, penetration testers, and IT administrators looking for a lightweight and customizable vulnerability scanner.

---

## **Features**  
1. **Port Scanning**:  
   - Scans a range of ports to identify open ones.
   - Provides details about commonly used ports for quick analysis.

2. **Service Detection**:  
   - Identifies services running on detected open ports (e.g., HTTP, SSH).  
   - Extracts service versions for additional insights.  

3. **Vulnerability Checking**:  
   - Maps detected services and versions to known vulnerabilities using CVE data.  
   - Cross-references data from reliable vulnerability databases like Vulners.  

4. **Web Vulnerability Testing**:  
   - Evaluates web servers for missing HTTP headers such as `Strict-Transport-Security` and `Content-Security-Policy`.  
   - Analyzes SSL/TLS configurations for deprecated protocols and weak ciphers.  

5. **Comprehensive Reporting**:  
   - Outputs findings into a structured, easy-to-read text report.  
   - Highlights critical vulnerabilities, open ports, and misconfigurations.  

6. **Extensibility**:  
   - Modular code structure allows users to customize or extend specific functionality.  
   - Ideal for developers who want to integrate additional features.  

---

## **Getting Started**  

### **Requirements**  
To ensure compatibility, ensure you have the following:  
- Python 3.8 or higher  
- Compatible Operating System (Linux, Windows, macOS)  
- Active Internet connection (required for CVE lookups and web vulnerability checks)  

### **Dependencies**  
Install the required Python libraries using the `requirements.txt` file:  
```bash
pip install -r requirements.txt
```

### **Setup**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/joshuavadala113/network-vuln-scanner.git
   cd network-vuln-scanner
   ```  

2. Install the dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Test the installation by running a sample scan:  
   ```bash
   python scanner.py --target localhost --ports 1-1024
   ```

### **Command-Line Arguments**  
The scanner supports the following arguments for flexible usage:  
| Argument          | Description                                          | Example                          |  
|-------------------|------------------------------------------------------|----------------------------------|  
| `--target`        | Specify the target IP address or domain              | `--target 192.168.1.1`           |  
| `--ports`         | Define the port range to scan                        | `--ports 1-65535`                |  
| `--web`           | Enable web vulnerability scanning                   | `--web`                          |  
| `--output`        | Specify the output file for the report               | `--output results.txt`           |  

---

## **Additional Notes**  
- **Target Scope**: Ensure you have explicit permission to scan the target system. Unauthorized scanning can violate laws and organizational policies.  
- **Performance**: For large port ranges or multiple scans, ensure sufficient system resources are available to avoid delays.  
- **Customization**: Advanced users can modify the scripts to include additional scanning modules or extend existing features.

---
