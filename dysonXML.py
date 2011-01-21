#!/usr/bin/env python

# python 3 
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as etree

url     = 'http://vk.stnet.ch/XmlEventList.jsp?lang=de&maxrows=50000&cat=B&dateinterval=7000&rlevel=nat&fields=all'
page    = urllib.request.urlopen( url )
#print( page.getheaders() )
content = page.read( ).decode( 'WINDOWS-1252' ).replace( '\r\n' , '' ).replace( '\n' , '' ).replace( '\t' , '' )
#print( content )
tree = etree.fromstring( content )
for child in tree:
    print( str( child.tag  ) + ' = ' +  str ( child.attrib ) )
    if child.tag == "EVENT_LIST" : 
        for ch in child:
            print( " -> " + str( ch.tag ) + ' = ' +  str ( ch.attrib ) )
            if ch.tag == "EVENT" :
                for c in ch :
                    #print( "  --> " + str( c.tag ) + ' = ' + str( c.attrib ) )
                    if 'ID' in c.attrib and c.attrib[ 'ID' ] == 'TITLE_DE' :
                        for title in c:
                            print( "   ---> " + title.tag  + ' = ' + str( title.text ) )
                    if 'ID' in c.attrib and c.attrib[ 'ID' ] == 'TITLE_FR' :
                        for title in c:
                            print( "   ---> " + title.tag  + ' = ' + str( title.text ) )
                    if 'ID' in c.attrib and c.attrib[ 'ID' ] == 'TITLE_IT' :
                        for title in c:
                            print( "   ---> " + title.tag  + ' = ' + str( title.text ) )
