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
myE  = {}
for child in tree:
    #print( str( child.tag  ) + ' = ' +  str ( child.attrib ) )
    if child.tag == "EVENT_LIST" : 
        for ch in child:
            print( " -> " + str( ch.tag ) + ' = ' +  str ( ch.attrib ) )
            if ch.tag == "EVENT" :
                myEvent = { 'id' : '' , 'title_fr' : '' , 'title_de' : '' ,'title_it' : ''  }
                for c in ch :
                    #print( "  --> " + str( c.tag ) + ' = ' + str( c.attrib ) )
                    if 'ID' in c.attrib and c.attrib[ 'ID' ] == 'EVENT_ID' :
                        for attrib in c:
                            if attrib.tag == 'VALUE' :
                                #print( "   ---> " + attrib.tag  + ' = ' + str( attrib.text ) )
                                myEvent[ 'id' ] = str( attrib.text ).replace( 'None' , '' )                 
                    if 'ID' in c.attrib and c.attrib[ 'ID' ] == 'TITLE_DE' :
                        #print( c )
                        for title in c:
                            if title.tag == 'VALUE' :
                                #print( "   ---> " + title.tag  + ' = ' + str( title.text ) )
                                myEvent[ 'title_de' ] = str( title.text ).replace( 'None' , '' )
                    if 'ID' in c.attrib and c.attrib[ 'ID' ] == 'TITLE_FR' :
                        #print( c )
                        for title in c:
                            if title.tag == 'VALUE' :
                                #print( "   ---> " + title.tag  + ' = ' + str( title.text ) )
                                myEvent[ 'title_fr' ] = str( title.text ).replace( 'None' , '' )
                    if 'ID' in c.attrib and c.attrib[ 'ID' ] == 'TITLE_IT' :
                        #print( c )
                        for title in c:
                            if title.tag == 'VALUE' :
                                #print( "   ---> " + title.tag  + ' = ' + str( title.text ) )
                                myEvent[ 'title_it' ] = str( title.text ).replace( 'None' , '' )
                found = 0
                if len( myE ) > 0 :
                    for e in myE :
                        #print( myE[ e ] )
                        if 'id' in myE[ e ] and myE[ e ][ 'id' ] == myEvent[ 'id' ]:
                            found = found + 1
                if found == 0 :
                    myE[ len( myE ) ] = myEvent
    
print ( myE )
