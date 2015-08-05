#!/usr/bin/python

import sys

class EdimaxDevice:

     host = ""
     port = 0
     user = ""
     password = ""
     payload = '''<?xml-version=\"1.0\" encoding=\"UTF8\"?>
         <SMARTPLUG id=\"edimax\">
               <CMD id=\"get\">
                    <NOW_POWER><Device.System.Power.NowCurrent></Device.System.Power.NowCurrent>
                    <Device.System.Power.+NowPower></Device.System.Power.NowPower></NOW_POWER>
               </CMD>
          </SMARTPLUG>'''

     def __init__(self,host,port=10000,user="admin",password="1234"):
          self.host = host
          self.port = port
          self.password = password
          self.user = user

     def getCurrentPowerUsage

if __name__ == "__main__":
    main()
