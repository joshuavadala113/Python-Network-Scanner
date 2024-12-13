import nmap

def detect_services(target, ports):
    nm = nmap.PortScanner()
    services = {}
    for port in ports:
        nm.scan(target, str(port))
        service_name = nm[target]['tcp'][port]['name'] if 'tcp' in nm[target] and port in nm[target]['tcp'] else "unknown"
        services[port] = service_name
    return services
