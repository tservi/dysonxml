#!/usr/bin/env python

# python 3 
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as etree
from email.mime.text import MIMEText
import smtplib
#import sys, socket
    
myEvent = {}
def reset_myEvent() :
    return { 'event_id' : '' ,
            'title_fr' : '' ,
            'title_de' : '' ,
            'title_it' : '' ,
            'title_en' : '' ,
            'description_fr' : '' ,
            'description_de' : '' ,
            'description_it' : '' ,
            'description_en' : '' ,
            'date_from' : '' ,
            'date_to' : '' ,
            'time_from' : '' ,
            'time_to' : '' ,
            'additionnal_info_fr' : '' ,
            'additionnal_info_de' : '' ,
            'additionnal_info_it' : '' ,
            'additionnal_info_en' : '' ,
            'locality' : '',
            'street' : '' ,
            'address_info' : '' ,
            'price_from' : '' ,
            'price_to' : '' ,
            'phone' : '',
            'fax' : '' ,
            'url' : '' ,
            'email' : '' ,
            'yearly' : '' ,
            'picture_url' : '' ,
            }


def getinfos( ) :
    page    = urllib.request.urlopen( url )
    content = page.read( )#.decode( 'WINDOWS-1252' ).replace( '\r\n' , '' ).replace( '\n' , '' ).replace( '\t' , '' ) # .encode( 'UTF-8' )
    tree = etree.fromstring( content )  
    for child in tree:
        #print( str( child.tag  ) + ' = ' +  str ( child.attrib ) )
        if child.tag == "EVENT_LIST" : 
            for ch in child:
                #print( " -> " + str( ch.tag ) + ' = ' +  str ( ch.attrib ) )
                if ch.tag == "EVENT" :
                    myEvent = reset_myEvent()
                    for c in ch :
                        for key in myEvent :
                            if 'ID' in c.attrib and c.attrib[ 'ID' ] == key.upper():
                                for attrib in c:
                                    if attrib.tag == 'VALUE' :
                                        myEvent[ key ] = str( attrib.text ).replace( 'None' ,  '' )
                    found = 0
                    if len( myE ) > 0 :
                        for e in myE :
                            if 'id' in myE[ e ] and myE[ e ][ 'id' ] == myEvent[ 'id' ]:
                                found = found + 1
                    if found == 0 :
                        myE[ len( myE ) ] = myEvent


# reading the xml files
myE  = {}
urls  = ( 'http://vk.stnet.ch/XmlEventList.jsp?lang=de&maxrows=50000&cat=A&dateinterval=7000&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=de&maxrows=50000&cat=B&dateinterval=7000&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=de&maxrows=50000&cat=C&dateinterval=7000&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=de&maxrows=50000&cat=D&dateinterval=7000&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=de&maxrows=50000&cat=E&dateinterval=7000&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=de&maxrows=50000&cat=F&dateinterval=7000&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=de&maxrows=50000&cat=G&dateinterval=7000&rlevel=nat&fields=all' ,
        )
#for url in urls :
#    getinfos( )

# sending the mails : one email for every events
# install this program on windows http://www.softstack.com/freesmtp.html
#print ( myE )
#for event in myE :
text             = ''
text            += '<html>\n<head>\n<title>New event</title>\n</head>\n<body>\n'
text            += '</body>\n'
msg              = MIMEText( text, 'plain', 'WINDOWS-1252')
msg['Subject']   = 'Test depuis la machine 127.0.0.1 ...'
msg['From']      = "admin@ca-dev.com"
msg['Reply-to']  = "admin@ca-dev.com"
msg['To']        = "admin@ca-dev.com"
#print( msg )
s                = smtplib.SMTP()
#s.helo()
s.connect( "ca-dev.com"  )
s.ehlo( "ca-dev.com" )
#s.login( "user" , "pass" )

#s.sendmail( "<admin@ca-dev.com>" , "<admin@ca-dev.com>" , "subject: hello from 127.0.0.1\r\n\r\ntest depuis python\r\n\r\n.\r\n" )
s.close()
"""
    port = 25
    sock_req = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock_req.connect(( "127.0.0.1" , port) ) 
    #print(msg.as_string())
    #s = smtplib.SMTP()
    #s.sendmail( 'admin@ca-dev.com', 'admin@ca-dev.com' , msg.as_string())
    #s.quit()
    sock_req.send( bytes( "HELO <admin@ca-dev.com>\r\n" , "latin-1") )
    rep = sock_req.recv(1024)
    print(rep)
    sock_req.send( bytes( "MAIL FROM: <admin@ca-dev.com>\r\n" , "latin-1") )
    rep = sock_req.recv(1024)
    print(rep)
    sock_req.send( bytes( "RCPT TO: <admin@ca-dev.com>\r\n" , "latin-1") )
    rep = sock_req.recv(1024)
    print(rep)
    sock_req.send( bytes( "DATA\r\n" , "latin-1") )
    rep = sock_req.recv(1024)
    print(rep)
    sock_req.send( bytes( "from: <admin@ca-dev.com>\r\nto: <admin@ca-dev.com>\r\nsubject: nouvel event\r\n" + msg.as_string() , "latin-1") )
    rep = sock_req.recv(1024)
    print(rep)
    #print( sock_req.recv( 1024 ) )
    sock_req.send( bytes( "QUIT\r\n" , "latin-1") )
    rep = sock_req.recv(1024)
    print(rep)
    sock_req.close( )
"""
print( "The end! ")