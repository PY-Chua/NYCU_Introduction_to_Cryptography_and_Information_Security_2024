#!/usr/bin/python3
from scapy.all import *

ip  = IP(src='1.2.3.4',dst='10.9.0.53')

udp = UDP(sport=12345, dport=53,chksum=0)

Qdsec    = DNSQR(qname='twysw.example.com') 
dns   = DNS(id=0xAAAA, qr=0, qdcount=1, qd=Qdsec)
Querypkt = ip/udp/dns

with open('ip_req.bin', 'wb') as f:
  f.write(bytes(Querypkt))
  Querypkt.show()

# reply = sr1(Querypkt)
