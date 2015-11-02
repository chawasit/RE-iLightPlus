#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# RE-iLightPlus - http://github.com/chawasit/RE-iLightPlus
# Copyright 2015 Chawasit Tengtrairatana <chawasit_teng@cmu.ac.th>

import socket
# Wifi Controller IP
UDP_IP = "192.168.2.22"
# Default UDP port
UDP_PORT = 8899

# http://stackoverflow.com/questions/7822956/how-to-convert-negative-integer-value-to-hex-in-python
def tohex(val, nbits=8):
    if val is 0: return "0x00"
    return hex((val + (1 << nbits)) % (1 << nbits))

while True:
    scan = raw_input("Command: ")
    command = scan.split()
    hex_string = "".join([ tohex(int(i)).replace("0x","") for i in command])
    MESSAGE = bytearray.fromhex(hex_string)
    s = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(MESSAGE, (UDP_IP, UDP_PORT))