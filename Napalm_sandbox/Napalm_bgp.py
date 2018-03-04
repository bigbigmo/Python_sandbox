import json
from napalm import get_network_driver

bgp_routers_list = ['192.168.122.16', '192.168.122.10']

for ip_addr in bgp_routers_list:
        print("Connecting to " + str(ip_addr))
        driver = get_network_driver('ios')
        iosl2 = driver(ip_addr,'kkk','cisco')
        iosl2.open()
        ios_output = iosl2.get_bgp_neighbors()
        print (json.dumps(ios_output, indent=4))
        iosl2.close()
