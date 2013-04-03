#!/bin/bash
if test -n "$1"; then 
    if test -r $1; then 
	infile=$1
	outfile=`echo $infile | sed -e "s/\.md$/.html/"` 
	if (/usr/bin/Markdown.pl "$infile" > "$outfile"); then
	    echo $outfile written successfully. 
	    #osascript -e ' 
            #tell application "Google Chrome"
            #    tell the active tab of its first window
            #        reload
            #    end tell
            # end tell
            # ' 
	fi
	
    else
	echo Input file does not exist. 
    fi
    
else
    echo Markdown conversion
    echo USAGE: $0 {filename.md}
    
fi
