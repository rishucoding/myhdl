#!/bin/bash

# two kinds of variables in shell script: environment and user
user1=$(whoami) # using command substitution
echo "Home for the current user *____ $user1 ____ * is $HOME " 
# $HOME is environment variable

# user variables
grade=5
person="rishu"
echo "$person has a github repository, he was in grade $grade"

# command substitution

dateis=$(date)
echo $dateis

# math calculation
var1=$(( 5 * 5 + 10 -100 + 36))
echo $var1

var2=$(( $var1 * 2))
echo $var2

# if else condition

if whoami
then
echo "if else It works"
fi

# check if a user exists
#user=Rishabh
user=mutdds
if grep $user /etc/passwd
    then
    echo "The user  $user exists"
    else
    echo "The user $user doesn't exist"
fi

# if elif fi command

if grep $user /etc/passwd
    then
    echo "The user $user exists"
    elif ls /home
    then
    echo "The uer $user user doesn't exist"
fi
    
