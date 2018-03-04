#Exercise 2
from __future__ import print_function

ip_addr = input('Please enter your ip address: ')

octets = ip_addr.split('.')

print('\n')
print('-' * 60)
print('{:^15}{:^15}{:^15}{:^15}'.format('Octet 1', 'Octet 2', 'Octet 3', 'Octet 4'))
print('-' * 60)
print('{:^15}{:^15}{:^15}{:^15}'.format(*octets))
print('{:^15}{:^15}{:^15}{:^15}'.format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
print('{:^15}{:^15}{:^15}{:^15}'.format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
print('-' * 60)


#Exercise 4
show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.upper().strip().split()


#Exercise 5

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1 = mac1.strip().split()
mac2 = mac2.strip().split()
mac3 = mac3.strip().split()

print('\n')
print('-' * 40)
print('{:>20}{:>20}'.format('IP ADDR', 'MAC ADDRESS'))
print('-' * 40)
print('{1:>20}{3:>20}'.format(*mac1))
print('{1:>20}{3:^20}'.format(*mac2))
print('{1:>20}{3:>20}'.format(*mac3))
