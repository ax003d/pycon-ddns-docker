import os
import json

from docker import Client
from settings import *


def update(domain, ip):
    print "update %s -> %s" % (domain, ip)
    p = os.popen('nsupdate -k %s' % KEY, 'w')
    p.write('server %s\n' % NAME_SERVER)
    p.write('zone %s\n' % ZONE)
    p.write('update del %s A \n' % domain)
    p.write('update add %s 600 A %s\n' % (domain, ip))
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
            if name in DOMAINS:
                update(DOMAINS[name], ip)


if __name__ == '__main__':
    ddns()
