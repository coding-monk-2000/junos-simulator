import paramiko
import threading

class DeviceSSHServer(paramiko.ServerInterface):
    """SSH Server Interface for the simulated device"""
    
    def __init__(self):
        self.event = threading.Event()
        
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
        
    def check_auth_password(self, username, password):
        if username == 'admin' and password == 'admin':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
        
    def get_allowed_auths(self, username):
        return 'password'
        
    def check_channel_shell_request(self, channel):
        self.event.set()
        return True
        
    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True