#!/usr/bin/env python

# python 3 
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as etree

url     = 'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=B&dateinterval=7000&rlevel=nat&fields=all'
page    = urllib.request.urlopen( url )
#print( page.getheaders() )
content = page.read( ).decode( 'WINDOWS-1252' ).replace( '\r\n' , '' ).replace( '\n' , '' ).replace( '\t' , '' )
#print( content )
tree = etree.fromstring( content )
for child in tree:
    print( child )
