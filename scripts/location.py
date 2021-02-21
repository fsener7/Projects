import requests
ip=input("IP giriniz:")
url="http://ipinfo.io/"+str(ip)
sonuc=requests.get("http://ipinfo.io/"+str(ip)+"/json",verify=False)
SonucJson=sonuc.json()
for key in SonucJson:
    print(key + " : " + SonucJson[key])