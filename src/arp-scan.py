#!/usr/bin/python

import sys
import getopt

from scapy.all import srp,Ether,ARP,conf

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:r:")
    except KeyInterrupt:
        print('arp.py -i <interface> -r <ip-range>')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print('arp.py -i <interface> -r <ip-range>')
        elif opt == '-i':
            interface = arg
        elif opt == '-r':
            ipRange = arg

    conf.verb = 0
    ans, uans = srp(Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(pdst=ipRange), timeout = 10, iface=interface)

    for snd, rcv in ans:
        macAddress = rcv.sprintf(r'%Ether.src%')

if __name__ == "__main__":
    main(sys.argv[1:])
