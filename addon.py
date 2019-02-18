import xbmcaddon
import xbmcgui
import urllib
import uuid
import socket
import json

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
mac = ':'.join('%02X' % ((uuid.getnode() >> 8*i) & 0xff) for i in reversed(xrange(6)))
response = urllib.urlopen('http://deprime.tv:3000/get.php?mac='+mac)
hostname = socket.gethostname()

data = json.load(response)

title = data['title']
line1 = data['line1']
line2 = data['line2']
line3 = data['line3']



xbmcgui.Dialog().ok(title, line1, line2,line3)
