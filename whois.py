#!usr/bin/env python
import os 

class Whois():
    def wh(self, ip):
        l="""

██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
██║    ██║██║  ██║██╔═══██╗██║██╔════╝
██║ █╗ ██║███████║██║   ██║██║███████╗
██║███╗██║██╔══██║██║   ██║██║╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝
                                      
"""
        print("")
        print("\033[1;35m",l)
        self.ip_add=ip
        os.system("whois "+ip)