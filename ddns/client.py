"""
Usage: python client.py webapp.devops.it
"""

import sys
import socket
import requests

from ddns import update


def public_ip():
    try:
        resp = requests.get('http://httpbin.org/ip')
        return resp.json()['origin']
    except Exception, e:
        pass


if __name__ == '__main__':
    domain = sys.argv[1]
    cur_ip = socket.gethostbyname(domain)
    pub_ip = public_ip()
    if cur_ip != pub_ip:
        update(domain, pub_ip)
