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
        os.system("nikto -h http://"+ip) 

