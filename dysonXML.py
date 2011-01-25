#!/usr/bin/env python

# python 3 
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as etree
from email.mime.text import MIMEText
import smtplib
import sys, socket
import datetime

    
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
            'fk_category' : '' ,
            }


def getinfos( ) :
    page    = urllib.request.urlopen( url )
    content = page.read( )#.decode( 'WINDOWS-1252' )#.replace( '\r\n' , '' ).replace( '\n' , '' ).replace( '\t' , '' ) # .encode( 'UTF-8' )
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
                                    if attrib.tag == 'VALUE' and  attrib.text  is not 'None' :
                                        #print( attrib.text.__doc__ )
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
urls  = ( 'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=A&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=B&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=C&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=D&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=E&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=F&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=G&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=H&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=I&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=J&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=K&dateinterval=14&rlevel=nat&fields=all' ,
         'http://vk.stnet.ch/XmlEventList.jsp?lang=fr&maxrows=50000&cat=O&dateinterval=14&rlevel=nat&fields=all' ,
        )
for url in urls :
    getinfos( )

# sending the mails : one email for every events
# install this program on windows http://www.softstack.com/freesmtp.html
user             = ''
password         = ''
text             = ''
text            += '<html>\n<head>\n<title>New event</title>\n</head>\n<body>\n'
text            += 'Email de validation des events depuis myswitzerland.com<br/>\n'
for num in myE:
    event        = myE[ num ]
    eid          = 'myswitzerland.com.'
    text        += "<form method='post' action='http://www.suisseevents.ch/inject.php'>\n"
    text        += "<table border='1' style='width: 100%'>\n"
    text        += "<tr>\n"
    text        += "<td> "
    if 'event_id' in event:
        text    += event[ 'event_id' ]
        eid     += event[ 'event_id' ]
    text    += "<input type='hidden' name='event_id' value='" + eid + "' />"
    text        += "</td>"
    text        += "<td> "
    if 'title_fr' in event and len ( event[ 'title_fr' ] ) > 1 :
        text    += event[ 'title_fr' ] 
    text        += "</td>"
    text        += "<td> "
    if 'title_de' in event and len ( event[ 'title_de' ] ) > 1 :
        text    += event[ 'title_de' ]
    text        += "</td>"
    text        += "<td> "
    if 'title_it' in event and len ( event[ 'title_it' ] ) > 1 :
        text    += event[ 'title_it' ]
    text        += "</td>"
    text        += "<td> "
    if 'title_en' in event and len ( event[ 'title_en' ] ) > 1 :
        text    += event[ 'title_en' ]
    text        += "</td>"
    text        += "</tr>\n"

    for key in event:
        if key != 'event_id' and key != 'fk_category' :
            text += "<tr>\n"
            text += "<td>\n"
            text += str( key ) + ' : '
            text += "</td>\n"
            text += "<td colspan='4'>\n"
            text += "<textarea name='" + eid + '_' + key + "' style='width: 100%' >"
            text += event[ key ]
            text += "</textarea>"
            text += "</td>\n"
            text += "</tr>\n"

    if 'fk_category' in event :
            text += "<tr>\n"
            text += "<td>\n"
            text += "Categories  : "
            text += "</td>\n"
            text += "<td colspan='4'>\n"
            text += "<select name='" + eid + '_' + key + "' style='width: 100%' >"
            cats  = { 'A' : 'Concert - Discotheque - Festival - Jazz - World Music' ,
                     'B' : 'Spectacles - Theatres - Opera - Comedies ' ,
                     'C' : 'Divers' ,
                     'D' : 'Exposition - Foires - Conferences - Congres - Seminaires ',
                     'E' : 'Visites commentes - Manifestations ',
                     'F' : 'Festival' ,
                     'G' : 'Expositon - Foires' ,
                     'H' : 'Sport' ,
                     'I' : 'Musee' ,
                     'J' : 'Manifestation' ,
                     'K' : 'Gastronomie' ,
                     'O' : 'Divers' , 
                     }  
            for option in cats :
                text += "<option value='" + option
                text += "'"
                if event[ 'fk_category' ] == option :
                    text += " selected "
                text += ">" + cats[ option ] + "</option>"
            text += "</select>"
            text += "</td>\n"
            text += "</tr>\n"
    
    text        += "<tr><td colspan='5'><input type='submit' value='injecter cet evenement dans les sites events'></td></tr>\n"
    text        += "</table>\n"
    text        += "</form>\n"
    text        += "<br/><br/>\n"
text            += '</body>\n'
msg              = MIMEText( text, 'html', 'UTF-8')
now              = datetime.datetime.today()
msg['Subject']   = 'Aspiration myswitzerland.com ' + str( now )
msg['From']      = "info@t-servi.com"
msg['Reply-to']  = "info@t-servi.com"
msg['To']        = "aeschlimann.charles@gmail.com"
#print( msg )
s                = smtplib.SMTP( "ca-dev.com" )
#s.set_debuglevel( 1 )
s.ehlo()
s.login( user, password )
s.sendmail( "<info@t-servi.com>" , "<aeschlimann.charles@gmail.com>" ,msg.as_string() )
s.close()
print( "The end! ")