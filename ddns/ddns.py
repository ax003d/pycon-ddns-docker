import os
import json

from docker import Client
from settings import *


def update(domain, ip):
    print "update %s -> %s" % (domain, ip)
    p = os.popen('nsupdate -k {key}'.format(key=KEY), 'w')
    p.write('server {ip}\n'.format(ip=NAME_SERVER))
    p.write('zone {zone}\n'.format(zone=ZONE))
    p.write('update del {domain}.{zone} A \n'.format(
        domain=domain, zone=ZONE))
    p.write('update add {domain}.{zone} 600 A {ip}\n'.format(
        domain=domain, zone=ZONE, ip=ip))
    p.write('send\n')
    p.close()


def ddns():
    client = Client(base_url='unix://var/run/docker.sock')
    for event in client.events():
        event = json.loads(event)
        if event['status'] == 'start':
            container = client.inspect_container(event['id'])
            name = container['Name']
            ip = container['NetworkSettings']['IPAddress']
            update(name[1:], ip)


if __name__ == '__main__':
    ddns()
