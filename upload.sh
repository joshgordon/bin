#!/bin/bash
httpRoot='http://grdn.me/pub/' 

#yourls api key: 
apikey=f9626d437c

#temp diretory
tempdir="/tmp"

#stupid thing doesn't support spaces... 


cleanName=`basename "$1" | sed "s/ /_/g"` 
#/usr/bin/basename "$1" | sed "s/ /_/g"


echo $cleanName

cp "$1" "$tempdir/$cleanName" 


echo scp

if (scp "$tempdir/$cleanName" gordonclan.net:~/josh/grdn/pub > /dev/null ); then
    

    echo cat

    http=$httpRoot$cleanName

    echo $http

    #shorten the url

    shortURL=`curl -s "http://grdn.me/yourls-api.php?signature=$apikey&action=shorturl&url=$http&format=simple"`

    echo $shortURL
else
    echo http://grdn.me/error.html
fi

