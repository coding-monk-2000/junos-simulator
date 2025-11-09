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
        elif command.startswith("show configuration"):
            parts = command.split()
            if len(parts) == 2:
                return self.show_configuration()
            elif len(parts) > 2:
                section = " ".join(parts[2:])
                return self.show_configuration_section(section)
            return self.show_configuration()
        elif command.startswith("show interface"):
            parts = command.split()
            if len(parts) > 2:
                return self.show_interface_detail(parts[2])
            return "Error: Interface name required\r\n"
        elif command.startswith("show system"):
            parts = command.split()
            if len(parts) == 2:
                return self.show_system_uptime()
            elif len(parts) > 2:
                subcommand = parts[2]
                if subcommand == "uptime":
                    return self.show_system_uptime()
                elif subcommand == "information":
                    return self.show_system_information()
                elif subcommand == "processes":
                    return self.show_system_processes()
                elif subcommand == "storage":
                    return self.show_system_storage()
                else:
                    return f"Unknown system subcommand: {subcommand}\r\nAvailable: uptime, information, processes, storage\r\n"
            return self.show_system_uptime()
        elif command == "exit" or command == "quit":
            self.running = False
            return "Goodbye!\r\n"
        else:
            return f"Unknown command: {command}\r\nType 'help' for available commands.\r\n"
            
    def help_command(self):
        return "\r\nAvailable commands:\r\n" + \
               "  help                     - Show this help message\r\n" + \
               "  show version             - Display device version information\r\n" + \
               "  show interfaces          - Display interface status\r\n" + \
               "  show interface <if>      - Display detailed interface information\r\n" + \
               "  show configuration       - Display complete configuration\r\n" + \
               "  show configuration <sec> - Display configuration section (system, interfaces)\r\n" + \
               "  show system [uptime]     - Display system uptime\r\n" + \
               "  show system information  - Display hardware inventory\r\n" + \
               "  show system processes    - Display system processes\r\n" + \
               "  show system storage      - Display storage information\r\n" + \
               "  exit/quit               - Exit the session\r\n\r\n"

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

    def show_system_uptime(self):
        return "\r\nCurrent time: 2025-11-09 14:30:42 UTC\r\n" + \
               "Time Source:  LOCAL CLOCK \r\n" + \
               "System booted: 2025-10-25 07:18:00 UTC (2w1d 07:12 ago)\r\n" + \
               "Protocols started: 2025-10-25 07:19:32 UTC (2w1d 07:11 ago)\r\n" + \
               "Last configured: 2025-11-08 14:25:33 UTC (1d 00:05 ago) by admin\r\n" + \
               " 2:30PM  up 15 days,  7:12, 1 user, load averages: 0.23, 0.18, 0.15\r\n\r\n"

    def show_system_information(self):
        return "\r\nHardware inventory:\r\n" + \
               "Item             Version  Part number  Serial number     Description\r\n" + \
               "Chassis                                JN139E123456      MX480\r\n" + \
               "Midplane         REV 05   750-031001   ABCD123456        MX480 Backplane\r\n" + \
               "FPM Board        REV 04   750-031002   EFGH789012        Front Panel Display\r\n" + \
               "Routing Engine 0 REV 03   750-031003   MNOP345678        RE-S-1800x4\r\n" + \
               "CB 0             REV 01   750-031004   QRST901234        Enhanced MX SCB\r\n" + \
               "CB 1             REV 01   750-031004   UVWX567890        Enhanced MX SCB\r\n" + \
               "MIC 0/0/0        REV 02   750-031005   ABCD111111        4x 10GE XFP\r\n" + \
               "MIC 0/1/0        REV 01   750-031006   EFGH222222        20x 1GE RJ45\r\n" + \
               "Fan Tray         REV 01   740-021822   MNOP333333        Enhanced Fan Tray\r\n" + \
               "PEM 0            REV 03   740-021823   QRST444444        2500W AC Power Entry Module\r\n" + \
               "PEM 1            REV 03   740-021823   UVWX555555        2500W AC Power Entry Module\r\n\r\n"

    def show_system_processes(self):
        return "\r\nlast pid: 15234;  load averages:  0.23,  0.18,  0.15    up 15+07:12:18  14:30:42\r\n" + \
               "80 processes:  2 running, 75 sleeping, 3 waiting\r\n" + \
               "CPU states: 12.5% user,  0.0% nice,  4.2% system,  2.1% interrupt, 81.2% idle\r\n" + \
               "Mem: 148M Active, 89M Inact, 892M Wired, 52M Cache, 199M Buf, 2820M Free\r\n\r\n" + \
               "  PID USERNAME    THR PRI NICE   SIZE    RES STATE   C   TIME    WCPU COMMAND\r\n" + \
               " 1234 root          1  20    0   148M  28984K select  0  12:45  0.00% chassisd\r\n" + \
               " 1345 root          1  20    0    89M  15672K select  0   8:23  0.00% dcd\r\n" + \
               " 1456 root          1  20    0   234M  45328K select  0  45:12  0.00% rpd\r\n" + \
               " 1567 root          1  20    0    67M  12456K select  0   2:34  0.00% mgd\r\n" + \
               " 1678 root          1  20    0    45M   8923K select  0   1:23  0.00% alarmd\r\n\r\n"

    def show_system_storage(self):
        return "\r\nFilesystem           1K-blocks      Used Available Capacity  Mounted on\r\n" + \
               "/dev/da0s1a             495703    174567    281486    38%    /\r\n" + \
               "devfs                        1         1         0   100%    /dev\r\n" + \
               "/dev/da0s1e             495703    123456    332597    27%    /config\r\n" + \
               "/dev/da0s1f            3952588   1234567   2401765    34%    /var\r\n" + \
               "/dev/da0s1d             495703     89012    367041    20%    /var/tmp\r\n" + \
               "procfs                       8         8         0   100%    /proc\r\n\r\n"

    def show_configuration(self):
        return "\r\n## Last commit: 2025-11-08 14:25:33 UTC by admin\r\n" + \
               "version 22.4R1.10;\r\n" + \
               "system {\r\n" + \
               "    host-name JUNOS-MX;\r\n" + \
               "    domain-name lab.local;\r\n" + \
               "    time-zone UTC;\r\n" + \
               "    authentication-order [ radius password ];\r\n" + \
               "    root-authentication {\r\n" + \
               "        encrypted-password \"$6$ABC123...\";\r\n" + \
               "    }\r\n" + \
               "    name-server {\r\n" + \
               "        8.8.8.8;\r\n" + \
               "        8.8.4.4;\r\n" + \
               "    }\r\n" + \
               "    login {\r\n" + \
               "        user admin {\r\n" + \
               "            uid 2000;\r\n" + \
               "            class super-user;\r\n" + \
               "            authentication {\r\n" + \
               "                encrypted-password \"$6$DEF456...\";\r\n" + \
               "            }\r\n" + \
               "        }\r\n" + \
               "    }\r\n" + \
               "    services {\r\n" + \
               "        ssh {\r\n" + \
               "            root-login allow;\r\n" + \
               "            protocol-version v2;\r\n" + \
               "        }\r\n" + \
               "        netconf {\r\n" + \
               "            ssh;\r\n" + \
               "        }\r\n" + \
               "    }\r\n" + \
               "    syslog {\r\n" + \
               "        user * {\r\n" + \
               "            any emergency;\r\n" + \
               "        }\r\n" + \
               "        file messages {\r\n" + \
               "            any notice;\r\n" + \
               "            authorization info;\r\n" + \
               "        }\r\n" + \
               "    }\r\n" + \
               "    ntp {\r\n" + \
               "        server 0.pool.ntp.org;\r\n" + \
               "        server 1.pool.ntp.org;\r\n" + \
               "    }\r\n" + \
               "}\r\n" + \
               "interfaces {\r\n" + \
               "    ge-0/0/0 {\r\n" + \
               "        description \"WAN Interface\";\r\n" + \
               "        unit 0 {\r\n" + \
               "            family inet {\r\n" + \
               "                address 192.168.1.1/24;\r\n" + \
               "            }\r\n" + \
               "        }\r\n" + \
               "    }\r\n" + \
               "    ge-0/0/1 {\r\n" + \
               "        description \"LAN Interface\";\r\n" + \
               "        disable;\r\n" + \
               "    }\r\n" + \
               "    ge-0/0/2 {\r\n" + \
               "        description \"DMZ Interface\";\r\n" + \
               "        unit 0 {\r\n" + \
               "            family inet {\r\n" + \
               "                address 10.0.1.1/24;\r\n" + \
               "            }\r\n" + \
               "        }\r\n" + \
               "    }\r\n" + \
               "    lo0 {\r\n" + \
               "        unit 0 {\r\n" + \
               "            family inet {\r\n" + \
               "                address 127.0.0.1/32;\r\n" + \
               "            }\r\n" + \
               "        }\r\n" + \
               "    }\r\n" + \
               "}\r\n" + \
               "routing-options {\r\n" + \
               "    static {\r\n" + \
               "        route 0.0.0.0/0 next-hop 192.168.1.254;\r\n" + \
               "    }\r\n" + \
               "}\r\n" + \
               "protocols {\r\n" + \
               "    ospf {\r\n" + \
               "        area 0.0.0.0 {\r\n" + \
               "            interface ge-0/0/2.0;\r\n" + \
               "        }\r\n" + \
               "    }\r\n" + \
               "}\r\n\r\n"

    def show_configuration_section(self, section):
        if section == "system":
            return "\r\n## Last commit: 2025-11-08 14:25:33 UTC by admin\r\n" + \
                   "system {\r\n" + \
                   "    host-name JUNOS-MX;\r\n" + \
                   "    domain-name lab.local;\r\n" + \
                   "    time-zone UTC;\r\n" + \
                   "    authentication-order [ radius password ];\r\n" + \
                   "    root-authentication {\r\n" + \
                   "        encrypted-password \"$6$ABC123...\";\r\n" + \
                   "    }\r\n" + \
                   "    name-server {\r\n" + \
                   "        8.8.8.8;\r\n" + \
                   "        8.8.4.4;\r\n" + \
                   "    }\r\n" + \
                   "    login {\r\n" + \
                   "        user admin {\r\n" + \
                   "            uid 2000;\r\n" + \
                   "            class super-user;\r\n" + \
                   "            authentication {\r\n" + \
                   "                encrypted-password \"$6$DEF456...\";\r\n" + \
                   "            }\r\n" + \
                   "        }\r\n" + \
                   "    }\r\n" + \
                   "    services {\r\n" + \
                   "        ssh {\r\n" + \
                   "            root-login allow;\r\n" + \
                   "            protocol-version v2;\r\n" + \
                   "        }\r\n" + \
                   "        netconf {\r\n" + \
                   "            ssh;\r\n" + \
                   "        }\r\n" + \
                   "    }\r\n" + \
                   "    syslog {\r\n" + \
                   "        user * {\r\n" + \
                   "            any emergency;\r\n" + \
                   "        }\r\n" + \
                   "        file messages {\r\n" + \
                   "            any notice;\r\n" + \
                   "            authorization info;\r\n" + \
                   "        }\r\n" + \
                   "    }\r\n" + \
                   "    ntp {\r\n" + \
                   "        server 0.pool.ntp.org;\r\n" + \
                   "        server 1.pool.ntp.org;\r\n" + \
                   "    }\r\n" + \
                   "}\r\n\r\n"
        elif section == "interfaces":
            return "\r\n## Last commit: 2025-11-08 14:25:33 UTC by admin\r\n" + \
                   "interfaces {\r\n" + \
                   "    ge-0/0/0 {\r\n" + \
                   "        description \"WAN Interface\";\r\n" + \
                   "        unit 0 {\r\n" + \
                   "            family inet {\r\n" + \
                   "                address 192.168.1.1/24;\r\n" + \
                   "            }\r\n" + \
                   "        }\r\n" + \
                   "    }\r\n" + \
                   "    ge-0/0/1 {\r\n" + \
                   "        description \"LAN Interface\";\r\n" + \
                   "        disable;\r\n" + \
                   "    }\r\n" + \
                   "    ge-0/0/2 {\r\n" + \
                   "        description \"DMZ Interface\";\r\n" + \
                   "        unit 0 {\r\n" + \
                   "            family inet {\r\n" + \
                   "                address 10.0.1.1/24;\r\n" + \
                   "            }\r\n" + \
                   "        }\r\n" + \
                   "    }\r\n" + \
                   "    lo0 {\r\n" + \
                   "        unit 0 {\r\n" + \
                   "            family inet {\r\n" + \
                   "                address 127.0.0.1/32;\r\n" + \
                   "            }\r\n" + \
                   "        }\r\n" + \
                   "    }\r\n" + \
                   "}\r\n\r\n"
        else:
            return f"\r\nConfiguration section '{section}' not found or not implemented.\r\n" + \
                   "Available sections: system, interfaces\r\n\r\n"