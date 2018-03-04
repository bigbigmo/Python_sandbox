
#!/usr/bin/env python

from netmiko import ConnectHandler

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

iosv_l2_S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.20',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_S1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.10',
    'username': 'cisco',
    'password': 'cisco',
}

#open file 'iosv_l2_config' with cisco config commands
with open('iosv_l2_config') as f:
    lines = f.read().splitlines()
    print(lines)

#array with all devices for configuration
all_switches = [iosv_l2_S5, iosv_l2_S4, iosv_l2_S4, iosv_l2_S3, iosv_l2_S2, iosv_l2_S1]

#create loop for configuration every switch in array
#and
#send all lines from file named "iosv_l2_config" for execution on switch
for switch in all_switches:
    net_connect = ConnectHandler(**switch)
    output = net_connect.send_config_set(lines)
    print(output)

