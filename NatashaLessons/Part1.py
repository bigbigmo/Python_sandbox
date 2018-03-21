#4-1
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace('Fast', 'Gigabit')
print (NAT)

#4-2
MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':','.')
print(MAC)

#4-3
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
CONFIG = CONFIG.split()
VLANS_ = CONFIG[4].split(',')
print(VLANS_)

#4-4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

command1 = command1.split()
command2 = command2.split()

command1 = set(command1[4].split(','))
command2 = set(command2[4].split(','))

result = list(map(int, command1&command2))

print (result)

#4-5
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
VLANS = list(set(VLANS))
VLANS.sort()
print(VLANS)

#4-6
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()
ospf_data = {}
if ospf_route[0] == 'O':
    ospf_data.setdefault('Protocol', 'OSPF')
else:
    print('This is not OSPF')
ospf_data.setdefault('Prefix', ospf_route[1])
ospf_data.setdefault('AD/Metric', ospf_route[2].strip('[]'))
ospf_data.setdefault('Next-Hop', ospf_route[4].strip(','))
ospf_data.setdefault('Last update', ospf_route[5].strip(','))
ospf_data.setdefault('Outbound Interface', ospf_route[6])
print(ospf_data)

#4-7
MAC2 = 'AAAA:BBBB:CCCC'
MAC2 = bin(int(MAC2.replace(':',''),16))
print(MAC2)

#4-8
IP = '192.168.3.1'
IP = list(map(int, IP.split('.')))

for ip in IP:
    print('{:<10}'. format(ip), end='')
print()
for ip in IP:
    print('{:<10}'.format(bin(ip)[2:].zfill(8)), end='')

