#!/usr/bin/eny python

import os

class Dnsrecon():
    def dns(self,ip):
        self.ip_add=ip
        print("\033[1;30m")
        os.system("dnsrecon -d "+ip)