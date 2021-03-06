from __future__ import print_function, unicode_literals
from pprint import pprint
import re

#1
"""Create a dictionary representing a network device.
The dictionary should have key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'.
If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named 'bgp_fields'.
The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.
Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.
Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values."""


dict = {
    'ip_addr': '10.10.10.10',
    'vendor': 'cisco',
    'username': 'ivan',
    'password': '123123'}
print(dict['ip_addr'])

if dict['vendor'].lower() == 'cisco':
    dict.update({'platform': 'ios'})
elif dict['vendor'].lower() == 'juniper':
    dict.update({'platform': 'junos'})

bgp_fields = {
    'bgp_as': '100',
    'peer_as': '200',
    'peer_ip': '9.9.9.9'}
dict.update(bgp_fields)

for key in bgp_fields.keys():
    print (key)
for key, value in bgp_fields.items():
    print("{key:>15} ---> {value:>15}".format(key=key, value=value))

#2
"""Create three separate lists of IP addresses.
The first list should be the IP addresses of the Houston data center routers, and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).
The second list should be the IP addresses of the Atlanta data center routers, and it should have at least eight RFC1918 IP addresses (including some addresses that overlap with the Houston data center).
The third list should be the IP addresses of the Chicago data center routers, and it should have at least eight RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.
Convert each of these three lists to a set.
Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.
Using set operations, find the IP addresses that are duplicated in all three sites.
Using set operations, find the IP addresses that are entirely unique in Chicago."""

houston_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.40.1',
    '10.10.50.1',
    '10.10.60.1',
    '10.10.70.1',
    '10.10.80.1',
    '10.10.10.1',
    '10.10.20.1',
    '10.10.70.1',
]

atlanta_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.160.1',
    '10.10.170.1',
    '10.10.180.1',
]

chicago_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.210.1',
    '10.10.220.1',
    '10.10.230.1',
    '10.10.240.1',
]

houston_ips = set(houston_ips)
atlanta_ips = set (atlanta_ips)
chicago_ips = set (chicago_ips)

print( houston_ips & atlanta_ips)
print( houston_ips & atlanta_ips & chicago_ips)
print( chicago_ips - (houston_ips.union(atlanta_ips)))


#3
"""Read in the 'show_version.txt' file.
From this file, use regular expressions to extract the OS version, serial number, and configuration register values.
Your output should look as follows:
OS Version: 15.4(2)T1
Serial Number: FTX0000038X
Config Register: 0x2102"""

with open ("show_version.txt") as f:
    show_ver = f.read()
    os_version = re.search(r"^Cisco IOS .* Version (\d+.\d+.\d+.\w+\d+).*$", show_ver, flags=re.M).group(1)
    print("os_version ---> {}". format(os_version))
    ser_num = re.search(r"^\*0.*\s+(\w+)$", show_ver, flags=re.M).group(1)
    print("serial number ---> {}". format(ser_num))
    con_reg = re.search(r"^Configuration register is (0x\d\d\d\d)$", show_ver, flags=re.M).group(1)
    print("config register ---> {}". format(con_reg))


#4
"""sing a named regular expression (?P<name>), extract the model from the below string:
show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''
Note that, in this example, '881' is the relevant model.
our regular expression should not, however, include '881' in its search pattern since this number changes across devices.
Using a named regular expression, also extract the '236544K/25600K' memory string.
Once again, none of the actual digits of the memory on this device should be used in the regular expression search pattern.
Print both the model number and the memory string to the screen."""

show_version = '''Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory
Processor board ID FTX0000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)'''

router_model = re.search(r"^Cisco (.*) processor ", show_version, flags=re.M).group(1)
memory = re.search(r"^Cisco .* with (.*) bytes", show_version, flags=re.M).group(1)
print('Model of router is {} with {} memory'.format(router_model, memory))


#5
"""Read the 'show_ipv6_intf.txt' file.
From this file, use Python regular expressions to extract the two IPv6 addresses.
The two relevant IPv6 addresses you need to extract are:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
Try to use re.DOTALL flag as part of your search.
Your search pattern should not include any of the literal characters in the IPv6 address.
From this, create a list of IPv6 addresses that includes only the above two addresses.
Print this list to the screen."""
