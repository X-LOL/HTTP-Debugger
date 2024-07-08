try:
    import mitmproxy
except ImportError:
    import subprocess
    subprocess.run(['pip', 'install', 'mitmproxy'])
    import mitmproxy


import os
import time

os.system('cls')

Port = input('What is the Port you want to start the Proxy ON? \n =>')

import winreg

def set_proxy(proxy_url):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy_url)
    winreg.CloseKey(key)

proxy_url = "localhost:"+Port
set_proxy(proxy_url)


print("\n => Service started successfuly .... Please Wait")

time.sleep(2)

os.system("mitmproxy -p "+Port)