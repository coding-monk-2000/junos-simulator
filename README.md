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
- `show system` - Display system information
- `exit` or `quit` - Exit the session

## Example Session

```
$ ssh admin@localhost -p 2222
admin@localhost's password: admin

Welcome to Simulated Network Device
Please login to continue.

simulated-device> show version

Device Information:
  Model: Simulated Network Device v1.0
  Software Version: SimOS 1.0.0
  Build Date: November 9, 2025
  Serial Number: SIM123456789
  Uptime: 1 day, 2 hours, 30 minutes

simulated-device> show interfaces

Interface Status:
----------------------------------------
Interface    Status   Description         
----------------------------------------
ge-0/0/0     up       Data Interface      
ge-0/0/1     down     Data Interface      
ge-0/0/2     up       Data Interface      
lo0          up       Management          

simulated-device> exit
Goodbye!
```

## Notes

- The server runs on localhost:2222 by default
- Multiple clients can connect simultaneously
- The device state is simulated and not persistent
- Press Ctrl+C to stop the server
