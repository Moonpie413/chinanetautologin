# -*- coding:utf8 -*-
# userip=119.97.98.54&basip=&acname=&oraurl=

import socket
import os

if os.name != "nt":
    import fcntl
    import struct

class login(object):

    def get_lan_ip(self):
        ip = socket.gethostbyname(socket.gethostname())
        if ip.startswith("127.") and os.name != "nt":
            interfaces = [
                "eth0",
                "eth1",
                "eth2",
                "wlan0",
                "wlan1",
                "wifi0",
                "ath0",
                "ath1",
                "ppp0",
                ]
            for ifname in interfaces:
                try:
                    ip = self.get_interface_ip(ifname)
                    break
                except IOError:
                    pass
        return ip

    def get_interface_ip(self,ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(),
            0x8915,struct.pack('256s',ifname[:15]))[20:24])
        return ip


login = login()
i = login.get_lan_ip()
print i
