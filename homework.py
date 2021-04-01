import requests
from bs4 import beautifulsoup
req=requests.get("https://csie.asia.edu.tw/project/semester-103",verify=false)
req=encoding="utf8"
if(req.status_code==200):
  #print(req.text)
  soup = Beautifulsoup(req.text,'html.parser')
  result = soup.find_all("p")
  fp=open("out1.txt","w",encoding="utf8")
  for va1 in resilt:
    text1=val.text.replace("\n","")
    text2=text1.replace("  ","")
    print(text2)
    fp.write(text1+"\n")
  fp.close()
else:
  print("no page")
