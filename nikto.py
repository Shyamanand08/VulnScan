
#!/usr/bin/eny python

import os

class Nikto():
    def nik(self,ip):
        print("\033[1;35m")
        n="""
        
          _  __       _           
         (_)[  |  _  / |_         
 _ .--.  __  | | / ]`| |-' .--.   
[ `.-. |[  | | '' <  | | / .'`\ \ 
 | | | | | | | |`\ \ | |,| \__. | 
[___||__|___|__|  \_]\__/ '.__.'  
                                  

        """
        var=1
        perm=input("[+] Do you want to continue (y/n)? ")
        self.ip_add=ip
        while var==1:
            print(n)
            
            
            if perm=="y" or "Y":
                os.system("nikto -h http://"+ip)
            else:
                var=2

            

        