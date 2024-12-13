import argparse
from port_scan import scan_ports
from service_detection import detect_services
from vulnerability_check import check_vulnerabilities
from web_vuln_check import check_https_headers
from report import generate_report

def main():
    parser = argparse.ArgumentParser(description="Network Vulnerability Scanner")
    parser.add_argument("--target", required=True, help="Target IP or domain to scan")
    parser.add_argument("--ports", default="1-1024", help="Port range to scan (e.g., 1-1024)")
    parser.add_argument("--web", action="store_true", help="Enable web vulnerability scanning")
    args = parser.parse_args()
    
    target = args.target
    port_range = args.ports
    web_scan = args.web

    print(f"Scanning target: {target}")
    print(f"Port range: {port_range}")

    open_ports = scan_ports(target, port_range)
    print(f"Open Ports: {open_ports}")

    services = detect_services(target, open_ports)
    print(f"Detected Services: {services}")

    vulnerabilities = check_vulnerabilities(services)
    print(f"Vulnerabilities: {vulnerabilities}")

    web_vulnerabilities = []
    if web_scan:
        print("Performing web vulnerability scan...")
        web_vulnerabilities = check_https_headers(target)
        print(f"Web Vulnerabilities: {web_vulnerabilities}")

    generate_report(target, open_ports, services, vulnerabilities, web_vulnerabilities)
    print("Report generated successfully!")

if __name__ == "__main__":
    main()
