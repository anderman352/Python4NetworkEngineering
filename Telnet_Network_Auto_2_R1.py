# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:43:39 2024

@author: david
"""

# telnet into switch, set loopn ip addres and mask

import getpass
import telnetlib

HOST = "192.168.122.71"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")

tn.write(b"conf t\n")

tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")

tn.write(b"int loop 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")

tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")



