#!/usr/bin/env python3
"""
SSH Server implementation for the simulated device
"""

import paramiko
import socket
import threading
import os
from ssh_interface import DeviceSSHServer
from cli import DeviceCLI


def handle_ssh_session(channel, cli):
    """Handle an SSH session with CLI interaction"""
    channel.send(b"\r\nWelcome to Simulated JUNOS Device\r\n")
    
    # Send initial prompt
    channel.send(cli.get_prompt().encode())
    
    buffer = ""
    
    while cli.running:
        try:
            # Read data from the channel
            data = channel.recv(1024)
            if not data:
                break
                
            # Handle incoming data
            for byte in data:
                char = chr(byte)
                
                if char == '\r' or char == '\n':
                    if buffer.strip():
                        # Process the command
                        output = cli.process_command(buffer)
                        if output:
                            channel.send(output.encode())
                        
                        if not cli.running:
                            break
                            
                        # Send new prompt
                        channel.send(cli.get_prompt().encode())
                    else:
                        # Empty line, just send prompt
                        channel.send(cli.get_prompt().encode())
                    buffer = ""
                elif char == '\x7f':  # Backspace
                    if buffer:
                        buffer = buffer[:-1]
                        channel.send(b'\b \b')
                elif char.isprintable():
                    buffer += char
                    channel.send(char.encode())
                    
        except Exception as e:
            print(f"Session error: {e}")
            break
    
    channel.close()


def create_host_key():
    """Create or load a persistent RSA host key"""
    key_file = "host_key.rsa"
    
    if os.path.exists(key_file):
        # Load existing key
        try:
            key = paramiko.RSAKey.from_private_key_file(key_file)
            print(f"Loaded existing host key from {key_file}")
            return key
        except Exception as e:
            print(f"Error loading host key: {e}")
            print("Generating new host key...")
    
    # Generate new key and save it
    key = paramiko.RSAKey.generate(2048)
    try:
        key.write_private_key_file(key_file)
        print(f"Generated and saved new host key to {key_file}")
    except Exception as e:
        print(f"Warning: Could not save host key: {e}")
    
    return key


def handle_client_connection(client_socket, host_key):
    """Handle individual client connections"""
    try:
        transport = paramiko.Transport(client_socket)
        transport.add_server_key(host_key)
        
        server = DeviceSSHServer()
        transport.start_server(server=server)
        
        # Wait for authentication
        channel = transport.accept(30)
        if channel is None:
            print("No channel opened")
            return
            
        # Create CLI instance and handle session
        cli = DeviceCLI()
        handle_ssh_session(channel, cli)
        
    except Exception as e:
        print(f"Client connection error: {e}")
    finally:
        try:
            transport.close()
        except:
            pass


def start_ssh_server(host='localhost', port=2222):
    """Start the SSH server"""
    print(f"Starting SSH server on {host}:{port}")
    print("Login credentials: username='admin', password='admin'")
    
    # Create host key
    host_key = create_host_key()
    
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"SSH server listening on {host}:{port}")
        print(f"To connect: ssh admin@{host} -p {port}")
        print("Press Ctrl+C to stop the server")
        
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            
            # Handle connection in a separate thread
            thread = threading.Thread(
                target=handle_client_connection,
                args=(client_socket, host_key)
            )
            thread.daemon = True
            thread.start()
            
    except KeyboardInterrupt:
        print("\nShutting down SSH server...")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
