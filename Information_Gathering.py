#!/usr/bin/env python2.7
import os
while True:
    print '''
                                                                               
          ###           #####        #   #                          #####  @
           #   #        |            # #                              #    #          #
           #   # # #    ####   ###   #        # #    # #     # #      #    #    ###   # # #
           #   #    #   #     #   #  #      #    #  #   #   #   #     #    #   #   #  #    #
          ###  #    #   #      ###   #     #     #      #    # #  #   #   ###   ###   #    # 
          
          '''
    print '''
        1- ping
        2- whois
        3- domain map 
        4- webspider
        5- adminfinder
        6- reverse ip
        7- ip locatoion
        8- clear page

        '''
    choose = raw_input("Enter The choose = ")
    print "\n\n"
    print "********"
    if choose == "1":
      import requests
      print "\n"
      print "Usage ==> site.com"
      u = raw_input("Enter The Domain = ")

      r = requests.get("http://api.hackertarget.com/nping/?q="+u)

      print "\n"

      print r.content

      f = open("ping.txt" , "w")
      f.write(r.text)
      f.close()

    elif choose == "2":
       import urllib 
       import bs4
       while True:
            print "\n"
            print "Usage ==> site.com"
            u = raw_input("Enter The Domain = ")

            url = "https://www.whois.com/whois/"

            link = urllib.urlopen(url+u)

            source = link.read()

            f = bs4.BeautifulSoup(source, "html.parser")

            filter = f.find("pre", id="registrarData")

            print filter.text

    elif choose == "3":
       import urllib
       while True:
            print "Usage ==> site.com"
            u = raw_input("Enter The Domain = ")

            link = urllib.urlopen("https://dnsdumpster.com/static/map/"+u+".png")

            if link.code == 200:
                print "Site Found !"

            else:
                print "site note found :("
                exit()	

            urllib.urlretrieve("https://dnsdumpster.com/static/map/"+u+".png",u+".png")

            print "Successfully !!"     
    elif choose == "4":
       import urllib
       from bs4 import BeautifulSoup
       while True:

            print "\n\n"

            print "Usage ==> http://site.com"
                    
            u  = raw_input("Enter The Domain = ")
                    
            print '''
                        1- a link
                        2- image link
                        3- script link
                '''
            ch = raw_input("Enter The choose = ")
            if ch == "1":
                tag = 'a'
            elif ch == "2":
                tag = 'img'
            elif ch == "3":
                tag = "script"     
                    
            link = urllib.urlopen(u)

            source = link.read()

            spider = BeautifulSoup(source , 'html.parser')

            file = open("web_sipder.txt","w")
                    

            for p in spider.find_all(tag):
                        
                if tag == "a":
                    spi = p.get('href')
                    file.writelines(str(spi)+"\n")
                else:
                    spi = p.get('scr')
                    file.writelines(str(spi)+"\n")


    elif choose == "5":
       import urllib
       while True:

            print "\n"
            print "Usage ==> http://site.com"
            u = raw_input("Enter The Domain = ")

            list = ["admin","login","wp-admin","administrator","wp-login.php"]

            for page in list:

                link = urllib.urlopen(u+"/"+page)

                if link.code == 200:
                    print "page Found ! => ",page

                elif link.code == 404:
                    print "page Not Found :(",page

                else:
                    print "Domain Not Found"
                    exit()    	                
    elif choose == "6":
       import requests 
       import json
       while True:
            print "Needs Filter Breaker!!!"
            print "\n"
            print "Usage ==> google.com/IP"
            u = raw_input("Enter The Domain/ip = ")

            data = {"remoteAddress":u}

            link = requests.post("https://domains.yougetsignal.com/domains.php", data)

            source = json.loads(link.content)

            file = open("Site.txt","w")
            for data in source["domainArray"]:
                file.writelines(data[0]+'\n')
            print "\n"
            print "Successfully Saved !! :)"
            file.close()
    elif choose == "7":
       import urllib
       import json 

       while True:


            u = raw_input("Enter The IP = ")

            link = urllib.urlopen("https://ipapi.co/"+u+"/json/")

            source = link.read()

            text = json.loads(source)

            print "*********"
            print "\n"
            print "IP = "+ text["ip"]
            print "City = "+ text["city"]
            print "Region = "+ text["region"]
            print "Country = "+ text["country_name"]
            print "Organization = "+text["org"]
            print "Latitude  = "+str(text['latitude'])
            print "Longitude = "+str(text['longitude'])
            print "\n"
            print "*********"
    elif choose == "8":
        os.system("cls")        
    print "\n"
    print "*******"
