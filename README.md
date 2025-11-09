# SSH Device Simulator

A simple SSH server that simulates a network device with CLI interface.

## Features

- SSH server with password authentication
- Simple CLI interface with common network device commands
- Simulated device information and interface status
- Multi-client support with threading

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the SSH server:
   ```bash
   python main.py
   ```

2. Connect from another terminal:
   ```bash
   ssh admin@localhost -p 2222
   ```

   **Login credentials:**
   - Username: `admin`
   - Password: `admin`

3. Use custom port (optional):
   ```bash
   python main.py 2223
   ```

## Available CLI Commands

Once connected, you can use these commands:

- `help` or `?` - Show available commands
- `show version` - Display device version information
- `show interfaces` - Display interface status
- `show interface <name>` - Display detailed interface information
- `show system` or `show system uptime` - Display system uptime
- `show system information` - Display hardware inventory
- `show system processes` - Display running processes
- `show system storage` - Display filesystem information
- `exit` or `quit` - Exit the session

## Example Session

```
$ ssh admin@localhost -p 2222
admin@localhost's password: admin

Welcome to Simulated JUNOS Device

JUNOS-MX> show system uptime

Current time: 2025-11-09 14:30:42 UTC
Time Source:  LOCAL CLOCK 
System booted: 2025-10-25 07:18:00 UTC (2w1d 07:12 ago)
Protocols started: 2025-10-25 07:19:32 UTC (2w1d 07:11 ago)
Last configured: 2025-11-08 14:25:33 UTC (1d 00:05 ago) by admin
 2:30PM  up 15 days,  7:12, 1 user, load averages: 0.23, 0.18, 0.15

JUNOS-MX> show interfaces

Interface Status:
--------------------------------------------------
Interface       Status   Description              
--------------------------------------------------
ge-0/0/0        up       Gigabit Ethernet         
ge-0/0/1        down     Gigabit Ethernet         
ge-0/0/2        up       Gigabit Ethernet         
lo0             up       Loopback Interface       

JUNOS-MX> exit
Goodbye!
```

## Notes

- The server runs on localhost:2222 by default
- Multiple clients can connect simultaneously
- The device state is simulated and not persistent
- Press Ctrl+C to stop the server
