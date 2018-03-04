#!/usr/local/bin/python3.6
#exercise 1-3

from __future__ import print_function, unicode_literals
from pprint import pprint

f = open("show_arp.txt")
output = f.readlines()
output.pop(0)
output.sort()

three_lines = list(output[:3])
three_lines = "\n".join(three_lines)

pprint("ORGINAL CONTENT")
pprint(output)

print("FIRST 3 LINES")
print(three_lines)

#f.close()

f = open("arp_entries.txt", "w")
f.write(three_lines)
f.close()

#exercise 4
"""4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.
Obtain the list entry associated with the FastEthernet4 interface.
You can just hard-code the index at this point since we haven't covered for-loops or regular expressions.
Use the string .split() method to obtain both the IP address and the corresponding MAC address associated with the IP.
Create a two element tuple from the result (intf_name, ip_address).
Print that tuple to the screen.
Use pycodestyle on this script. Get the warnings/errors to zero.
You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt).
Alternatively, you can type 'python -m pip install pycodestyle'. """

with open("show_ip_int_brief.txt") as f:
    show_ip_int_brief = f.readlines()

fa4_ip = show_ip_int_brief[5].strip()
fields = fa4_ip.split()
intf = fields[0]
ip_address = fields[1]

my_results = (intf, ip_address)
print(my_results)

#exercise 5
"""Read the 'show_ip_bgp_summ.txt' file into your program.
From this BGP output obtain the first and last lines of the output.
From the first line use the string .split() method to obtain the local AS number.
From the last line use the string .split() method to obtain the BGP peer IP address.
Print both local AS number and the BGP peer IP address to the screen."""

with open("show_ip_bgp_summ.txt") as f:
    show_ip_bgp_summ = f.readlines()

#line_1 = show_ip_bgp_summ[0].strip().split()
#line_last = show_ip_bgp_summ[-1].strip().split()

line_1_ = show_ip_bgp_summ[0].strip()
line_last_ = show_ip_bgp_summ[-1].strip()

line_1 = line_1_.split()
line_last = line_last_.split()

local_as = str(line_1[7])
ip_peer = str(line_last[0])


pprint("Local AS number is " + local_as)
pprint("IP peer is " + ip_peer)
