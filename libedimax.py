#!/usr/bin/python

import sys
import urllib2
import re

import xml.etree.ElementTree as ET

class EdimaxDevice:

     host = ""
     port = 0
     user = ""
     password = ""
     payload = '''<?xml version=\"1.0\" encoding=\"UTF8\"?>
         <SMARTPLUG id=\"edimax\">
               <CMD id=\"get\">
                    <NOW_POWER><Device.System.Power.NowCurrent></Device.System.Power.NowCurrent>
                    <Device.System.Power.NowPower></Device.System.Power.NowPower></NOW_POWER>
               </CMD>
          </SMARTPLUG>'''

     def __init__(self,host,port=10000,user="admin",password="1234"):
          self.host = host
          self.port = port
          self.password = password
          self.user = user

     def getCurrentPowerUsage(self):
         # Create an OpenerDirector with support for Basic HTTP Authentication...
          auth_handler = urllib2.HTTPBasicAuthHandler()
          auth_handler.add_password(realm='SP2101W',
               uri='http://'+self.host+':'+str(self.port),
               user=self.user,
               passwd=self.password)
          opener = urllib2.build_opener(auth_handler)
          # ...and install it globally so it can be used with urlopen.
          urllib2.install_opener(opener)
          req = urllib2.Request('http://'+self.host+':'+str(self.port)+'/smartplug.cgi')
          req.add_header('Accept','*/*')
          req.add_header('Content-Type','application/x-www-form-urlencoded')
          req.add_header('User-Agent','EdiPlug/20150504 CFNetwork/711.3.18 Darwin/14.0.0')
          req.add_header('Accept-encoding','gzip, deflate')
          req.add_header('Connection','keep-alive')
          req.add_header('Accept-Language','de-de')
          req.add_header('Content-Length',str(len(self.payload)))
          req.add_data(self.payload)
          result = urllib2.urlopen(req)
          reply = result.read()

          root = ET.fromstring(reply)
          ampsElement = root.find('.//Device.System.Power.NowCurrent')
          wattsElement = root.find('.//Device.System.Power.NowPower')


          if wattsElement is not None:
               if ampsElement is not None:
                    return {'amps':float(ampsElement.text),'watts':float(wattsElement.text)}

          return {'amps':-1.,'watts':-1.}

def main():
     dev1 = EdimaxDevice('192.168.176.34')
     print dev1.getCurrentPowerUsage()

if __name__ == "__main__":
    main()
