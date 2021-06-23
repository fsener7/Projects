import socket
import sys
from ipaddress import IPv4Network
try:
  net = IPv4Network(sys.argv[1])
  print("IP - DOMAIN"+"\n----------------------")
  for IP in net: 
    try:
      host = socket.gethostbyaddr(str(IP))[0]
      print(IP,host)
    except Exception as e:
      print(IP,"NULL")
except Exception as e:
  print("usage: python3 iptodomainbyblock.py IP_BLOCK")
