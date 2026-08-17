import socket
import time

def scan_port(target, port, timeout=0.5):
    """Try to connect to a single port. Return True if it's open."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((target, port))
        return result == 0
    finally:
        s.close()


def main():
    target_input = input("Enter IP address or hostname: ").strip()

    # Resolve hostname to an IP address up front, so we fail with a clean
    # message instead of crashing partway through the scan.
    try:
        target_ip = socket.gethostbyname(target_input)
    except socket.gaierror:
        print(f"Error: could not resolve '{target_input}'. Check the hostname/IP and try again.")
        return

    try:
        start_port = int(input("Start port (default 1): ") or 1)
        end_port = int(input("End port (default 1024): ") or 1024)
    except ValueError:
        print("Error: ports must be numbers.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Error: enter a valid range between 1 and 65535.")
        return

    print(f"\nScanning {target_input} ({target_ip}) — ports {start_port}-{end_port}...\n")

    open_ports = []
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    elapsed = time.time() - start_time
    print(f"\nScan complete in {elapsed:.1f} seconds.")
    print(f"Open ports: {open_ports if open_ports else 'None found'}")


if __name__ == "__main__":
    main()
