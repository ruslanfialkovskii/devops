#!/bin/bash

# Back up files

if [ -z $1 ]
then 
    echo "Need to supply a parameter for the logfile."
    exit 255
fi

LOGFILE=/Users/$USER/bash/$1
BACKUP_LOC="/Users/$USER/bash/work"
BACKUP_TARGET="/Users/$USER/bash/backup_work"

init () {
    if [ -d $BACKUP_TARGET ]
        then
            echo "Directory already exists"
            echo "$(date "+DATE: %Y-%m-%d%nTIME: %H:%M:%S")" >> $LOGFILE
            return 1
        else
            echo "Creating backup directory"
            echo "$(date "+DATE: %Y-%m-%d%nTIME: %H:%M:%S")" >> $LOGFILE
            mkdir $BACKUP_TARGET
        return 0
    fi
}

tail () {
    command tail -n $1
}

cleanup () {
    rm -rf $BACKUP_TARGET
    echo "RECEVIED CTRLC" >> $LOGFILE
}

init

trap cleanup SIGINT

cd $BACKUP_LOC
for i in $( ls ); do
    cp -v $i  $BACKUP_TARGET/"$i"-backup >> $LOGFILE 2>&1
done

grep -i denied $LOGFILE | tail 2

exit 127 
