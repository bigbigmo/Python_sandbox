
#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.20',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_S3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.30',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_S4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.40',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_S5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.50',
    'username': 'cisco',
    'password': 'cisco',
}

all_switches = [iosv_l2_S2, iosv_l2_S3, iosv_l2_S4, iosv_l2_S5]

for switch in all_switches:
    net_connect = ConnectHandler(**switch)
    for n in range (2,21):
        print "Creating VLAN " + str(n)
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print output



