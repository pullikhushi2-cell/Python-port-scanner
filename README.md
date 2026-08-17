# Python Port Scanner

A simple TCP port scanner written in Python, built while learning
networking and cybersecurity fundamentals.

## What it does

Given an IP address or hostname and a port range, the script checks
each port by attempting a TCP connection, and reports which ones are
open.

## Requirements

No third-party packages — uses only Python's built-in `socket` and
`time` modules.

## Usage

```bash
python scanner.py
```

You'll be prompted for:
- Target IP address or hostname (e.g. `127.0.0.1` or `scanme.nmap.org`)
- Start port (defaults to 1 if left blank)
- End port (defaults to 1024 if left blank)

### Example output

```
Enter IP address or hostname: scanme.nmap.org
Start port (default 1): 20
End port (default 1024): 100

Scanning scanme.nmap.org (45.33.32.156) — ports 20-100...

Port 22 is OPEN
Port 80 is OPEN

Scan complete in 12.3 seconds.
Open ports: [22, 80]
```

## What I learned

- How the `socket` module works for TCP connections
- The basics of ports and how connect-scanning works
- Handling bad input (unresolvable hostnames, invalid ranges) without crashing

## Possible future improvements

- [ ] Multi-threading to scan faster
- [ ] Banner grabbing to identify the service running on each open port
- [ ] Export results to a file (CSV/JSON)
- [ ] Command-line arguments instead of interactive prompts

## Disclaimer

This tool is for educational purposes only. Only scan hosts and
networks you own or have explicit permission to test. Unauthorized
port scanning may be illegal in your jurisdiction.
