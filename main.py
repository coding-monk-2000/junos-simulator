#!/usr/bin/env python3
"""
Simple SSH Device Simulator
A basic SSH server that simulates a network device with CLI interface.
"""

import sys
from ssh_server import start_ssh_server


if __name__ == "__main__":
    # You can change the host and port here
    HOST = 'localhost'
    PORT = 2222
    
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    
    start_ssh_server(HOST, PORT)