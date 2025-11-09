class DeviceCLI:
    """Simple CLI interface for the simulated device"""
    
    def __init__(self):
        self.hostname = "JUNOS-MX"
        self.running = True
        self.interface_status = {
            "ge-0/0/0": "up",
            "ge-0/0/1": "down", 
            "ge-0/0/2": "up",
            "lo0": "up"
        }
        
    def get_prompt(self):
        return f"{self.hostname}> "
        
    def process_command(self, command):
        """Process CLI commands and return output"""
        command = command.strip()
        
        if not command:
            return ""
            
        if command == "help" or command == "?":
            return self.help_command()
        elif command == "show version":
            return self.show_version()
        elif command == "show interfaces":
            return self.show_interfaces()
        elif command.startswith("show interface"):
            parts = command.split()
            if len(parts) > 2:
                return self.show_interface_detail(parts[2])
            return "Error: Interface name required\r\n"
        elif command == "show system":
            return self.show_system()
        elif command == "exit" or command == "quit":
            self.running = False
            return "Goodbye!\r\n"
        else:
            return f"Unknown command: {command}\r\nType 'help' for available commands.\r\n"
            
    def help_command(self):
        return "\r\nAvailable commands:\r\n" + \
               "  help                - Show this help message\r\n" + \
               "  show version        - Display device version information\r\n" + \
               "  show interfaces     - Display interface status\r\n" + \
               "  show interface <if> - Display detailed interface information\r\n" + \
               "  show system         - Display system information\r\n" + \
               "  exit/quit          - Exit the session\r\n\r\n"

    def show_version(self):
        return "\r\nDevice Information:\r\n" + \
               "  Model: MX480 Juniper Networks Router\r\n" + \
               "  JUNOS Software Release: 22.4R1.10\r\n" + \
               "  Build Date: November 9, 2025\r\n" + \
               "  Serial Number: JN139E123456\r\n" + \
               "  Uptime: 15 days, 3 hours, 42 minutes, 18 seconds\r\n" + \
               "  Boot time: 2025-10-25 07:18:00 UTC\r\n\r\n"

    def show_interfaces(self):
        output = "\r\nInterface Status:\r\n"
        output += "-" * 50 + "\r\n"
        output += f"{'Interface':<15} {'Status':<8} {'Description':<25}\r\n"
        output += "-" * 50 + "\r\n"
        
        for interface, status in self.interface_status.items():
            desc = "Loopback Interface" if "lo" in interface else "Gigabit Ethernet"
            output += f"{interface:<15} {status:<8} {desc:<25}\r\n"
        
        output += "\r\n"
        return output
        
    def show_interface_detail(self, interface):
        if interface not in self.interface_status:
            return f"Error: Interface {interface} not found\r\n"
            
        status = self.interface_status[interface]
        return f"\r\nPhysical interface: {interface}\r\n" + \
               f"  Interface type: Gigabit Ethernet\r\n" + \
               f"  Administrative status: Enabled\r\n" + \
               f"  Operational status: {status.capitalize()}\r\n" + \
               f"  Link-level type: Ethernet\r\n" + \
               f"  MTU: 1514, MRU: 1522\r\n" + \
               f"  Speed: 1000Mbps\r\n" + \
               f"  Duplex: Full-duplex\r\n" + \
               f"  Hardware address: 00:1f:12:34:56:78\r\n" + \
               f"  Last flapped: Never\r\n" + \
               f"  Statistics last cleared: Never\r\n\r\n"

    def show_system(self):
        return "\r\nSystem Information:\r\n" + \
               "  Hostname: JUNOS-MX\r\n" + \
               "  Model: mx480\r\n" + \
               "  Serial number: JN139E123456\r\n" + \
               "  JUNOS version: 22.4R1.10\r\n" + \
               "  Current time: 2025-11-09 10:30:42 UTC\r\n" + \
               "  System booted: 2025-10-25 07:18:00 UTC (2w1d 03:12 ago)\r\n" + \
               "  Protocols: inet\r\n" + \
               "  Last configured: 2025-11-08 14:25:33 UTC (20:05:09 ago) by admin\r\n" + \
               "  JUNOS Base OS boot: Complete\r\n" + \
               "  JUNOS Base OS software: Complete\r\n" + \
               "  JUNOS Kernel software: Complete\r\n" + \
               "  JUNOS Crypto software: Complete\r\n" + \
               "  JUNOS Packet Forwarding Engine: Complete\r\n" + \
               "  JUNOS Routing software: Complete\r\n" + \
               "  JUNOS Web Management: Complete\r\n\r\n"