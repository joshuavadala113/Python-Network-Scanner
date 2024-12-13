from datetime import datetime

def generate_report(target, open_ports, services, vulnerabilities, web_vulnerabilities):
    report = f"""
    Network Vulnerability Report
    Target: {target}
    Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    
    Open Ports:
    {open_ports}
    
    Detected Services:
    {services}
    
    Vulnerabilities:
    {vulnerabilities}
    
    Web Vulnerabilities:
    {web_vulnerabilities if web_vulnerabilities else 'Web scan not performed'}
    """
    with open(f"{target}_report.txt", "w") as file:
        file.write(report)
