#!/bin/bash
# didn't get this example well... what is happening??? 
dir=/home/muts
name="muts"
if  [ -d $dir ] && [ -n $name ]; then
    echo "The name exists and the folder $dir exists, cooool!"
else
    echo "one test failed.. :("
fi

if  [ -d $dir ] || [ -n $name ]; then
    echo "Success! , cooool!"
else
    echo "both test failed.. :("
fi


