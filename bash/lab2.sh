#!/bin/bash

MYLOG=$1

cleanup () {
	echo "Recived ctrl c"
	rm -rf /home/$USER/work_backup
	exit 255
}

if [ -z $1 ]
then
	echo "Use parameter"
	exit 255
fi

echo "Timestamp before work is done $(date +"%D %T")" >> /home/$USER/$MYLOG
echo "Creating backup directory" >> /home/$USER/$MYLOG
mkdir /home/$USER/work_backup
trap cleanup SIGINT
echo "Copying Files" >> /home/$USER/$MYLOG
cp -v /home/$USER/work/* /home/$USER/work_backup/ >> /home/$USER/$MYLOG
echo "Finished Copying Files" >> /home/$USER/$MYLOG
echo "Timestamp after work is done $(date +"%D %T")" >> /home/$USER/$MYLOG
sleep 20