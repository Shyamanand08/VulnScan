#!/usr/bin/eny python

# import os

# class Cewl():
#     def cew(self,ip):
#         print("\033[1;90m")
#         self.ip_add=ip
#         os.system("cewl http://"+ip)

# import os


import os


class Cewl():
    def cew(self, ip):
        print("\033[1;90m")
        
        self.ip_add = ip
        var =1
        while var==1:
            print("[+] 1 Enter your IP address/URL ")
            print("[+] 2 Exit")
            input_for_cewl=int(input("[+] Please enter a number 1 or 2 > "))
            if(input_for_cewl==1):
                var1=1
                while var1==1:

                    print("[+]Please select from the below options > ")
                    print("[+] 1 Normal scan ")
                    print("[+] 2 show the count of each word found (use --count or -c) ")
                    print("[+] 3 depth search --depth")
                    print("[+] 4 Include email addresses in search(use --email) ")
                    print("[+] 5 To keep the downloaded files (use --keep) ")
                    print("[+] 6 To get the User agent (--ua) ")
                    print("[+] 7 Exit")
                    input_scan_type=int(input(f"[+] Enter your number for IP :{ip} "))
                    if(input_scan_type==1):
                        os.system("sudo cewl "+ip)
                    elif(input_scan_type==2):
                        os.system("sudo cewl "+ip+" --count")
                    elif(input_scan_type==3):
                        os.system("sudo cewl "+ip+" --depth")
                    elif(input_scan_type==4):
                        os.system("sudo cewl "+ip+" --email")
                    elif(input_scan_type==5):
                        os.system("sudo cewl "+ip+" --keep")
                    elif(input_scan_type==6):
                        os.system("sudo cewl "+ip+" --ua")
                    elif input_scan_type==7:
                        var1=2
                        print("")
                    else:
                        print("") 
                        print("\033[1;41m[*] Please Enter valid number \033[1;40m")
                        print("")             
            elif input_for_cewl==2:

                var=2
                print("-------------------! CEwL Scan Completed Successfully--------------------")

            else:
                print("") 
                print("\033[1;41m[*] Please Enter valid number \033[1;40m")
                print("") 

