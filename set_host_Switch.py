# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:44:51 2024

@author: david
"""
# configure username and password
#configue IP address on switch
# configure VTY virtual teletype
# line vty 0 4 opens five virt interfaces 0-4

host S6

enable password cisco
!
username david privilege 15 password 0 cisco


interface VLAN1
ip address 192.168.122.86 255.255.255.0
no shut
!

line vty 0 4
login local
transport input all
!
end
wr
