#!/bin/bash

MYLOG=$1

echo "Creating backup directory" >> /Users/$USER/$MYLOG
mkdir /Users/$USER/work_backup

echo "Copying files" >> /Users/$USER/$MYLOG
cp -v /Users/$USER/work/* /Users/$USER/work_backup/ >> /Users/$USER/$MYLOG
echo "Finished copying files" >> /Users/$USER/$MYLOG
